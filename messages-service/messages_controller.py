import hazelcast
import consul
from flask import Flask, make_response, request, jsonify

app = Flask(__name__)


@app.errorhandler(404)
def not_found():
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/messages', methods=['GET'])
def message():
    if request.method == 'GET':
        msg = []
        queue_l.drain_to(msg)
        return jsonify({'message': ", ".join(msg)})
    return not_found()


if __name__ == '__main__':
    c = consul.Consul(port=8500)
    hz_client = hazelcast.HazelcastClient(
            cluster_members=c.kv.get("hazelcast")[1]["Value"].decode("utf-8").split()
        )
    queue_l = hz_client.get_queue(c.kv.get("queue")[1]["Value"].decode("utf-8")).blocking()
    port = 5004
    c.agent.service.register(name="message-service", address="127.0.0.1", port=port, service_id=f"message-service:{port}")
    app.run(port=port, debug=True)
