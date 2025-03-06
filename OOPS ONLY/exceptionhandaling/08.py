# class Car:
#     brand="BMW"
#     model="X1"

# my_car=Car()
# print(my_car.brand)


class Car:

    total_car=0

    def __init__(self,userbrand,usermodel):
        self.__brand=userbrand
        self.model=usermodel
        Car.total_car+=1    # class variable    
        

    def get_brand(self):
        return self.__brand + "!"
    
    def full_name(self):


        return f"{self.__brand} {self.model}"
    
    def Fuel_type(self):
        return "Petrol"
    
    
    @staticmethod               # static method is the decorator mainly used in Many framework
    def general_info():
        return "This is a car"
    
    

class ElectircCar(Car):
    def __init__(self, userbrand, usermodel,battery_size):
        super().__init__(userbrand, usermodel)          # super() is used to call the parent class constructor
        self.battery_size=battery_size
    
    def Fuel_type(self):
        return "eLECTRIC cHARGE"


my_tesla=ElectircCar("Tesla","Model S",75)
# print(isinstance(my_tesla,Car))
# print(isinstance(my_tesla,ElectircCar))
# print(my_tesla.full_name())
# print(my_tesla.get_brand())
# print(my_tesla.Fuel_type())

# safari=Car("Tata","Safari")


# # print(safari.Fuel_type())
# # print(Car.total_car)
# # print(safari.general_info())
# print(Car.general_info())


class Battery:
    # def __init__(self,battery_size=75):
    #     self.battery_size=battery_size
    
    # def describe_battery(self):
    #     return f"This car has a {self.battery_size}-kWh battery."
    
    # def get_range(self):
    #     if self.battery_size==75:
    #         range=260
    #     elif self.battery_size==100:
    #         range=315
    #     return f"This car can go about {range} miles on a full charge."



    def battery_info(self):
        return "This is a battery info"
    



class engine:
    def engine_info(self):
        return "This is a engine info"
class ElectricCar2(Battery,Car,engine):
    pass

my_new_car=ElectricCar2("Tesla","Model S")
print(my_new_car.engine_info())
print(my_new_car.battery_info())
# print(my_new_car.get_brand(
# print(my_new_car.Fuel_type())
  

    


# new_car=Car("BMW","X1")
# print(new_car.brand)
# print(new_car.model) 
# print(new_car.full_name()) # BMW X1

# new_car=Car("Audi","Q7")
# print(new_car.brand)
# print(new_car.model)  # Audi Q7


# new_car=Car("Mercedes","GLA")
# print(new_car.brand)
# print(new_car.model)  # Mercedes GLA
        