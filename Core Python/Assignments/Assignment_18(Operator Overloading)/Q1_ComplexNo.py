# 1. Create a class Complex Number with data members as real and imag and add following methods :
# a. Constructor
# b. Destructor
# c. Overload +,- operator

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
        print("Constructor called...")

    def __del__(self):
        print("Destructor called...")

    def __add__(self, other):
        r = self.real + other.real
        i = self.imag + other.imag
        return Complex(r, i)

    def __sub__(self, other):
        r = self.real - other.real
        i = self.imag - other.imag
        return Complex(r, i)

c1 = Complex(5, 3)
c2 = Complex(2, 4)

print("First Complex Number:", c1.real, "+", c1.imag, "i")
print("Second Complex Number:", c2.real, "+", c2.imag, "i")

add_result = c1 + c2
sub_result = c1 - c2

print("\nAfter Addition:", add_result.real, "+", add_result.imag, "i")
print("After Subtraction:", sub_result.real, "+", sub_result.imag, "i")