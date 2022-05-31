import json
import uuid
import random
import requests
import hazelcast
import consul
from flask import Flask, request, jsonify, make_response, abort

app = Flask(__name__)

port = 5000

@app.errorhandler(404)
def not_found():
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/facade_service', methods=['POST', 'GET'])
def facade():
    hz_client = hazelcast.HazelcastClient(
            cluster_members=c.kv.get("hazelcast")[1]["Value"].decode("utf-8").split()
        )

    queue_client = hz_client.get_queue(c.kv.get("queue")[1]["Value"].decode("utf-8")).blocking()

    if request.method == 'POST':
        if not request.json:
            abort(400)
        request_data = request.get_json()
        uuid_user = uuid.uuid4()
        print(["127.0.0.1:" + str(value['Port']) for value in c.agent.services().values() if value["Service"] == 'login-service'])
        login_rand = random.choice(["http://127.0.0.1:" + str(value['Port'])
                                    for value in c.agent.services().values() if value["Service"] == 'login-service']) + "/login"
        response = requests.post(url=login_rand, data=json.dumps({str(uuid_user): str(request_data)}),
                                 headers={'Content-Type': 'application/json'})
        queue_client.add(str(request_data))
        return response.content

    elif request.method == 'GET':
        login_rand = random.choice(["http://127.0.0.1:" + str(value['Port']) for
                                    value in c.agent.services().values() if value["Service"] == 'login-service']) + "/login"
        response_l = requests.get(url=login_rand).json()
        mes_rand = random.choice(["http://127.0.0.1:" + str(value['Port'])
                                  for value in c.agent.services().values() if value["Service"] == "message-service"]) + "/messages"
        response_m = requests.get(url=mes_rand).json()
        return jsonify(response_l, response_m)
    else:
        not_found()


if __name__ == '__main__':
    c = consul.Consul(port=8500)
    c.agent.service.register(name="facade_service", address="127.0.0.1", port=port, service_id=f"facade_service:{port}")
    print(c.agent.services())
    app.run(port=port, debug=True)
