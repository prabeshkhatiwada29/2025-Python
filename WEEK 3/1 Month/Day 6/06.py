# abstraction

class Student:
    def __init__(self,name,grade,percentage):
        self.name=name
        self.grade=grade
        self.percentage=percentage
    def student_details(self):
        print(f"{self.name} is in class{self.grade},with  {self.percentage}%")


student1=Student('madav',11,96)
student1.student_details()
