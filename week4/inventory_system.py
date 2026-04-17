# Create a dictionary that stores products and prices
inventory = {
    "Laptop": 45000,
    "Mouse": 500,
    "Keyboard": 1200
}

# Display the product list
print("--- Product Inventory ---")
for item, price in inventory.items():
    # Using an f-string to format the price for better readability
    print(f"{item}: {price}")