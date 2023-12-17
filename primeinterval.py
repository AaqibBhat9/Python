# Author: Aaqib Hilal

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Function to print prime numbers within an interval
def print_primes_in_interval(start, end):
    print(f"Prime numbers between {start} and {end} are:")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=" ")

# Taking user input for the interval
start_num = int(input("Enter the starting number of the interval: "))
end_num = int(input("Enter the ending number of the interval: "))

# Calling the function to print prime numbers within the interval
print_primes_in_interval(start_num, end_num)
