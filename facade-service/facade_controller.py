import json
import uuid
import random
import requests
import hazelcast
from flask import Flask, request, jsonify, make_response, abort

app = Flask(__name__)


@app.errorhandler(404)
def not_found():
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/facade_service', methods=['POST', 'GET'])
def facade():
    login_url = ("http://127.0.0.1:5001/login", "http://127.0.0.1:5002/login", "http://127.0.0.1:5003/login")
    mes_url = ("http://127.0.0.1:5004/messages", "http://127.0.0.1:5005/messages")
    hz_client = hazelcast.HazelcastClient(
        cluster_members=[
            "127.0.0.1:5701",
        ]
    )
    queue_client = hz_client.get_queue("queue").blocking()
    if request.method == 'POST':
        if not request.json:
            abort(400)
        request_data = request.get_json()
        uuid_user = uuid.uuid4()
        login_rand = random.choice(login_url)
        response = requests.post(url=login_rand, data=json.dumps({str(uuid_user): str(request_data)}),
                                 headers={'Content-Type': 'application/json'})
        queue_client.add(str(request_data))
        return response.content

    elif request.method == 'GET':
        login_rand = random.choice(login_url)
        response_l = requests.get(url=login_rand).json()
        mes_rand = random.choice(mes_url)
        response_m = requests.get(url=mes_rand).json()
        return jsonify(response_l, response_m)
    else:
        not_found()


if __name__ == '__main__':
    app.run(port=5000, debug=True)
