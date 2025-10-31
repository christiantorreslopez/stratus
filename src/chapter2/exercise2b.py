"""
Let's practice working with numbers - integers and floats!

Integers are whole numbers, and floats are decimal numbers
"""

# Print happens to take care of not only strings but also numbers, how convenient!
temperature = 75
print(temperature)

# Make two variables. One called high_temp, another low_temp. Set them to integers of your choice. Then print the difference between the two.
high_temp = 100
low_temp = 60
print(high_temp - low_temp)

# Use the two variables and print their sum, difference, product, and division results to see how Python handles math operations with ints.
print(high_temp + low_temp)
print(high_temp - low_temp)
print(high_temp * low_temp)
print(high_temp // low_temp)

# Make a two variable called wind_mph, rainfall_inches and give them float values
wind_mph = 10.5
rainfall_inches = 1.4

# Use the two variables and print their sum, difference, product, and division results to see how Python handles math operations with floats.
print(wind_mph + rainfall_inches)
print(wind_mph - rainfall_inches)
print(wind_mph * rainfall_inches)
print(wind_mph // rainfall_inches)

"""
Now let's work with floats
"""

# Create a float variable for expected rainfall in inches (like 1.2 or 0.5)
expected_rainfall = 1.2

# Create a float variable for wind speed in mph (like 8.7)
wind_speed = 8.7

# Print both of your float variables
print(expected_rainfall)
print(wind_speed)

# Do some math: calculate what the wind speed would be if it doubled
print(wind_speed * 2)

# Convert a temperature: if it's 20 degrees Celsius, what is it in Fahrenheit?
# Formula: (Celsius * 9/5) + 32
temp_c = 100
temp_f = (temp_c * 9/5) + 32
print(temp_c)
print(temp_f)
