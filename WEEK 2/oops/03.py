class Stduent:
    def __init__(self, name, age, grade,percentage):
        self.name = name
        self.age = age
        self.grade = grade
        self.percentage=percentage
    def student(self):
        print(f"{self.name} is in class{self.grade},with {self.percnetage}%")

Student1=Stduent("prabseh",19,"bachelor",99)
# Student1.student()  # Output: prabseh is in classbachelor

print(Student1.percentage)
Student1.percentage=100

print(Student1.percentage)  # Output: 100


# delete object property

print(Student1.__dict__)
del Student1.percentage
print(Student1.__dict__)


# delete object
del Student1
print(Student1)