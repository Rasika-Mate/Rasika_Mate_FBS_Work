from EnggStudent import EnggStudent
from MedicalStudent import MedicalStudent
from Student import Student
from College import College

# Create a College with capacity for 3 students
c = College(3)

# Create student objects
s1 = EnggStudent(101, "Riya", 21, 78.5, "Computer", 80)
s2 = MedicalStudent(202, "Amit", 23, 88.0, "Cardiology", 90)
s3 = Student(303, "Sneha", 20, 65)

# Add to college
c.addStudent(s1)
c.addStudent(s2)
c.addStudent(s3)

# Display all students
print("\n--- College Students ---")
print(c)

# Access and display individual details
print("\n--- Display Individual Details ---")
s1.display()
s2.display()

# Remove one student
print("\n--- Removing Student (ID 202) ---")
c.removeStudent(202)

# Show updated list
print("\n--- After Removal ---")
print(c)
