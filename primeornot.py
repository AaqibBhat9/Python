# Author: Aaqib Hilal

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Taking user input for the number to check
number = int(input("Enter a number to check if it's prime or not: "))

# Checking if the number is prime and displaying the result
if is_prime(number):
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")
