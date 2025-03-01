# exception handaling is the process of responding to the occurrence of exceptions – anomalous or exceptional conditions requiring special processing – during the execution of a program.
# 
# 
a=input("Enter a number:")
print(f"Multiply the table of{a}is")
try:

   for i in range(1,11):
      print(f"{int(a)} x {i}={int(a)*i}")
except Exception as e:
      print(f"Error:{e}")

print("End of the program")