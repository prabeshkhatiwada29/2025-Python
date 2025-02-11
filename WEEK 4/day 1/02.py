import json

x={
    "name":"John",
    "age":30,
    "city":"New York",
    "married":False,
    "divorced":False,
    

    "cars":[
    {"model":"BMW","year":2015},
    {"model":"Volvo","year":2012}

]
}

print(json.dumps(x))