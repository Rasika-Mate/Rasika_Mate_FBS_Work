# 1. Develop a simple calculator program that performs basic arithmetic operations (+, -, *, /) on two numbers provided by the user. The program should ask the user for
# the numbers and the operator. However, the program should handle the following exceptions:
# a. Invalid Number: If the user enters a number that is not valid, catch the exception and display an error message.
# b. Invalid Operator: If the user enters an operator other than "+", "-", "*", or "/", catch the exception and display an error message.
# c. Division by Zero: If the user tries to divide by zero, catch the exception and display an error message.
# WAP that performs the requested arithmetic operation and handles the exceptions as described above.

try:
    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))
    operator = input("Enter Operator (+, -, *, /): ")

    if operator == '+':
        result = num1 + num2
        print("Result:", result)
    elif operator == '-':
        result = num1 - num2
        print("Result:", result)
    elif operator == '*':
        result = num1 * num2
        print("Result:", result)
    elif operator == '/':
        try:
            result = num1 / num2
            print("Result:", result)
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
    else:
        raise ValueError("Invalid operator entered!")

except ValueError as e:
    print("Error:", e)

except Exception as e:
    print("Unexpected error:", e)