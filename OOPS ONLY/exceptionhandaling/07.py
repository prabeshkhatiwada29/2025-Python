try:
    a=int(input("Enter an integer"))
    b=7/a
    print(b)
except Exception as e:
    print("This is a wrong input",e)
finally:
    print("This will be executed always")


# try
# except
# valueerror as e
# zeroDivision error as e
# exception as e
# finally
