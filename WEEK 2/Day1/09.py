# abstraction

# hidding the implematation details of class and only showing the essential feature to the user

#  Encapsulation

# Wrapping data and function into a single unit(object)

# class car:
#     def __init__(self, brand, model, year):
#         self.brand = "bmw"
#         self.model = 99
#         self.year = 2020
#         self.speed = 0
#     def start(self):
#      self.brand=True
#      self.year=2020
#      print("car started")


# car1=car()
# car1.start()  # car started


class Car:
    def __init__(self):
        self.acc=False
        self.speed=0
        self.clutch=False

    def start(self):
        self.clutch=True
        self.acc=True
        print("car started")
car1=Car()
car1.start()  # car started