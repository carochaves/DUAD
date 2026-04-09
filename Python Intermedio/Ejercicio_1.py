class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.1416 * self.radius ** 2

    def __repr__(self):
        return f"Circle(radius={self.radius})"

circle1 = Circle(5)
circle2 = Circle(7)
circle3 = Circle(10)

area1 = circle1.area()
area2 = circle2.area()
area3 = circle3.area()

print("El área del círculo 1 con radio", circle1.radius, "es:", area1)
print("El área del círculo 2 con radio", circle2.radius, "es:", area2)
print("El área del círculo 3 con radio", circle3.radius, "es:", area3)