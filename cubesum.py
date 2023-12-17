# Author: Aaqib Hilal

# Function to calculate the sum of cubes of first n natural numbers
def sum_of_cubes(n):
    return ((n * (n + 1)) // 2) ** 2

# Taking user input for the value of n
n = int(input("Enter the value of n: "))

# Calculating the sum of cubes of first n natural numbers
result = sum_of_cubes(n)

# Displaying the result
print(f"The sum of cubes of the first {n} natural numbers is:", result)
