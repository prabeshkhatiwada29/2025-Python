# inheritance
class Car:
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")

class Toyotacar(Car):
    def __init__(self,name):
        self.name=name

car1=Toyotacar("honda")
car2=Toyotacar("prius")

print(car1.start())