class Student:
    # make the init method
    def __init__(self, name, age):           #method
        self.name = name
        self.age = age
    def student_details(self):
        print(f"name:{self.name},age:{self.age}")                                                          #method


student1 = Student('prabesh',21)
# print(student1.name,student1.age)
student1.student_details()
print(student1.__dict__)


del student1.age
print(student1.__dict__)

del student1.name
print(student1.__dict__)