# Week 2 Activity 6 - Develop a basic HR project using OO (lorenzoagaloos-270729354)

# Develop a simple program for the Human Resources (HR) department to store and display basic employee information, including each employee’s name, salary, and job title
# Create at least two Employee objects with different data.
# Call the display_info() method to show each employee’s details
# Call the give_raise() method to increase an employee’s salary and display the updated amount

class Employee:
    def __init__(self, name, salary, job_title):
        self.name = name
        self.salary = salary
        self.job_title = job_title

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: ${self.salary:.2f}")
        print(f"Job Title: {self.job_title}\n")

    def give_raise(self, amount):
        old_salary = self.salary # Store the old salary to calculate the percentage increase
        self.salary *= amount
        actual_increase = (self.salary - old_salary) / old_salary * 100 # Calculate the percentage increase
        print(f"{self.name}'s new salary after a "f"{actual_increase:.2f}% raise is: ${self.salary:.2f}")

def main():

    # Create Employee objects
    employee1 = Employee("Paul Barron", 160000, "Data Architect")
    employee2 = Employee("Jake Claver", 175000, "Data Engineer")
    
    # Display employee information
    print("Employee 1 Information:")
    employee1.display_info()

    print("Employee 2 Information:")
    employee2.display_info()

    # Give a raise to each employee
    employee1.give_raise(1.10) # 10% raise
    employee2.give_raise(1.15) # 15% raise

    # Display updated information
    print("\nUpdated Employee 1 Information:")
    employee1.display_info()
    print("Updated Employee 2 Information:")
    employee2.display_info()

if __name__ == "__main__":
    main()
    
# Week 2 Activity 6 - Develop a basic HR project using OO (lorenzoagaloos-270729354)

        