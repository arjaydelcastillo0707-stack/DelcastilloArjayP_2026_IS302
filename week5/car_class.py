# Define the Car class
class Car:
    # Initialize the car attributes
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    # Method to display the car's full details in one line
    def display_car(self):
        print(f"Car Details: {self.brand} {self.model} ({self.year})")

# Create an instance of the Car class
car1 = Car("rusiiii", "promaxx", 2020)

# Call the method to display the information
car1.display_car()