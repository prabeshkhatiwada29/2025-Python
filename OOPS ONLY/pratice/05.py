# Abstraction


class Student:
    def __init__(self, name,grade,percentage):
        self.name=name
        self.grade=grade
        self.percentage=percentage

    def student_details(self):
        print(f"{self.name}is in class ,{self.grade},with{self.percentage+2}%")

student1=Student('prabesh','A+',90)
student2=Student('prabesh','A+',90)

student1.student_details()
student2.student_details()
# print(student1.__dict__)
