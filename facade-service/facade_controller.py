import json
import uuid

import requests
from flask import Flask, request, jsonify, make_response, abort

app = Flask(__name__)


@app.errorhandler(404)
def not_found():
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/facade_service', methods=['POST', 'GET'])
def facade():
    login_url = "http://127.0.0.1:5001/login"
    mes_url = "http://127.0.0.1:5002/messages"
    if request.method == 'POST':
        if not request.json:
            abort(400)
        request_data = request.get_json()
        uuid_user = uuid.uuid4()
        response = requests.post(url=login_url, data=json.dumps({str(uuid_user): str(request_data)}),
                                 headers={'Content-Type': 'application/json'})
        return response.content

    elif request.method == 'GET':
        response_l = requests.get(url=login_url).json()
        response_m = requests.get(url=mes_url).json()

        return jsonify(response_l, response_m)
    else:
        not_found()


if __name__ == '__main__':
    app.run(port=5000, debug=True)
