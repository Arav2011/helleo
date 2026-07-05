import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


# Ta in radien från användaren
radius = float(input("Enter the radius: "))

# Skapa ett Circle-objekt
circle = Circle(radius)

# Skriv ut area och omkrets
print("Area:", circle.area())
print("Perimeter:", circle.perimeter())