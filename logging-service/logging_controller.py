from flask import Flask, make_response, request, jsonify

app = Flask(__name__)
req_data = {}


@app.errorhandler(404)
def not_found():
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        req_data.update(request.get_json())
        return jsonify({'success':True}), 200, {'ContentType':'application/json'}
    elif request.method == 'GET':
        return jsonify({'login': ", ".join(list(req_data.values()))}), 200
    else:
        return not_found()


if __name__ == '__main__':
    app.run(port=5001, debug=True)
