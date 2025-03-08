arr=[1,2,3,4,5,6,7]

# print(min(arr))
# print(arr.sort())

arr.sort()
print(arr)
arr.sort(reverse=True)
print(arr)

arr.append(9)
print(arr)
arr.remove(9)
print(arr)