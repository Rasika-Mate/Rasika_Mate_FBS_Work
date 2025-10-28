from Student import Student

class MedicalStudent(Student):
    # Parameterized Constructor
    def __init__(self, sid=0, name="", age=0, percentage=0.0, specialization="", marks_of_internship=0.0):
        super().__init__(sid, name, age, percentage)
        self.Specialization = specialization
        self.MarksOfInternship = marks_of_internship

    # Accept method
    def accept(self):
        print("\nEnter Medical Student Details:")
        super().accept()
        self.Specialization = input("Enter Specialization: ")
        self.MarksOfInternship = float(input("Enter Marks of Internship: "))

    # Display method
    def display(self):
        print("\nMedical Student Details:")
        super().display()
        print("Specialization:", self.Specialization)
        print("Marks of Internship:", self.MarksOfInternship)
        print("Final Rank:", self.calculateRank())

    # Calculate Rank (Override)
    def calculateRank(self):
        total = (self.Percentage + self.MarksOfInternship) / 2
        if total >= 85:
            return "Outstanding"
        elif total >= 70:
            return "Very Good"
        elif total >= 55:
            return "Good"
        elif total >= 40:
            return "Average"
        else:
            return "Poor"

    # Override __str__
    def __str__(self):
        return (super().__str__() +
                f", Specialization:{self.Specialization}, Internship Marks:{self.MarksOfInternship}, Final Rank:{self.calculateRank()}")