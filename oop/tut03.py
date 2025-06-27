import math 
## Polymorphism with functions and methods
# base class
class Shape:
    def area(self):
        return "The area of the figure"

# derived class 1
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.width*self.length
    
#derived class 2
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return (self.radius**2)*math.pi
    
## Function that demonstrates polymorphism
def print_area(shape):
    print(f"Area of the figure is: {shape.area()}")

rectangle = Rectangle(4,5)
circle = Circle(3)

print_area(rectangle)
print_area(circle)

