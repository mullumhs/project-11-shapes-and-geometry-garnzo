import math

class Shape:
    
    def area(self):
        pass

    def perimeter(self):
        pass

class Square(Shape):
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return (self.width + self.height) * 2
    
class Triangle(Shape):

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height
    
    def perimeter(self):
        return self.base + self.height + self.height
    