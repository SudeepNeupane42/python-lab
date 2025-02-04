from math import pi


class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def area(self, length, width):
        print("Area of rectangle is: ",length*width)

class Circle(Shape):
    def area(self,r):
        print("area of circle is: ",pi*r*r)


s=Shape()
s.area()
r=Rectangle()
r.area(5,2)
c=Circle()
c.area(7)