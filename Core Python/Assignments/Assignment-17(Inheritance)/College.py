class College:
    # Parameterized Constructor for number of students
    def __init__(self, num_students=0):
        self.num_students = num_students
        self.students = []

    # Add Student
    def addStudent(self, student):
        if len(self.students) < self.num_students:
            self.students.append(student)
            print(f"Student '{student.Name}' added successfully!")
        else:
            print("Cannot add more students — limit reached.")

    # Get Student
    def getStudent(self, sid):
        for s in self.students:
            if s.StudentId == sid:
                return s
        print("Student not found.")
        return None

    # Remove Student
    def removeStudent(self, sid):
        for s in self.students:
            if s.StudentId == sid:
                self.students.remove(s)
                print(f"Student '{s.Name}' removed successfully!")
                return
        print("Student not found.")

    # Override __str__
    def __str__(self):
        if not self.students:
            return "No students in the college."
        return "\n".join(str(s) for s in self.students)