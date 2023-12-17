# Author: Aaqib Hilal

# Function to add two numbers
def add_numbers(a, b):
    return a + b

# Taking user input for two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Calling the function and storing the result
result = add_numbers(num1, num2)

# Displaying the result
print("The sum of", num1, "and", num2, "is:", result)
