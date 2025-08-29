"""
Now let's learn about functions that return values instead of just printing!
"""


# Example 1: A function that returns a value (1 input)
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


# Use the returned value
temp_celsius = convert_to_celsius(75)
print("75F is", temp_celsius, "C")

"""
Notice how we used 'return' instead of 'print' inside the function?
This lets us save the result and use it later!
"""

# Example 2: Create a function called `get_weather_message` with 1 input called `condition` and returns a string
# Note: Make sure that the function uses the `return` keyword instead of `print`

# Now call the function with an input, and save the returned value to a variable. Then, print that variable.

# Example 3: Create a function called 'get_city_weather' with 2 inputs: city_name and temperature, and returns a string

# Now call the function with a the inputs, and save the returned value to a variable. Then, print that variable.
