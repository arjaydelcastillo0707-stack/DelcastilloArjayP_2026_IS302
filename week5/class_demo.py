# Define the class
class Person:
    # The __init__ method initializes the attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method to display the person's information
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

# Create an object (instance) of the Person class
p1 = Person("Juan", 20)

# Call the method to show the results
p1.display_info()