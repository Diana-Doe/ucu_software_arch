from flask import Flask, make_response, request, jsonify

app = Flask(__name__)


@app.errorhandler(404)
def not_found():
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/messages', methods=['GET'])
def message():
    if request.method == 'GET':
        return jsonify({'messages': "Not implemented yet!"})
    return not_found()


if __name__ == '__main__':
    app.run(port=5004, debug=True)
