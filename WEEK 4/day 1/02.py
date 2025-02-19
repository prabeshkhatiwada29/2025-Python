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
# Output: {"name": "John", "age": 30, "city": "New York", "married": false, "divorced": false, "cars": [{"model": "BMW", "year": 2015}, {"model": "Volvo", "year": 2012}]}
# Compare this snippet from WEEK%204/day%201/08.py: