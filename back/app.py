from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import hashlib

app = Flask(__name__)
CORS(app, resources={r"/music/*": {"origins": "http://*"}})

with open('.users', 'r') as file:
    users = json.load(file)

cache = {}

@app.route('/music/set', methods=['POST'])
def set_content():
    data = request.get_json()
    user = data.get('user')
    password = data.get('password')
    if user in users and users[user] == hashlib.sha256(password.encode()).hexdigest():
        # cache.clear()
        cache.update(data)
        cache.pop('user', None)
        cache.pop('password', None)
        return jsonify({'message': f'Content set successfully.'})
    else:
        return jsonify({'message': 'Invalid user or password.'}), 401

@app.route('/music/get', methods=['GET'])
def display_content():
    return jsonify(cache)

if __name__ == '__main__':
    app.run(debug=True)