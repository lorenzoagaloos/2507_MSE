# Week 5 - activity 2 | lorenzo.agaloos - 270729354
# Develop a Python program that demonstrates the usage of inheritance
# Create a base class called "Yoobee_Users" with attributes like "name", "address", "email", and "ID"

# Yoobee Users Parent Class
class Yoobee_Users:
    def __init__(self, name, address, email):
        self.name = name
        self.address = address
        self.email = email
    
   
    def greet(self):
        print("Greetings from Yoobee Colleges, I am Director " + self.name)

   
# student as Child Class inheriting from Yoobee_Users Parent Class
class student(Yoobee_Users):
    def __init__(self, name, address, email, user_id):
        super().__init__(name, address, email)
        self.user_id = user_id
    
    def greet(self):
        print("Welcome to Yoobee Colleges, " + self.name)

# teacher as Child Class inheriting from Yoobee_Users Parent Class
class teacher(Yoobee_Users):
    def __init__(self, name, address, email, employee_id):
        super().__init__(name, address, email)
        self.employee_id = employee_id
    
    def greet(self):
        print("Everyone, meet Professor " + self.name)

if __name__ == "__main__":
    # Create instances of student and teacher
    yoobee1 = Yoobee_Users("John Doe","001 Queen St", "jd@yoobee.com",)
    student1 = student("Alice Smith", "123 Main St", "as@yoobee.com", "S1001")
    teacher1 = teacher("Bob Johnson", "456 Elm St", "bj@yoobee.com", "T2001")

    yoobee1.greet()
    student1.greet()
    teacher1.greet()

   