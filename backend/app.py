from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3
import os

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "database.db")

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def home():
    return "Flask backend is running"

@app.route("/doctors")
def get_doctors():
    conn = get_db_connection()
    doctors = conn.execute("SELECT * FROM doctors").fetchall()
    conn.close()
    return jsonify([dict(row) for row in doctors])

@app.route("/patients")
def get_patients():
    conn = get_db_connection()
    patients = conn.execute("SELECT * FROM patients").fetchall()
    conn.close()
    return jsonify([dict(row) for row in patients])

@app.route("/doctor/<int:doctor_id>")
def get_doctor_patients(doctor_id):
    conn = get_db_connection()
    patients = conn.execute(
        "SELECT * FROM patients WHERE doctor_id = ?", (doctor_id,)
    ).fetchall()
    conn.close()
    return jsonify([dict(row) for row in patients])

if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(host="127.0.0.1", port=5000, debug=True)
