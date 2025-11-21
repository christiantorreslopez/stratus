"""
Now let's learn about dictionary methods and how to iterate through dictionaries!

Dictionaries have useful methods like keys(), values(), and items() that help you
work with their data. You can also loop through dictionaries just like lists.
"""

# Here's a dictionary of cities and temperatures
city_temps = {"Houston": 85, "Austin": 82, "Dallas": 88, "San Antonio": 86}

# Loop through all cities (keys)
print("Cities:")
for city in city_temps:
    print(city)

# Loop through all temperatures (values)
print("\nTemperatures:")
for temp in city_temps.values():
    print(temp)

# Loop through both cities and temperatures (items)
print("\nCity weather:")
for city, temp in city_temps.items():
    print(city, "is", temp, "degrees")

"""
Notice how we can iterate through the dictionary in different ways?
This gives us flexibility in how we process the data.

Now let's practice dictionary methods and iteration!
"""

# Create a dictionary called 'weekly_forecast' mapping day names to temperatures
weekly_forecast = {"Sun": 55, "Mon": 60, "Tue": 65, "Wed": 70, "Thu": 75, "Fri": 80, "Sat": 85}

# Use a for loop to print each day and its temperature
for day, temp in weekly_forecast.items():
    print(day, temp)

# print the same result but only using the keys in the loop
for day in weekly_forecast:
    print(day, weekly_forecast[day])

# Use .values() to get all the temperatures and calculate the average temperature
temp_sum = 0
for temp in weekly_forecast.values():
    temp_sum += temp
print(temp_sum/len(weekly_forecast))

# Create a dictionary called 'city_conditions' mapping cities to weather conditions

# Use a for loop with .items() to print formatted weather reports like "Houston: sunny"

# Check if a specific city exists in your dictionary, if so print its condition
