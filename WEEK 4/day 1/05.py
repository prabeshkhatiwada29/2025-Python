
list = [1, 2, 3, 4, 5]

try:
    print(list[5])
except IndexError:
    print("Index out of range")
