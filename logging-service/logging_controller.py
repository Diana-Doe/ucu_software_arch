import hazelcast
import signal
from flask import Flask, make_response, request, jsonify


class LoginService:
    def __init__(self, port, node):
        self.app = Flask(__name__)
        self.port = port
        self.client = hazelcast.HazelcastClient(
            cluster_members=[

                node,

            ]
        )

        self.my_map = self.client.get_map("logging_map").blocking()

    def run(self):
        @self.app.errorhandler(404)
        def not_found():
            return make_response(jsonify({'error': 'Not found'}), 404)

        @self.app.route('/login', methods=['POST', 'GET'])
        def login():
            if request.method == 'POST':
                data = request.get_json()
                self.my_map.lock(list(data.keys())[0])
                try:
                    self.my_map.set(list(data.keys())[0], list(data.values())[0])
                finally:
                    self.my_map.unlock(list(data.keys())[0])
                return jsonify({'success': True}), 200, {'ContentType': 'application/json'}
            elif request.method == 'GET':
                return jsonify({'login': ", ".join(list(self.my_map.values()))}), 200
            else:
                return not_found()

        self.app.run(port=self.port, debug=True)

    def shut(self):
        self.client.shutdown()


if __name__ == '__main__':
    s = LoginService(5001, "127.0.0.1:5701")
    s.run()
    s.shut()
    # app.run(port=5001, debug=False, threaded=True)
