class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
    def perimeter(self):
        return 2 * (self.length + self.width)
    
rect1 = Rectangle(15, 5)

print("Area:", rect1.area())
print("Perimeter:", rect1.perimeter())

rect1 = Rectangle(18, 3)

print("Area:", rect1.area())
print("Perimeter:", rect1.perimeter())


rect1 = Rectangle(20, 5)

print("Area:", rect1.area())
print("Perimeter:", rect1.perimeter())

rect1 = Rectangle(100, 15)

print("Area:", rect1.area())
print("Perimeter:", rect1.perimeter())