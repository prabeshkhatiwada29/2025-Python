

def calculate_fact(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
        print(fact)
calculate_fact(6)