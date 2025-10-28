# Write a program to
# 1. create a package “SY” which has class SYMARKS (Computer Total, MathsTotal, ElectronicsTotal).
# 2. Create another package “TY” which has a class TYMarks (Theory, Practical).
# 3. Create object of student class (Outside SY & TY package) having roll number, name, SYMakrs and TYMarks. Add the marksof SY and TY Computer subjects and calculate grade ("A" for >=70, "B" for >=60, "C" for >=50, “Pass Class” for >=40 else “Fail”) and display the result of the student in proper format.

from SY.SYMarks import SYMarks
from TY.TYMarks import TYMarks

class Student:
    def __init__(self, roll_no, name, sy_marks, ty_marks):
        self.roll_no = roll_no
        self.name = name
        self.sy_marks = sy_marks
        self.ty_marks = ty_marks

    def calculate_grade(self):
        total = self.sy_marks.comp_total + self.ty_marks.theory + self.ty_marks.practical
        avg = total / 3

        if avg >= 70:
            grade = "A"
        elif avg >= 60:
            grade = "B"
        elif avg >= 50:
            grade = "C"
        elif avg >= 40:
            grade = "Pass Class"
        else:
            grade = "Fail"

        return total, avg, grade

    def display(self):
        total, avg, grade = self.calculate_grade()
        print("\n----- Student Result -----")
        print(f"Roll No      : {self.roll_no}")
        print(f"Name         : {self.name}")
        print(f"SY Computer  : {self.sy_marks.comp_total}")
        print(f"TY Theory    : {self.ty_marks.theory}")
        print(f"TY Practical : {self.ty_marks.practical}")
        print(f"Total Marks  : {total}")
        print(f"Average      : {avg:.2f}")
        print(f"Grade        : {grade}")

if __name__ == "__main__":
    sy = SYMarks(comp_total=65, maths_total=70, electronics_total=68)
    ty = TYMarks(theory=75, practical=80)

    s1 = Student(roll_no=101, name="Rasika Mate", sy_marks=sy, ty_marks=ty)
    s1.display()