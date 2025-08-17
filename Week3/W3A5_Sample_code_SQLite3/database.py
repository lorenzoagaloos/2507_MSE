# Week 3 Activity 5 - (lorenzoagaloos-270729354)
# Re-using and updating the given code to add a new table "Students" with three columns: Stu_ID, Stu_name, and Stu_address
# Insert two sample records into Students, then display all rows from both the Users and Students tables

import sqlite3

def create_connection():
    conn = sqlite3.connect("Week3\W3A5_Sample_code_SQLite3\students.db")
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            Stu_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Stu_name TEXT NOT NULL,
            Stu_address TEXT NOT NULL UNIQUE
        )
    ''')
    conn.commit()
    conn.close()
