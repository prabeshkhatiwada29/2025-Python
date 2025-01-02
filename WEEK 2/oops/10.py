class Car:
    def __init__(self,userbrand,usermodel,userage):
        self.brand=userbrand
        self.model=usermodel
        self.age=userage
class ElectricCar(Car):
        def __init__(self,brand,model, battery_size):
             super().__init__(brand,model)
             self.mattery_size=battery_size

my_tesla=ElectricCar("tesla","model s","87kwh")
print(my_tesla.model)

# my_car=Car("prabesh","khatiwada",98)
# print(my_car.brand)
# print(my_car.model)
# print(my_car.age)


# my_new_car=Car("tata","safari")
# print(my_new_car.model)


