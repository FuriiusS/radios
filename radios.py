import math

# Define the value of pi with 6 decimal places
PI = math.pi  # This gives us the built-in pi value in Python, which is already quite accurate
PI = round(PI, 6)  # Round it to 6 decimal places

# Function to calculate the circumference
def calculate_circumference(radius):
    circumference = 2 * PI * radius
    return circumference

# Test the function with radii of 3, 8, and 10
radii = [3, 8, 10]
for radius in radii:
    circumference = calculate_circumference(radius)
    print(f'La circunferencia de un círculo con radio {radius} es {circumference}')
