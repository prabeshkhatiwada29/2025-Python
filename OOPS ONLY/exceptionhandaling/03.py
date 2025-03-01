a=5
b=0

k= int(input("Enter a number:"))
print(f"the number is {k}")

try:
    print(a/b)
except Exception as e:
    print("hey, you can't divide a number by zero")

finally:
    print("this is the finally block")