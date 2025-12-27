import sqlite3
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "database.db")
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE doctors (
    doctor_id INTEGER PRIMARY KEY,
    doctor_name TEXT
)
""")

cursor.execute("""
CREATE TABLE patients (
    patient_id INTEGER PRIMARY KEY,
    patient_name TEXT,
    doctor_id INTEGER
)
""")

cursor.execute("INSERT INTO doctors VALUES (1, 'Dr. Sharma')")
cursor.execute("INSERT INTO doctors VALUES(2,'Dr. Adithya')")
cursor.execute("INSERT INTO patients VALUES (1, 'Rahul', 1)")
cursor.execute("INSERT INTO patients VALUES (2, 'Anita', 1)")
cursor.execute("INSERT INTO patients VALUES(1,'Aravind',2)")
cursor.execute("INSERT INTO patients VALUES(2,'Gayathri',2)")

conn.commit()
conn.close()