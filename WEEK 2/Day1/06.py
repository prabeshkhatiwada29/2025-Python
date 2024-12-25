# methods
# class> attributes> methods
# methods are function that belongd to objects


class Student:
    college_name="Sungava college"


    def __init__(self,name,marks):
        self.name=name
        self.marks=marks


    def welcome(self):
        print("Welcome student,",self.name)

    def get_marks(self):
        return self.marks
    

s1=Student("Prabesh",20)
s1.welcome()
print(s1.get_marks())


