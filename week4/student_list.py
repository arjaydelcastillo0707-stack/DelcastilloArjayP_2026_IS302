# 1. Create an empty list called students
students = []

# 2. & 3. Ask the user for 5 names and store them in the list
for i in range(5):
    name = input(f"Enter name for student {i+1}: ")
    students.append(name)

# 4. Display all students
print("\nStudent List:")
for student in students:
    print(student)