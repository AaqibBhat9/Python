# Author: Aaqib Hilal

# Function to calculate compound interest
def calculate_compound_interest(principal, rate, time, frequency):
    amount = principal * (1 + (rate / frequency)) ** (frequency * time)
    compound_interest = amount - principal
    return compound_interest

# Taking user input for principal amount, rate, time period, and frequency of compounding
principal_amount = float(input("Enter the principal amount: "))
rate_of_interest = float(input("Enter the annual interest rate: "))
time_period = float(input("Enter the time period (in years): "))
compounding_frequency = int(input("Enter the frequency of compounding per year: "))

# Calling the function to calculate compound interest
compound_interest = calculate_compound_interest(principal_amount, rate_of_interest, time_period, compounding_frequency)

# Displaying the compound interest
print("The compound interest is:", compound_interest)
