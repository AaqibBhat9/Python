# Author: Aaqib Hilal

# Function to check if a number is an Armstrong number
def is_armstrong_number(number):
    num_str = str(number)
    num_digits = len(num_str)
    sum_of_digits = 0

    for digit in num_str:
        sum_of_digits += int(digit) ** num_digits

    return number == sum_of_digits

# Taking user input for the number to check
num_to_check = int(input("Enter a number to check if it's an Armstrong number: "))

# Checking if the number is an Armstrong number and displaying the result
if is_armstrong_number(num_to_check):
    print(num_to_check, "is an Armstrong number.")
else:
    print(num_to_check, "is not an Armstrong number.")
