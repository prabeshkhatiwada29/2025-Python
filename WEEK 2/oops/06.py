# abstraction : Hidden the  implemantation


class Student:
    def __init__(self, name, age, grade,percentage):
        self.name = name
        self.age=age
        self.grade=grade
        self.percentage=percentage
    def Student_details(self):
        print(f"{self.name} is in class {self.grade} and is {self.age} years old {self.percentage+2}%")


Student1=Student('madhav',12,"bachelor",97)
Stundent2=Student("prabesh",23,"plus2",98)

Student1.Student_details()
Stundent2.Student_details()