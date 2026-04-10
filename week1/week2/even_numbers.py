 # Task: Print all even numbers from 1 to 50

print("--- Even Numbers (1-50) ---")

# We loop from 1 to 51 so that the number 50 is included
for i in range(1, 51):
    # The % (modulo) operator finds the remainder of a division.
    # If a number divided by 2 has a remainder of 0, it is even.
    if i % 2 == 0:
        print(i, end=" ")  # 'end=" "' keeps the numbers on one line for better readability

print("\n" + "-"*27)