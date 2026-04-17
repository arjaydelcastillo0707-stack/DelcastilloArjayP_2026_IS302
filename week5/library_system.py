# Define the Book class
class Book:
    # Initialize the book attributes
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    # Method to display the book's details
    def display_book(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year: {self.year}")
        print("-" * 20)  # Visual separator for readability

# 1. Create three book objects
book1 = Book("Python Programming", "John Smith", 2022)
book2 = Book("Data Science Basics", "Jane Doe", 2021)
book3 = Book("Web Development", "Alan Turing", 2023)

# 2. Display the book information
print("--- Library Inventory ---\n")
book1.display_book()
book2.display_book()
book3.display_book()