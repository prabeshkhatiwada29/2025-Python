# create a function both area and circumference of the circle in radius
import math
def circle_properties(radius):
    are= math.pi * radius ** 2
    cir= 2 * math.pi * radius
    return are, cir

print(circle_properties(2))
    
