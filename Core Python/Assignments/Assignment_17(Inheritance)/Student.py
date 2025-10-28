class Student:
    # Parameterized Constructor
    def __init__(self, sid=0, name="", age=0, percentage=0.0):
        self.StudentId = sid
        self.Name = name
        self.Age = age
        self.Percentage = percentage

    # Accept method
    def accept(self):
        print("\nEnter Student Details:")
        self.StudentId = int(input("Enter Student ID: "))
        self.Name = input("Enter Name: ")
        self.Age = int(input("Enter Age: "))
        self.Percentage = float(input("Enter Percentage: "))

    # Display method
    def display(self):
        print("\nStudent Details:")
        print("Student ID:", self.StudentId)
        print("Name:", self.Name)
        print("Age:", self.Age)
        print("Percentage:", self.Percentage)
        print("Rank:", self.calculateRank())

    # Calculate Rank
    def calculateRank(self):
        if self.Percentage >= 75:
            return "Distinction"
        elif self.Percentage >= 60:
            return "First Class"
        elif self.Percentage >= 50:
            return "Second Class"
        elif self.Percentage >= 35:
            return "Pass"
        else:
            return "Fail"

    # Override __str__
    def __str__(self):
        return f"Student(ID:{self.StudentId}, Name:{self.Name}, Age:{self.Age}, Percentage:{self.Percentage}, Rank:{self.calculateRank()})"
