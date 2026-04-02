from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

# CREATE DATABASE
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            location TEXT,
            date TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def home():
    return "LOCLY Backend Running 🚀"

@app.route('/book', methods=['POST'])
def book():
    data = request.json

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO bookings (name, location, date) VALUES (?, ?, ?)",
              (data['name'], data['location'], data['date']))
    conn.commit()
    conn.close()

    return jsonify({"message": "Booking saved in database!"})

if __name__ == '__main__':
    app.run(debug=True)