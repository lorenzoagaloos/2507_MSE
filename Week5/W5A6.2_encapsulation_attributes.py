# W5A6.2 - Encapsulation / Different Types of Attributes lorenzo.agaloos - 270729354
# Add a new method "updated info" in student class to increase mark to A+

class Student:
    def __init__(self, name, age):

        self.name = name # public
        self._age = age # protected​
        self.__grade = 'A' # private​

    # Getter for grade
    def get_grade(self):
        return self.__grade
    
    # Setter for grade
    #def set_grade(self, grade):
    #    if isinstance(grade, str) and len(grade) > 0:
    #        self.__grade = grade
    #    else:
    #        print("Invalid grade. It must be a non-empty string.")
    
    def updated_info(self):
        self.__grade = 'A++'
        return self.__grade



class new_Student(Student):
    def __init__(self, name, age, phone):
        super().__init__(name, age) # Inheriting parent attributes
        self._phone = phone # protected attribute

  
s = Student('Alicia', 25)
print(f"\nStudent Name: {s.name}")          # public attribute that is accessible​
print(f"Student Age: {s._age}")             # protected attribute that is accessible but discouraged 
print(f"Initial Grade: {s.get_grade()}")  # private attribute but correctly accessed
print(f"Final Grade: {s.updated_info()}\n")


ns = new_Student("James", 21, "02212123333")
print(f"\nStudent Name: {ns.name}")         # public attribute that is accessible​
print(f"Student Age: {ns._age}")            # protected attribute that is accessible but discouraged 
print(f"Contact No.: {ns._phone}")          # protected attribute that is accessible but discouraged
print(f"Initial Grade: {ns.get_grade()}")  # private attribute but correctly accessed
print(f"Final Grade: {ns.updated_info()}\n")
