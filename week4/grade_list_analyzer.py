# 1. Create an empty list to store grades
grades = []

# 2. Ask the user to enter 5 grades
for i in range(5):
    # We use float() in case the user enters grades with decimals (e.g., 85.5)
    grade = float(input(f"Enter grade {i+1}: "))
    grades.append(grade)

# 3. Compute the analysis
# sum() adds all numbers in the list; len() counts how many items are in the list
average = sum(grades) / len(grades)
highest = max(grades)
lowest = min(grades)

# 4. Display the results
print("\n--- Grade Analysis ---")
print(f"Average Grade: {average:.1f}")
print(f"Highest Grade: {highest}")
print(f"Lowest Grade: {lowest}")