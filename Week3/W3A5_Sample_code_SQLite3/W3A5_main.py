# Week 3 Activity 5 - (lorenzoagaloos-270729354)
# Re-using and updating the given code to add a new table "Students" with three columns: Stu_ID, Stu_name, and Stu_address
# Insert two sample records into Students, then display all rows from both the Users and Students tables

from database import create_table
from student_manager import add_student, view_student, search_student, delete_student

def menu():
    print("\n==== Student Records Manager ====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student Record by Name")
    print("4. Delete Student Record by ID")
    print("5. Exit")

def main():
    create_table()
    while True:
        menu()
        choice = input("\nSelect an option (1-5): ")
        if choice == '1':
            Stu_name = input("Enter name: ")
            Stu_address = input("Enter address: ")
            add_student(Stu_name, Stu_address)
        elif choice == '2':
            students = view_student()
            for student in students:
                print(student)
        elif choice == '3':
            Stu_name = input("\nEnter name to search: ")
            students = search_student(Stu_name)
            for student in students:
                print(f"\n{student}")
        elif choice == '4':
            Stu_ID = int(input("Enter user ID to delete: "))
            delete_student(Stu_ID)
        elif choice == '5':
            print("\nGoodbye!\n")
            break
        else:
            print("\nInvalid choice, try again.")

if __name__ == "__main__":
    main()