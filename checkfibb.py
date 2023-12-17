# Author: Aaqib Hilal

# Function to check if a number is a perfect square
def is_perfect_square(num):
    return (int(num**0.5))**2 == num

# Function to check if a number is a Fibonacci number
def is_fibonacci(num):
    if num <= 0:
        return False
    return is_perfect_square(5 * num * num + 4) or is_perfect_square(5 * num * num - 4)

# Taking user input for the number to check
number_to_check = int(input("Enter a number to check if it's a Fibonacci number: "))

# Checking if the number is a Fibonacci number and displaying the result
if is_fibonacci(number_to_check):
    print(number_to_check, "is a Fibonacci number.")
else:
    print(number_to_check, "is not a Fibonacci number.")
