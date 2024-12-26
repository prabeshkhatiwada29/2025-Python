# del keyword
# used to delete object properties or object itself

class Student:
    def __init__(self, name):
       self.name=name
    
s1=Student("prabesh")

del s1.name
print(s1)