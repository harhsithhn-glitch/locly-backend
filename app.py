from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Home route (test backend)
@app.route('/')
def home():
    return "LOCLY Backend Running 🚀"

# Booking route
@app.route('/book', methods=['POST'])
def book():
    data = request.json

    name = data.get('name')
    location = data.get('location')
    date = data.get('date')

    print("Booking:", name, location, date)

    return jsonify({
        "message": "Booking saved!"
    })

# IMPORTANT FOR RENDER
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)