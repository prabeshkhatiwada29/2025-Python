try:
    a=int(input("Enter a number:"))
    b=7/a
    print(b)
except Exception as e:
    print("hey, you can't divide a number by zero")
finally:
    print("this is the finally block")