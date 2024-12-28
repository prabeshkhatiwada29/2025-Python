# Encapsulation
# restrict access to certain attributes or method to protect data and enforce controlled access

class Student:
    def __init__(self, name, grade, percentage):
        self.name=name
        self.__grade=grade
        self.__percentage=percentage  #double underscore limirs acess
    def get_percentage(self):
        return self.__percentage
    
    def student_details(self):
        print(f"{self.name} is om class{self.grade},with{self.__percentage}%")

Student1=Student("prabesh",11,12)


print(Student1.get_percentage)