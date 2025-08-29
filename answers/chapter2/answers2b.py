"""
Let's practice working with numbers - integers and floats!

Integers are whole numbers, and floats are decimal numbers
"""

# Print happens to take care of not only strings but also numbers, how convenient!
temperature = 75
print(temperature)

# Make two variables. One called high_temp, another low_temp. Set them to integers of your choice. Then print the difference between the two.
high_temp = 85
low_temp = 62
print(high_temp - low_temp)

# Use the two variables and print their sum, difference, product, and division results to see how Python handles math operations with ints.
print(high_temp + low_temp)  # sum
print(high_temp - low_temp)  # difference
print(high_temp * low_temp)  # product
print(high_temp / low_temp)  # division

# Make a two variable called wind_mph, rainfall_inches and give them float values
wind_mph = 12.5
rainfall_inches = 2.3

# Use the two variables and print their sum, difference, product, and division results to see how Python handles math operations with floats.
print(wind_mph + rainfall_inches)  # sum
print(wind_mph - rainfall_inches)  # difference
print(wind_mph * rainfall_inches)  # product
print(wind_mph / rainfall_inches)  # division

"""
Now let's work with floats
"""

# Create a float variable for expected rainfall in inches (like 1.2 or 0.5)
rainfall = 1.2

# Create a float variable for wind speed in mph (like 8.7)
wind_speed = 8.7

# Print both of your float variables
print(rainfall)
print(wind_speed)

# Do some math: calculate what the wind speed would be if it doubled
doubled_wind = wind_speed * 2
print(doubled_wind)

# Convert a temperature: if it's 20 degrees Celsius, what is it in Fahrenheit?
# Formula: (Celsius * 9/5) + 32
celsius = 20
fahrenheit = (celsius * 9 / 5) + 32
print(fahrenheit)
