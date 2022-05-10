# Has only one client for 3 apps :(
import hazelcast
from flask import Flask, make_response, request, jsonify
import threading

app1 = Flask(__name__)
app2 = Flask(__name__)
app3 = Flask(__name__)

client = hazelcast.HazelcastClient(
    cluster_members=[

        "127.0.0.1:5701",

        "127.0.0.1:5702",

        "127.0.0.1:5703",

    ]
)

my_map = client.get_map("logging_map").blocking()


@app1.route('/')
def index1():
    return "Logging 1"


@app2.route('/')
def index2():
    return "Logging 2"


@app3.route('/')
def index3():
    return "Logging 3"


@app1.errorhandler(404)
@app2.errorhandler(404)
@app3.errorhandler(404)
def not_found():
    return make_response(jsonify({'error': 'Not found'}), 404)


@app1.route('/login', methods=['POST', 'GET'])
@app2.route('/login', methods=['POST', 'GET'])
@app3.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        my_map.lock(list(data.keys())[0])
        try:
            my_map.set(list(data.keys())[0], list(data.values())[0])
        finally:
            my_map.unlock(list(data.keys())[0])
        return jsonify({'success': True}), 200, {'ContentType': 'application/json'}
    elif request.method == 'GET':
        return jsonify({'login': ", ".join(list(my_map.values()))}), 200
    else:
        return not_found()


def start_app1():
    app1.run(port=5001, debug=False, threaded=True)


def start_app2():
    app2.run(port=5002, debug=False, threaded=True)


def start_app3():
    app3.run(port=5003, debug=False, threaded=True)


if __name__ == '__main__':
    t1 = threading.Thread(target=start_app1)
    t2 = threading.Thread(target=start_app2)
    t3 = threading.Thread(target=start_app3)
    t1.start()
    t2.start()
    t3.start()
