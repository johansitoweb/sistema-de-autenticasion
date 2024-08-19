from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your_secret_key'
jwt = JWTManager(app)

users = {}

@app.route('/register', methods=['POST'])
def register():
    user = request.json
    users[user['username']] = user['password']
    return jsonify({"msg": "User registered"}), 201

@app.route('/login', methods=['POST'])
def login():
    user = request.json
    if user['username'] in users and users[user['username']] == user['password']:
        access_token = create_access_token(identity=user['username'])
        return jsonify(access_token=access_token)
    return jsonify({"msg": "Bad username or password"}), 401

if __name__ == '__main__':
    app.run(debug=True)
