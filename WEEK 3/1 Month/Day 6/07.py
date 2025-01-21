# incapsulation


class Student:
    def __init__(self,name,grade,percentage):
        self.name=name
        self.grade=grade
        self.__percentage=percentage

    def get_percentage(self):
        return self.__percentage
    
    def student_details(self):
        print(f"{self.name} is in class{self.grade},with  {self.percentage}%")


student1=Student('madav',11,96)
# print(student1.percentage)
print(student1.get_percentage)