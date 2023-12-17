# Author: Aaqib Hilal

# Function to generate the Fibonacci series
def generate_fibonacci_series():
    fibonacci = [0, 1]
    while True:
        next_number = fibonacci[-1] + fibonacci[-2]
        if next_number > 10**18:  # Limiting the Fibonacci series for demonstration purposes
            break
        fibonacci.append(next_number)
    return fibonacci

# Function to find the nth multiple of a number in the Fibonacci series
def find_nth_multiple_of_number(n, number):
    fibonacci_series = generate_fibonacci_series()
    count = 0
    for fib in fibonacci_series:
        if fib % number == 0:
            count += 1
            if count == n:
                return fib
    return None

# Taking user input for the number and the value of n
given_number = int(input("Enter a number: "))
nth_multiple = int(input("Enter the value of n to find the nth multiple: "))

# Finding the nth multiple of the given number in the Fibonacci series
result = find_nth_multiple_of_number(nth_multiple, given_number)

# Displaying the result
if result is not None:
    print(f"The {nth_multiple}th multiple of {given_number} in the Fibonacci series is:", result)
else:
    print(f"There are fewer than {nth_multiple} multiples of {given_number} in the generated Fibonacci series.")
