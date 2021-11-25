class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


block_1 = Rectangle(12, 5)
assert block_1.area() == 60
assert block_1.perimeter() == 34
