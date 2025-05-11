# convert list to tuple

a=[1,2,3,4,5,6,7,8,9]
t=tuple(a)
print(t)


t=('gfg', 'is', 'best', 'for', 'geeks')
n=10
for i in range(int (n)):
    t=(t,)
print(t)