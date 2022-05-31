import hazelcast
import consul
from flask import Flask, make_response, request, jsonify


class LoginService:
    def __init__(self, port):
        self.app = Flask(__name__)
        self.port = port
        self.client = hazelcast.HazelcastClient(
            cluster_members=c.kv.get("hazelcast")[1]["Value"].decode("utf-8").split()
        )

        self.my_map = self.client.get_map(c.kv.get("map")[1]["Value"].decode("utf-8")).blocking()

        # self.my_map = self.client.get_map("logging_map").blocking()

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
    c = consul.Consul(port=8500)
    port = 5002
    s = LoginService(port)
    c.agent.service.register(name="login-service", address="127.0.0.1", port=port, service_id=f"login-service:{port}")
    s.run()
    s.shut()
