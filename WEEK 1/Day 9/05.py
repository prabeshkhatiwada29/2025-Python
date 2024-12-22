# odd even

def odd_even():
    num=int(input("Enter number to check="))
    if num%2==0:
            print("Number is even")
    else:
          print("Number is odd")
          return num
    

user=odd_even()
print(user)