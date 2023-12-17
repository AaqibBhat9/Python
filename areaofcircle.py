# Author: Aaqib Hilal

import math

# Function to calculate the area of a circle
def calculate_circle_area(radius):
    return math.pi * (radius ** 2)

# Taking user input for the radius of the circle
radius = float(input("Enter the radius of the circle: "))

# Calculating the area of the circle
area = calculate_circle_area(radius)

# Displaying the area of the circle
print("The area of the circle with radius", radius, "is:", area)
