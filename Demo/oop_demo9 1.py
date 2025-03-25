from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Attempting to instantiate the abstract class will raise an error
try:
    shape = Shape()
except TypeError as e:
    print(e)

# Instantiating the concrete classes works fine
circle = Circle(5)
print(f"Circle area: {circle.area()}")
print(f"Circle perimeter: {circle.perimeter()}")

rectangle = Rectangle(4, 6)
print(f"Rectangle area: {rectangle.area()}")
print(f"Rectangle perimeter: {rectangle.perimeter()}")