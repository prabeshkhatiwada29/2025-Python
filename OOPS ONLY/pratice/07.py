# inheritance in python
# Inheritance is a powerful feature in object oriented programming.
# parent class

class Student:
    def __init__(self,name,grade,percentage):
        self.name=name
        self.grade=grade
        self.percentage=percentage
    
    def student_details(self):
        print(f"{self.name} is in class {self.grade} with {self.percentage}%")
student = Student('prabesh','A+',90)
student1 = Student('prabesh','A+',90)


# child class
class Teacher(Student):
    def __init__(self,name,grade,percentage,subject):
        super().__init__(name,grade,percentage)
        self.subject=subject
    
    def teacher_details(self):
        super().student_details()
        print(f"{self.name} is teaching {self.subject} in class {self.grade}")
teacher = Teacher('prabesh','A+',90,'math')
teacher.teacher_details()    
teacher.student_details()
print(teacher.__dict__) 
print(student1.__dict__)                                   