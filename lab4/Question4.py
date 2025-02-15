# 4. Create a function that returns both the area and circumference of a circle given its radius.
 
from math import pi
def circle(r):
    return pi*r**2,2*pi*r

r=int(input("enter the radius of cirlce: "))
list=circle(r)
print(f"the area of circle is{round(list[0],2)} and circumference of circle is {round(list[1],2)} ")