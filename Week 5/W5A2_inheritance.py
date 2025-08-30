# Week 5 - activity 2 | lorenzo.agaloos - 270729354
# Develop a Python program that demonstrates the usage of inheritance
# Create a base class called "Yoobee_Users" with attributes like "name", "address", "email", and "ID"

# Yoobee Users Parent Class
class Yoobee_Users:
    def __init__(self, name, address, email):
        self.name = name
        self.address = address
        self.email = email

   
# student as Child Class inheriting from Yoobee_Users Parent Class
class student(Yoobee_Users):
    def __init__(self, name, address, email, user_id):
        super().__init__(name, address, email)
        self.user_id = user_id

# teacher as Child Class inheriting from Yoobee_Users Parent Class
class teacher(Yoobee_Users):
    def __init__(self, name, address, email, employee_id):
        super().__init__(name, address, email)
        self.employee_id = employee_id

if __name__ == "__main__":
    # Create instances of student and teacher
    student1 = student("Alice Smith", "123 Main St", "as@yoobee.com", "S1001")
    teacher1 = teacher("Bob Johnson", "456 Elm St", "bj@yoobee.com", "T2001")

    # Print details of the student
    print("Student Details:")
    print(f"Name: {student1.name}")
    print(f"Address: {student1.address}")
    print(f"Email: {student1.email}")
    print(f"user ID: {student1.user_id}")

    # Print details of the teacher
    print("\nTeacher Details:")
    print(f"Name: {teacher1.name}")
    print(f"Address: {teacher1.address}")
    print(f"Email: {teacher1.email}")
    print(f"Employee ID: {teacher1.employee_id}")



