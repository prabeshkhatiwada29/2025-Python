class Student:
    def __init__(self,full_name,Class_grade):
        self.full_name=full_name
        self.class_grade=Class_grade    
    def student_details(self):
        print(f"Student Name: {self.full_name}")

student1=Student("madhav",11)
student2=Student("Prabesh",12)
# print(student1.name, student1.grade)  
student1.student_details()  
student2.student_details()  