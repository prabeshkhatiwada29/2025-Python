class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(abc):
        print("Hello, my name is " + abc.name)

p1=Person("prabesh",26)
p1.myfunc()  # Output: Hello, my name is prabesh