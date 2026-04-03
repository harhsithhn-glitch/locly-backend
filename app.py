from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import os

app = Flask(__name__)
CORS(app)

# -------- DATABASE --------
def init_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        phone TEXT,
        email TEXT,
        dob TEXT,
        age TEXT,
        gender TEXT,
        address TEXT,
        emergency TEXT
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS bookings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        location TEXT,
        date TEXT,
        payment_status TEXT
    )
    """)

    conn.commit()
    conn.close()

init_db()

# -------- ROUTES --------

@app.route('/')
def home():
    return "LOCLY Backend Running 🚀"

# SAVE USER
@app.route('/save_user', methods=['POST'])
def save_user():
    data = request.json

    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    c.execute("""
    INSERT INTO users (name, phone, email, dob, age, gender, address, emergency)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        data['name'],
        data['phone'],
        data['email'],
        data['dob'],
        data['age'],
        data['gender'],
        data['address'],
        data['emergency']
    ))

    conn.commit()
    conn.close()

    return jsonify({"message": "User saved!"})

# BOOKING
@app.route('/book', methods=['POST'])
def book():
    data = request.json

    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    c.execute("""
    INSERT INTO bookings (name, location, date, payment_status)
    VALUES (?, ?, ?, ?)
    """, (
        data['name'],
        data['location'],
        data['date'],
        data['payment_status']
    ))

    conn.commit()
    conn.close()

    return jsonify({"message": "Booking saved!"})

# GET BOOKINGS
@app.route('/bookings', methods=['GET'])
def get_bookings():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    c.execute("SELECT * FROM bookings")
    rows = c.fetchall()

    conn.close()

    result = []
    for row in rows:
        result.append({
            "id": row[0],
            "name": row[1],
            "location": row[2],
            "date": row[3],
            "payment_status": row[4]
        })

    return jsonify(result)

# -------- RUN --------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)