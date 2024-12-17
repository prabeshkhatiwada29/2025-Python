info={'name':'prabesh','age':12,'eligible':True}
print(info)
print(info['name'])
print(info['age'])
print(info.keys())
print(info.values())


for key in info.keys():
    print(f"The value correspomding to the key{key}is {info[key]}")