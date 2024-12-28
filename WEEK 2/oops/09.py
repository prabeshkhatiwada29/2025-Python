# # polymorphism
# # allows methods in diffterent classes to have same name but different bahaviour depending on objects


# class Student:
#     def __init__(self, name, age,percentage):
#         self.name = name
#         self.age = age
#         self.percentage = percentage

#     def Student_details(self):
#         print(f"Name: {self.name},Age:{self.age},percentage:{self.percentage}")



# class GraduateStudent(student):
#     def __init__(self, name, age, percentage, degree):
#         super().__init__(name, age, percentage)
#         self.degree = degree
#         def Student_details(self):
#             print(f"Name: {self.name},Age:{self.age},percentage:{self.percentage}")
# # object-student

# student1=Student("prabesh",12,13)

# # graduation
# gradu_01=Student("pratik",12,13)

# gradu_01.Student_details()
# student1.Student_details()

