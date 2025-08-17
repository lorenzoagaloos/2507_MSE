# Week 3 Activity 5 - (lorenzoagaloos-270729354)
# Re-using and updating the given code to add a new table "students" with three columns: Stu_ID, Stu_name, and Stu_address
# Insert two sample records into Students, then display all rows from both the Users and Student tables

from database import create_connection
import sqlite3

def add_student(Stu_name, Stu_address):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO students (Stu_name, Stu_address) VALUES (?, ?)", (Stu_name, Stu_address))
        conn.commit()
        print(" Student record added successfully.")
    except sqlite3.IntegrityError:
        print("Address must be unique.")
    conn.close()

def view_student():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_student(Stu_name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE Stu_name LIKE ?", ('%' + Stu_name + '%',))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_student(Stu_ID):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE Stu_ID = ?", (Stu_ID,))
    conn.commit()
    conn.close()
    print("🗑️ Student record deleted.")

def add_user(name, email):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        print("\nUser added successfully.")
    except sqlite3.IntegrityError:
        print(" Email must be unique.")
    conn.close()

def view_users():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_user(name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE name LIKE ?", ('%' + name + '%',))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_user(user_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()
    print("🗑️ User deleted.")