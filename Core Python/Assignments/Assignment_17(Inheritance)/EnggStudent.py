from Student import Student

class EnggStudent(Student):
    # Parameterized Constructor
    def __init__(self, sid=0, name="", age=0, percentage=0.0, branch="", internal_marks=0.0):
        super().__init__(sid, name, age, percentage)
        self.Branch = branch
        self.InternalMarks = internal_marks

    # Accept method
    def accept(self):
        print("\nEnter Engineering Student Details:")
        super().accept()
        self.Branch = input("Enter Branch: ")
        self.InternalMarks = float(input("Enter Internal Marks: "))

    # Display method
    def display(self):
        print("\nEngineering Student Details:")
        super().display()
        print("Branch:", self.Branch)
        print("Internal Marks:", self.InternalMarks)
        print("Final Rank:", self.calculateRank())

    # Calculate Rank (Override)
    def calculateRank(self):
        total = (self.Percentage + self.InternalMarks) / 2
        if total >= 80:
            return "Outstanding"
        elif total >= 70:
            return "Excellent"
        elif total >= 60:
            return "Good"
        elif total >= 50:
            return "Average"
        else:
            return "Poor"

    # Override __str__
    def __str__(self):
        return (super().__str__() +
                f", Branch:{self.Branch}, Internal Marks:{self.InternalMarks}, Final Rank:{self.calculateRank()}")
