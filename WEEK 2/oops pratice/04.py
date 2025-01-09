class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def move(self):
        print("drive")
class Boat:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("float")
class PLANE:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def move(self):
        print("fly")

car1=Car("ford","mustang")
Boat1=Boat("ixa","praneah")
plane1=PLANE("prabesh","12")

for x in (car1, Boat1,plane1):
    x.move()