import hazelcast
from flask import Flask, make_response, request, jsonify

app = Flask(__name__)

hz_listener = hazelcast.HazelcastClient(
    cluster_members=[
        "127.0.0.1:5702",
    ]
)

queue_l = hz_listener.get_queue("queue").blocking()


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
    app.run(port=5004, debug=True)
