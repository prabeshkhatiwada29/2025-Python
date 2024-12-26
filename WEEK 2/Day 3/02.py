# multilevel inheritance

class Car:
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")

class Toyotacar(Car):
    def __init__(self,brand):
        self.brand=brand

class Fortuner(Toyotacar):
        def _init__(self,type):
            self.type=type

car1=Fortuner("petrol")
car1.start()



