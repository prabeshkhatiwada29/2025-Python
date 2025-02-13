class Student:
    def __init__(self, name, age,percentage):
        self.name = name
        self.age = age
        # self._percentage=percentage
        self.percentage=percentage


    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Percentage:", self.percentage)

Student1 = Student("John", 36, 90)
Student1.display()
    