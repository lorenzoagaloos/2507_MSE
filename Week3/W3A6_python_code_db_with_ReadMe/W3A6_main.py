# Week 3 - Activity 6: Develop the python code for Week 3 - Activity 4 (lorenzoagaloos-270729354)
# Use the sample code to develop a command-line application for Week 3 – Activity 4, incorporating a database sqlite3
# Should have at least three functionality such as add records, delete records and view records for different tables
# Should including a README.txt file in your repository to describe the technical aspects of this project (Yoobee Colleges)


from W3A6_database import create_table
from W3A6_records_manager import add_student, view_student, search_student, delete_student, add_lecturer, view_lecturer, search_lecturer, delete_lecturer, add_subject, view_subject, search_subject, delete_subject, add_assessment, view_assessment, search_assessmentName, delete_assessment, edit_assessment

def main_menu():
    print("\n==== Yoobee MSE800 2507 Section A Records Manager ====")
    print("1. Student Management")
    print("2. Lecturer Management")
    print("3. Subject Management")
    print("4. Assessment Management")
    print("5. Exit")

def stud_menu_():
    print("\n==== Student Records Manager ====")
    print("1. Add Student")
    print("2. View all Students")
    print("3. Search Student by Name")
    print("4. Delete Student by ID")
    print("5. Back to Main Menu")
    print("\nSelect Student Menu option:")

def lect_menu_():
    print("\n==== Lecturer Records Manager ====")
    print("1. Add Lecturer")
    print("2. View all Lecturers")
    print("3. Search Lecturer by Name")
    print("4. Delete Lecturer by ID")
    print("5. Back to Main Menu")
    print("\nSelect Lecturer Menu option:")

def subj_menu_():
    print("\n==== Subject Records Manager ====")
    print("1. Add Subject")
    print("2. View all Subjects")
    print("3. Search Subject by Name")
    print("4. Delete Subject by ID")
    print("5. Back to Main Menu")
    print("\nSelect Subject Menu option:")

def assess_menu_():
    print("\n==== Assessment Records Manager ====")
    print("1. Add Assessment")
    print("2. View all Assessments")
    print("3. Search Assessment by Name")
    print("4. Delete Assessment by ID")
    print("5. Edit Assessment Grade and Status by ID")
    print("6. Back to Main Menu")
    print("\nSelect Assessment Menu option:")


def main():
    create_table() # Create the database and tables if they do not exist
    print("\nWelcome to the Yoobee MSE800 2507 Section A Records Manager!")
    print("This application allows you to manage student, lecturer, subject, and assessment records.")
    while True:
        main_menu()
        choice = input("\nSelect a Records Management option (1-5): ")
        if choice == '1':
            stud_menu_()
            stud_choice = input("\nSelect Student option (1-5): ")
            if stud_choice == '1':
                Name = input("Enter name: ")
                Email = input("Enter email: ")
                Enrol_Date = input("Enter enrolment date: ")
                Subj_ID = int(input("Enter Subject ID: "))
                add_student(Name, Email, Enrol_Date, Subj_ID)
            elif stud_choice == '2':
                students = view_student()
                print("\nAll Student Records:")
                for student in students:
                    print(student)
            elif stud_choice == '3':
                Name = input("\nEnter student name to search: ")
                students = search_student(Name)
                print(f"\n{students}")
            elif stud_choice == '4':
                Stu_ID = int(input("Enter Student ID to delete: "))
                delete_student(Stu_ID)
            elif stud_choice == '5':
                continue
            else:
                print("\nInvalid choice, try again.")
        
        elif choice == '2':
            lect_menu_()
            lect_choice = input("\nSelect Lecturer option (1-5): ")
            if lect_choice == '1':
                Name = input("Enter name: ")
                Email = input("Enter email: ")
                Department = input("Enter department: ")
                add_lecturer(Name, Email, Department)
            elif lect_choice == '2':
                lecturers = view_lecturer()
                print("\nAll Lecturer Records:")
                for lecturer in lecturers:
                    print(lecturer)
            elif lect_choice == '3':
                Name = input("\nEnter lecturer name to search: ")
                lecturers = search_lecturer(Name)
                print(f"\n{lecturers}")
            elif lect_choice == '4':
                Lect_ID = int(input("Enter Lecturer ID to delete: "))
                delete_lecturer(Lect_ID)
            elif lect_choice == '5':
                continue
            else:
                print("\nInvalid choice, try again.")
        
        elif choice == '3':
            subj_menu_()
            subj_choice = input("\nSelect Subject option (1-5): ")
            if subj_choice == '1':
                Subj_Name = input("Enter subject name: ")
                SubjectCode = input("Enter subject code: ")
                CreditHours = int(input("Enter credit hours: "))
                Lect_ID = int(input("Enter Lecturer ID: "))
                add_subject(Subj_Name, SubjectCode, CreditHours, Lect_ID)
            elif subj_choice == '2':
                subjects = view_subject()
                print("\nAll Subject Records:")
                for subject in subjects:
                    print(subject)
            elif subj_choice == '3':
                Subj_Name = input("\nEnter subject name to search: ")
                subjects = search_subject(Subj_Name)
                print(f"\n{subjects}")
            elif subj_choice == '4':
                Subj_ID = int(input("Enter Subject ID to delete: "))
                delete_subject(Subj_ID)
            elif subj_choice == '5':
                continue
            else:
                print("\nInvalid choice, try again.")

        elif choice == '4':
            assess_menu_()
            assess_choice = input("\nSelect Assessment option (1-5): ")
            if assess_choice == '1':
                
                print("\n--- Add new student assessment record ---")
                AssessmentName = input("Enter Assessment Name: ")
                AssessmentType = input("Enter Assessment Type (Exam/Activity/Assessment): ")
                MaxGrade = int(input("Enter Maximum Grade: "))
                DueDate = input("Enter Due Date (DD-MMM-YY): ")
    
                view_subject()
                Subj_ID = int(input("Enter Subject ID: "))
    
                view_student()
                Stud_ID = int(input("Enter Student ID: "))
    
                Stud_Grade = input("Enter Student Grade (or press Enter ): ")
                if Stud_Grade == '':
                    Stud_Grade = None
                else:
                    Stud_Grade = float(Stud_Grade)
    
                Status = input("Assessment Status (Pending/Passed/Failed): ")
                if Status not in ['Pending', 'Passed', 'Failed']:
                    print("Invalid status. Defaulting to 'Pending'.")
                Status = 'Pending'
    
                add_assessment(AssessmentName, AssessmentType, MaxGrade, DueDate, Subj_ID, Stud_ID, Stud_Grade, Status)

            elif assess_choice == '2':
                assess = view_assessment()
                print("\nAll Assessment Records:")
                for assessment in assess:
                    print(assessment)
            elif assess_choice == '3':
                Assess_name = input("\nEnter assessment name to search: ")
                assess = search_assessmentName(Assess_name)
                print(f"\n{assessment}")
            elif assess_choice == '4':
                Assess_ID = int(input("Enter Assessment ID to delete: "))
                delete_assessment(Assess_ID)
            elif assess_choice == '5':
                Assess_ID = int(input("Enter Assessment ID to edit: ")) 
                edit_assessment(Assess_ID)
            elif assess_choice == '6':
                continue
            else:
                print("\nInvalid choice, try again.")
                    
        elif choice == '5':
            print("\nGoodbye!\n")
            break
        
        else:
            print("\nInvalid choice, try again.")

if __name__ == "__main__":
    main()