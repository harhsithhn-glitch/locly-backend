from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "LOCLY Backend Running 🚀"

@app.route('/book', methods=['POST'])
def book():
    data = request.json
    print("Booking:", data)
    return jsonify({"message": "Booking saved!"})

import os
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)