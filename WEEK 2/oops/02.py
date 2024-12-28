class Student:
    def __init__(self,name,grade,percentage):
        self.name=name
        self.grade=grade
        self.percnetage=percentage

    def student_details(self):
        print(f"{self.name} is in class{self.grade},with {self.percnetage}%")


Student1=Student('prabesh',11,96)
Student2=Student('pratik',11,99)

        
Student1.student_details()
Student2.student_details()
print(Student1.__dict__)