from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import os

app = Flask(__name__)
CORS(app)

# ---------------- DATABASE ----------------
def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            location TEXT,
            date TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

# ---------------- ROUTES ----------------
@app.route('/')
def home():
    return "LOCLY Backend Running 🚀"

@app.route('/book', methods=['POST'])
def book():
    data = request.json
    name = data.get('name')
    location = data.get('location')
    date = data.get('date')

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO bookings (name, location, date) VALUES (?, ?, ?)",
                   (name, location, date))
    conn.commit()
    conn.close()

    return jsonify({"message": "Booking saved!"})

# NEW ROUTE 🔥
@app.route('/bookings', methods=['GET'])
def get_bookings():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bookings")
    rows = cursor.fetchall()
    conn.close()

    bookings = []
    for row in rows:
        bookings.append({
            "id": row[0],
            "name": row[1],
            "location": row[2],
            "date": row[3]
        })

    return jsonify(bookings)

# ---------------- RUN ----------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)