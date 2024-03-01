from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/music/*": {"origins": "http://127.0.0.1:5500"}})

@app.route('/music/set', methods=['POST'])
def set_content():
    global cache
    cache = request.get_json()
    return jsonify({'message': 'Content set successfully'})

@app.route('/music/get', methods=['GET'])
def display_content():
    return jsonify(cache)

if __name__ == '__main__':
    app.run(debug=True)