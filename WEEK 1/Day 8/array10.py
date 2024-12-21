import array as arr
a=arr.array("d",[1.1,2.1,3.6,1.1])

print("popping last element",a.pop())
print("popping first element",a.pop())
a.remove(1.1)
print(a)  # prints array('d', [2.1, 3.6])