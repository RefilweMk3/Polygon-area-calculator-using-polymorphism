class Polygon:
    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height

class Rectangle(Polygon):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

class Square(Polygon):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side * self.side

class Pentagon(Polygon):
    def __init__(self, side, apothem):
        self.side = side
        self.apothem = apothem
    
    def area(self):
        perimeter = 5 * self.side
        return 0.5 * perimeter * self.apothem

class Hexagon(Polygon):
    def __init__(self, side):
        self.side = side

    def area(self):
        return (3 * (3**0.5) / 2) * self.side ** 2

def print_area(polygon):
    print(f"Area of {polygon.__class__.__name__}: {polygon.area()}")

triangle = Triangle(10, 5)
rectangle = Rectangle(10, 5)
square = Square(4)
pentagon = Pentagon(6, 4)
hexagon = Hexagon(6)

print_area(triangle) 
print_area(rectangle)
print_area(square)
print_area(pentagon)
print_area(hexagon)