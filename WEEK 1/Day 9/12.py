# create a function that returns both the area ad circumference of a circle given its radius

import math
def circle_stats(radius):
    area=math .pi * radius ** 2
    circumference=2*math.pi*radius
    return area,circumference
    print("hi")
a,c=circle_stats(3)
print("area:",a,"circumference:",c)
