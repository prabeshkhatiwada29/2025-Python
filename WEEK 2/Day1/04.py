# constructor 
# All classes have a function called_init_(), which is always executed when the c;ass is being initiated.
class Student:

    def __init__(self,fullname):
        self.fullname = fullname
        print("adding new student in database")
        # instance method
s1= Student("prbesh")
print(s1.fullname)

s2=Student("pratik")
print(s2.fullname)
     
