from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/music/set', methods=['POST'])
def set_content():
    global cache
    cache = request.get_json()
    return jsonify({'message': 'Content set successfully'})

@app.route('/music/display', methods=['GET'])
def display_content():
    return jsonify(cache)

if __name__ == '__main__':
    app.run(debug=True)
