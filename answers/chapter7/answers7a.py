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
city_weather = {"Houston": "sunny", "Austin": "cloudy", "Dallas": "partly cloudy"}

# Print the entire dictionary
print(city_weather)

# Print the weather condition for one of your cities
print("Houston weather:", city_weather["Houston"])

# Add a new city and its weather condition to your dictionary
city_weather["San Antonio"] = "rainy"

# Print the updated dictionary
print(city_weather)

# Create a dictionary called 'rainfall_data' that maps cities to rainfall amounts (numbers)
rainfall_data = {"Houston": 2.5, "Austin": 1.3, "Dallas": 0.8, "San Antonio": 3.2}

# Print a specific city's rainfall amount
print("Austin rainfall:", rainfall_data["Austin"], "inches")

# Update one city's rainfall amount to a new value
rainfall_data["Houston"] = 3.0

# Print the updated dictionary
print(rainfall_data)

# Check if a city exists in your dictionary using 'in' and print a message
if "Dallas" in rainfall_data:
    print("Dallas is in the rainfall data")
