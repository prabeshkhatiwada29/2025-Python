def shown(n):
    if(n==0):
        return 0
    
    print(n)
    shown(n-1)
    print("end")
shown(3)