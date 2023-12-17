# Author: Aaqib Hilal

# Function to calculate simple interest
def calculate_simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest

# Taking user input for principal amount, rate, and time period
principal_amount = float(input("Enter the principal amount: "))
rate_of_interest = float(input("Enter the annual interest rate: "))
time_period = float(input("Enter the time period (in years): "))

# Calling the function to calculate simple interest
simple_interest = calculate_simple_interest(principal_amount, rate_of_interest, time_period)

# Displaying the simple interest
print("The simple interest is:", simple_interest)
