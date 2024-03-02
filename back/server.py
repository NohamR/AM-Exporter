from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app, resources={r"/music/*": {"origins": "http://*"}})

with open('.users', 'r') as file:
    users = json.load(file)

print(users)

@app.route('/music/set', methods=['POST'])
def set_content():
    global cache
    cache = request.get_json()
    if cache['user'] in users and users[cache['user']] == cache['password']:
        for key in ['user', 'password']:
            if key in cache:
                del cache[key]
        return jsonify({'message': 'Content set successfully.'})
    else:
        return jsonify({'message': 'Invalid user or password.'})

@app.route('/music/get', methods=['GET'])
def display_content():
    return jsonify(cache)

if __name__ == '__main__':
    app.run(debug=True)