# there are two types of oops in python  which aare procedural and oops


# class: class is a blue print of template for creating objects

# object: object is an instance of class
class student:
    def __init__(self,Name,grade,percentage):
        self.name=Name
        self.grade=grade
        self.percentage=percentage
    def student_details(self):
        # print(f"Name: {self.name} , Grade: {self.grade}")
        print(f"{self.name}is in class{self.grade}and her {self.percentage}% in bachelor also")


student1 =student("prabesh",12,13)
# print(student1.grade,student1.name)

student1.student_details()
# print(student.__dict__)