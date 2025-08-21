# Week 3 - Activity 6: Develop the python code for Week 3 - Activity 4 (lorenzoagaloos-270729354)
# Use the sample code to develop a command-line application for Week 3 – Activity 4, incorporating a database sqlite3
# Should have at least three functionality such as add records, delete records and view records for different tables
# Should including a README.txt file in your repository to describe the technical aspects of this project (Yoobee Colleges)

from W3A6_database import create_connection
import sqlite3

# Functions to manage student records
def add_student(Name, Email, Enrol_Date, Subj_ID):
    conn = create_connection()
    conn.execute("PRAGMA foreign_keys = ON")  # Enable foreign key support
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO students (Name, Email, Enrol_Date, Subj_ID) VALUES (?, ?, ?, ?)", (Name, Email, Enrol_Date, Subj_ID))
        conn.commit()
        print("\nStudent record added successfully.")
    except sqlite3.IntegrityError:
        print("Student email must be unique.")
    conn.close()

def view_student():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Students")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_student(Name):
    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Students WHERE Name LIKE ?", ('%' + Name + '%',))
        rows = cursor.fetchall()
    finally:
        if not rows:
            print("No student record found with that name.")
        else:
            return rows
    conn.close()


def delete_student(Stud_ID):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Students WHERE Stud_ID = ?", (Stud_ID,))
    conn.commit()
    conn.close()
    print("🗑️ Student record deleted.")

# Functions to manage lecturer records
def add_lecturer(Name, Email, Department):
    conn = create_connection()
    conn.execute("PRAGMA foreign_keys = ON")  # Enable foreign key support
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO Lecturer (Name, Email, Department) VALUES (?, ?, ?)", (Name, Email, Department))
        conn.commit()
        print("\nLecturer added successfully.")
    except sqlite3.IntegrityError:
        print("Lecturer email must be unique.")
    conn.close()

def view_lecturer():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Lecturer")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_lecturer(Name):
    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Lecturer WHERE Name LIKE ?", ('%' + Name + '%',))
        rows = cursor.fetchall()
    finally:
        if not rows:
            print("No lecturer record found with that name.")
        else:
            return rows
    conn.close()
    

def delete_lecturer(Lect_ID):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Lecturer WHERE Lect_ID = ?", (Lect_ID,))
    conn.commit()
    conn.close()
    print("🗑️ Lecturer record deleted.")


# Functions to manage Subject records
def add_subject(Subj_Name, SubjectCode, CreditHours, Lect_ID):
    conn = create_connection()
    conn.execute("PRAGMA foreign_keys = ON")  # Enable foreign key support
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO Subject (Subj_Name, SubjectCode, CreditHours, Lect_ID) VALUES (?, ?, ?, ?)", (Subj_Name, SubjectCode, CreditHours, Lect_ID))
        conn.commit()
        print("\nSubject record added successfully.")
    except sqlite3.IntegrityError:
        print("SubjectCode must be unique.")
    conn.close()

def view_subject():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Subject")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_subject(Subj_Name):
    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Subject WHERE Subj_Name LIKE ?", ('%' + Subj_Name + '%',))
        rows = cursor.fetchall()
    finally:
        if not rows:
            print("No subject found with that name.")
        else:
            return rows
    conn.close()

def delete_subject(Subj_ID):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Subject WHERE Subj_ID = ?", (Subj_ID,))
    conn.commit()
    conn.close()
    print("🗑️ Subject record deleted.")

# Functions to manage Assessments records
def add_assessment(AssessmentName, AssessmentType, MaxGrade, DueDate, Subj_ID, Stud_ID, Stud_Grade, Status):

    # Insert the assessment record into the database
    conn = create_connection()
    conn.execute("PRAGMA foreign_keys = ON")  # Enable foreign key support
    cursor = conn.cursor()
    
    try:
        cursor.execute("INSERT INTO Assessments (AssessmentName, AssessmentType, MaxGrade, DueDate, Subj_ID, Stud_ID, Stud_Grade, Status) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (AssessmentName, AssessmentType, MaxGrade, DueDate, Subj_ID, Stud_ID, Stud_Grade, Status))
        conn.commit()
        print("\nAssessment record added successfully.")
    except sqlite3.IntegrityError:
        print("Assess_Code must be unique.")   
    conn.close()

def view_assessment():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Assessments")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_assessmentName(AssessmentName):
    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Assessments WHERE AssessmentName LIKE ?", ('%' + AssessmentName + '%',))
        rows = cursor.fetchall()
    finally:
        if not rows:
            print("No assessment found with that name.")
        else:
            return rows
    conn.close()
    
def delete_assessment(Assess_ID):
    conn = create_connection()
    conn.execute("PRAGMA foreign_keys = ON")  # Enable foreign key support
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Assessments WHERE Assess_ID = ?", (Assess_ID,))
    conn.commit()
    conn.close()
    print("🗑️ Assessment record deleted.")

def edit_assessment(Assess_ID):
    conn = create_connection()
    conn.execute("PRAGMA foreign_keys = ON")  # Enable foreign key support
    cursor = conn.cursor()
    cursor.execute("Select * FROM Assessments WHERE Assess_ID = ?", (Assess_ID,))
    assessment = cursor.fetchone()
    if not assessment:
        print("No assessment found with that ID.")
        conn.close()
        return
    
    print(f"Current Assessment: {assessment}")
    Stud_Grade = input("Enter new Student Grade (or press Enter to keep current): ")
    if Stud_Grade == '':
        Stud_Grade = assessment[6]  # Keep current grade if no input
    else:
        try:
            Stud_Grade = float(Stud_Grade)
        except ValueError:
            print("Invalid grade input. Keeping current grade.")
            Stud_Grade = assessment[6]

    Status = input("Enter new Status ((Pending/Passed/Failed): ")
    if Status not in ['Pending', 'Passed', 'Failed']:
        print("Invalid status. Keeping current status.")
        Status = assessment[7]  # Keep current status if invalid input
    else:
        Status = Status
    cursor.execute("UPDATE Assessments SET Stud_Grade = ?, Status = ? WHERE Assess_ID = ?", (Stud_Grade, Status, Assess_ID))

    conn.commit()
    conn.close()
    print