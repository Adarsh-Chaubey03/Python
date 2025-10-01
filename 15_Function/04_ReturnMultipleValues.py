# Create a function that returns both area and circumference of a circle for the given radius.
import math

def circle(r):
    area = math.pi * r ** 2
    peri = math.pi * r * 2
    return area,peri

a,c = circle(8)
print("Area: ",a,"Perimeter: ",c)
