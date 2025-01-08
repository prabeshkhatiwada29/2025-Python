# polymorphism
#  over loading and over writein




class prabesh:
    def displayinfo(self,name=''):
        print(f"Name is {name}")
class iip(prabesh):
    def  displayinfo(self):
        super().displayinfo()
        print("I am IIP")


obj=iip()
obj.displayinfo()  #overloading


