# Author: Aaqib Hilal

# Function to find the maximum of two numbers
def find_maximum(a, b):
    return max(a, b)

# Taking user input for two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Calling the function to find the maximum
maximum = find_maximum(num1, num2)

# Displaying the maximum number
print("The maximum of", num1, "and", num2, "is:", maximum)
