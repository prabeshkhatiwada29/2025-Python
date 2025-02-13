# inheritances
# Inheritance allows us to define a class that inherits all the methods and properties from another class.
class Person:
    def __init__(self, name, age,percentage):

        self.name = name
        self.age = age
        self.percentage=percentage

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Percentage:", self.percentage)


class Student(Person):
    def __init__(self, name, age, percentage,roll):
        super().__init__(name, age,percentage,roll)              #super() is used to call the parent class constructor
        self.percentage = percentage
        self.roll = roll

    def display(self):
        super().display()
        print("Percentage:", self.percentage)
        print("Roll:", self.roll)

Student1 = Student("John", 36, 12,13)
Student1.display()
