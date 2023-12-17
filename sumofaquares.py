# Author: Aaqib Hilal

# Function to calculate the sum of squares of first n natural numbers
def sum_of_squares(n):
    return (n * (n + 1) * (2 * n + 1)) // 6

# Taking user input for the value of n
n = int(input("Enter the value of n: "))

# Calculating the sum of squares of first n natural numbers
result = sum_of_squares(n)

# Displaying the result
print(f"The sum of squares of the first {n} natural numbers is:", result)
