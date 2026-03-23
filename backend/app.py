from flask import Flask, request, jsonify
from utils.auth import check_login
from utils.capital_gain_calculator import calculate_capital_gain
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "CA Portal Backend Running 🚀"

# 🔐 LOGIN API
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    
    username = data.get('username')
    password = data.get('password')

    if check_login(username, password):
        return jsonify({"message": "Login successful"})
    else:
        return jsonify({"message": "Invalid credentials"}), 401
    
# 📈 CAPITAL GAIN CALCULATOR API
@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json

    result = calculate_capital_gain(data)

    return jsonify(result)

import os

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))