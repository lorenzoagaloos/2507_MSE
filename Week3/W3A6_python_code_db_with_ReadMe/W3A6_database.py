# Week 3 - Activity 6: Develop the python code for Week 3 - Activity 4 (lorenzoagaloos-270729354)
# Use the sample code to develop a command-line application for Week 3 – Activity 4, incorporating a database sqlite3
# Should have at least three functionality such as add records, delete records and view records for different tables
# Should including a README.txt file in your repository to describe the technical aspects of this project (Yoobee Colleges)

import sqlite3

# Create a connection to the SQLite database
# The database file will be created if it does not exist
def create_connection():
    conn = sqlite3.connect("Week3\W3A6_python_code_db_with_ReadMe\yoobee.db")
    conn.execute("PRAGMA foreign_keys = ON")  # Enable foreign key support
    return conn

# Create Lecturer table
def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS Lecturer (
            Lect_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            Email TEXT NOT NULL UNIQUE,
            Department TEXT NOT NULL
        )
    ''')
    conn.commit()
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS Subject (
            Subj_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Subj_Name TEXT NOT NULL,
            SubjectCode TEXT NOT NULL UNIQUE,
            CreditHours INTEGER NOT NULL,
            Lect_ID INTEGER,
                FOREIGN KEY (Lect_ID) REFERENCES Lecturer(Lect_ID)
        )
    ''')
    conn.commit()
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS Students (
            Stud_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            Email TEXT NOT NULL UNIQUE,
            Enrol_date TEXT NOT NULL,
            Subj_ID INTEGER,
                FOREIGN KEY (Subj_ID) REFERENCES Subject(Subj_ID)
        )
    ''')
    conn.commit()
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS Assessments (
            Assess_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            AssessmentName TEXT NOT NULL,
            AssessmentType TEXT NOT NULL,
            MaxGrade INTEGER NOT NULL,
            DueDate TEXT NOT NULL,
            Subj_ID INTEGER NOT NULL,
            Stud_ID INTEGER NOT NULL,
            Stud_Grade INTEGER DEFAULT 0,
            Status TEXT DEFAULT 'Pending',  
                FOREIGN KEY (Subj_ID) REFERENCES Subject(Subj_ID),
                FOREIGN KEY (Stud_ID) REFERENCES Students(Stud_ID)
        )
    ''')
    conn.commit()
    conn.close()

