# pattern


def lines():
    line=int(input("Enter a number of lines="))
    for i in range(1,line+1):
        for j in range(i):
            print("x",end="")
            print()
        
        return f"The{line} number of trangle has been created"
    
    triangle=lines()
    print(triangle)
