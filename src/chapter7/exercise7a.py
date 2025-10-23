"""
Let's learn about dictionaries - a way to store data as key-value pairs!

Dictionaries let you associate data together. Instead of having separate lists for
cities and temperatures, you can create one dictionary that maps cities to temperatures.
"""

# Here's a dictionary mapping cities to their temperatures
city_temperatures = {"Houston": 85, "Austin": 82, "Dallas": 88}

print(city_temperatures)

# Access a specific city's temperature using its key
print("Houston temperature:", city_temperatures["Houston"])
print("Austin temperature:", city_temperatures["Austin"])

# Add a new city to the dictionary
city_temperatures["San Antonio"] = 86
print(city_temperatures)

"""
Notice how we use curly braces {} for dictionaries and access values using keys
instead of numeric indices? This makes our code more readable and meaningful!

Now let's practice creating and using dictionaries!
"""

# Create a dictionary called 'city_weather' that maps 3 cities to weather conditions (like "sunny", "rainy")

# Print the entire dictionary

# Print the weather condition for one of your cities

# Add a new city and its weather condition to your dictionary

# Print the updated dictionary

# Create a dictionary called 'rainfall_data' that maps cities to rainfall amounts (numbers)

# Print a specific city's rainfall amount

# Update one city's rainfall amount to a new value

# Print the updated dictionary

# Check if a city exists in your dictionary using 'in' and print a message
