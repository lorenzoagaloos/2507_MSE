# Week 3 Activity 5 - (lorenzoagaloos-270729354)
# Re-using and updating the given code to add a new table "Students" with three columns: Stu_ID, Stu_name, and Stu_address
# Insert two sample records into Students, then display all rows from both the Users and Students tables

from database import create_table
from student_manager import add_student, view_student, search_student, delete_student, add_user, view_users, search_user, delete_user

def menu():
    print("\n==== Yoobee Records Manager ====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student Record by Name")
    print("4. Delete Student Record by ID")
    print("5. Add User")
    print("6. View All Users")
    print("7. Search User by Name")
    print("8. Delete User by ID")
    print("9. View all Records")
    print("10. Exit")

def main():
    create_table()
    while True:
        menu()
        choice = input("\nSelect an option (1-10): ")
        if choice == '1':
            Stu_name = input("Enter name: ")
            Stu_address = input("Enter address: ")
            add_student(Stu_name, Stu_address)
        
        elif choice == '2':
            students = view_student()
            print("\nAll Student Records:")
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
            name = input("Enter name: ")
            email = input("Enter email: ")
            add_user(name, email)
        
        elif choice == '6':
            users = view_users()
            print("\nAll User Records:")
            for user in users:
                print(user)
        
        elif choice == '7':
            name = input("Enter name to search: ")
            users = search_user(name)
            for user in users:
                print(f"\n{user}")
        
        elif choice == '8':
            user_id = int(input("Enter user ID to delete: "))
            delete_user(user_id)
        
        elif choice == '9':
            students = view_student()
            print("\nAll Student Records:")
            for student in students:
                print(student)
            users = view_users()
            print("\nAll User Records:\n")
            for user in users:
                print(user)
        
        elif choice == '10':
            print("\nGoodbye!\n")
            break
        else:
            print("\nInvalid choice, try again.")

if __name__ == "__main__":
    main()