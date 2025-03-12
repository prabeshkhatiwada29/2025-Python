# in capsulation we can restrict the access of the data members of the class
# we can restrict the access of the data members of the class


class Student:
    def __init__(self, name,grade,percentage):
        self.name=name
        self.grade=grade
        self.__percentage=percentage

    def get_percentage(self):
        return self.__percentage
    def student_details(self):
        print(f"{self.name}is in class ,{self.grade},with{self.percentage}")

student1=Student('prabesh','A+',90)
student2=Student('prabesh','A+',90)
# student1.student_details()
print(student1.get_percentage())
# student2.student_details()
