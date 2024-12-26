# multiple inheritance

class A:
    VarA="welcome to class A"

class B:
    VarB="welcome to class B"

class c(A,B):
    varc="welcome to  class C"

c1=c()
print(c1.varc)
print(c1.VarA)
print(c1.VarB)