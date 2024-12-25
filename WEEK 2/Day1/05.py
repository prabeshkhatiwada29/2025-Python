# class and instance attributes
# class.attr
# instance.attr


class Student:
    college_name="Sungava college"

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        print("Adding new student in database..")
s1=Student("Karan",77)
print(s1.name)