# Inheritance 
# allows one child  to reuse the property and methods of another class (parents)
# Parents
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def student_details(self):
        print(f"{self.name} is in class {self.age}th")

Student1=Student("PRABESH",12)
Student1.student_details()


# Child
class Teacher(Student):
    def __init__(self, name, age, subject):   # we are calling the parent class constructor
        super().__init__(name, age)          # calling parent class constructor
        self.subject = subject
    def teacher_details(self):
        super().student_details()
        # print(f"{self.name} is teaching {self.subject} in class {self.age}th")
        
Teacher1=Teacher("pratik",12,16)
print(Teacher1.subject)
    
Teacher1.teacher_details()