# Author: Aaqib Hilal

# Function to calculate factorial of a number
def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        factorial = 1
        for i in range(2, n + 1):
            factorial *= i
        return factorial

# Taking user input for a number
num = int(input("Enter a number to calculate its factorial: "))

# Calling the function to calculate factorial
result = calculate_factorial(num)

# Displaying the factorial
print("The factorial of", num, "is:", result)
