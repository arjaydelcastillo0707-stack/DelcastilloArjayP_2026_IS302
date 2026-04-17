# Define the Student class
class Student:
    # Initialize the student attributes
    def __init__(self, name, student_id, course):
        self.name = name
        self.student_id = student_id
        self.course = course

    # Method to print student details
    def display_student(self):
        print("--- Student Record ---")
        print(f"Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Course: {self.course}")

# Instantiate the object with specific data
student1 = Student("Mj", "2023-001", "BSIS")

# Call the method to display the info
student1.display_student()