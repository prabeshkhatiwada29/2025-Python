class Student:
    def __init__(self,name,age,grade,percentage,team):
        self.name=name
        self.age=age
        self.grade=grade
        self.perceentage=percentage
        self.team=team

    def student_details(self):
        print(f"Name: {self.name} is in class {self.grade},with{self.perceentage}%" )

team1="A"
team2="B"


student1=Student("prabesh",12,"Bachelor",99,team1)
student2=Student("prabesh",12,"Bachelor",99,team2)
# print(student1.team)
student1.student_details()