class Dog:
    # Klassvariabel
    animal = "Dog"

    # Konstruktor
    def __init__(self, breed, colour):
        self.breed = breed
        self.colour = colour

    # Metod för att visa information
    def display(self):
        print("Animal:", Dog.animal)
        print("Breed:", self.breed)
        print("Colour:", self.colour)
        print()


# Skapa två objekt
dog1 = Dog("German Shepherd", "Black and Tan")
dog2 = Dog("Labrador", "Golden")

# Visa information
dog1.display()
dog2.display()