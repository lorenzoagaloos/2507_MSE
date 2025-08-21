README.TXT
Yoobee College MSE800 2507 Section-A Database Application

WHAT IS THIS PROJECT?
This is a simple command-line application that manages student records for Yoobee College MSE800 2507 Intake Section-A. It is designed to be a beginner-friendly project to learn Python programming and database concepts using SQLite.

WHO MADE THIS?
This project was created by a Master's of Software Engineering student learning about Python and databases. As much as possible, it is meant to be organised and structured yet simple enough for anyone just starting to code to understand and modify.

WHAT DOES IT DO?
The application lets you:
- Add new lecturers, subjects, students, and assessments to a database
- View all records available in each table
- Delete records you don't need anymore
- Edit an assessment based on the grade a student receives as well as the student's status (Pending, Passed, or Failed) at the end of each assessment
- Automatically creates the database file when the application is first run

TECHNICAL
Programming Language Used:
- Python 3.11
- Uses built-in libraries

Database:
- SQLite3
- Creates a database file called "yoobee.db" in the same folder where the program is saved
- Has 4 tables: LECTURER, SUBJECT, STUDENTS, and ASSESSMENTS

How the Database is Connected:
- Lecturers teach subjects (one lecturer can teach many subjects)
- Students are enrolled in subjects (each student has at least one subject)
- Assessments belong to both a subject and a student
- Everything is connected with ID numbers (foreign keys)

HOW TO RUN THIS PROGRAM
Step 1: Save the Code
- Save the Python codes on your preferred folder
- There will be three files to save: "main.py"; "records_manager.py", and "database.py""
- Be sure to have Python installed on your computer

Step 2: Run the Program
- Open a command prompt or an IDE terminal
- Navigate to the folder where you saved the file
- Type: python main.py
- Press Enter
- In VSCode, open the "main.py" file
- Then run the python file

Step 3: Use the Menus
- The program will show you numbered menu options
- Type the number and press Enter to choose what you would like to do
- Follow the prompts to add, view, delete, edit records, and exit the application

WHAT FILES WILL BE CREATED?
When you run the program for the first time, it will create:
- "yoobee.db" (a generated SQLite database file)

USER-FRIENDLY FEATURES
Simple Menu System:
- Everything is organized in easy-to-follow menus and sub-menus
- Type the numbers to choose what you want to do
- Instructions are intuitive enough for every step

Helpful Prompts:
- When adding records, it asks what information to enter

Error Prevention:
- Prompts users when there are no records found during search
- Uses simple input validation

WHAT YOU CAN LEARN FROM THIS CODE
Python Concepts:
- Functions and how to organize code
- Working with user input
- Simple loops and if/else statements
- String formatting and printing

Database Concepts:
- Creating tables with SQL
- Primary keys and foreign keys
- INSERT, SELECT, and DELETE operations
- Basic table relationships

Programming Skills:
- How to structure a menu-driven program
- Breaking big problems into smaller functions
- Working with external files and databases
- Basic error handling

POSSIBLE IMPROVEMENTS (For practice and learning)
If you want to practice more programming, try adding:
- More edit/update for all existing records
- Add more validation (like checking email and date formats)
- Add more error handling functions for invalid entries
- Make more aesthetic table and user-interface displays
- Add a simple backup feature

TROUBLESHOOTING
Program Won't Start:
- Make sure Python is installed
- Check that the file name ends with .py
- Try running from the command line, not by double-clicking

Database Errors:
- Delete the yoobee.db file and restart the program
- This will create a fresh, empty database

Unable to See Your Data:
- Make sure you're adding records before trying to view them
- Start with adding a lecturer, then a subject, then students, and then finally assessments

FILES IN THIS PROJECT
- main.py (the main program file)
- records_manager.py (stores the data entry and manipulation functions for each table created)
- database.py (stores the database creation function when you run the program)
- yoobee.db (automatically created database when you run the program)
- README.TXT (this file with instructions)

