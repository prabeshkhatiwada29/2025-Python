# from array import*
# a=arr.array('d',[1.1,2.1,3.1])
# len(a)

import array as arr
a=arr.array('d',[1.1,2.1,3.1])
a.append(3.4)
print("Array a=",a)
b=arr.array("d",[2,1,3.1,4.6])
b.extend([4.5,2.4,6.7])
print("Array b=",b)  # extend() function is used to add multiple elements to th