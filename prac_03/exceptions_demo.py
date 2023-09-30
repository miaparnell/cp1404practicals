"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")

# Question 1:
# A vValueError will occur if any non-integer is entered. For example, if a floating point number or a
# string is entered, this will return a value error.

# Question 2:
# A ZeroDivisionError will occur if the denominator entered is 0, as this results in an undefined result

# Question 3:
# YOu could change the code by checking if the value of the denominator is 0 before the numbers are divided.
# You can do this by adding an if/else to the try, and if the denominator is 0 it will print an error message.
