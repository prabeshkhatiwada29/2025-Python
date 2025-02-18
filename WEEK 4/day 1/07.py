class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def showDetails(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print()
class Programmer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language
    def showDetails(self):
        super().showDetails()
        print(f"Language: {self.language}")
        print()



e= Employee("John", 50000)
e.showDetails()
p= Programmer("Doe", 60000, "Python")
p.showDetails()

