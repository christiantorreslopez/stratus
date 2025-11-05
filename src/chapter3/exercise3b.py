"""
Now let's practice functions with parameters and return values!

Parameters are like ingredients in a recipe - you can change them to get different results.
Return values are like the finished dish - the function gives you back something useful.

The examples below show functions that take inputs and give back outputs.
"""


def create_weather_message(city):
    message = "Weather report for " + city + " is coming up!"
    return message


# Call the function and store the result
report = create_weather_message("Austin")
print(report)


def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


# Call the function and use the result
temp_celsius = convert_to_celsius(75)
print("75°F equals", temp_celsius, "°C")

"""
Notice how parameters make functions flexible - the same function can work with
different inputs. Return values let you get results back to use in other places.

Time to practice with your own weather parameter functions!
"""


# Create a function called 'weather_greeting' that takes a weather condition parameter
# and returns a greeting message about that weather
def weather_greeting(condition):
    message = "It is " + condition + " today."
    return message

# Test your function with "sunny" and print the result
message2 = weather_greeting("sunny")
print(message2)

# Create a function called 'calculate_wind_chill' that takes temperature and wind speed
# and returns a simple wind chill estimate (temp - wind_speed for simplicity)
def calculate_wind_chill(temp, wind_speed):
    return temp - wind_speed

# Test your function with temperature 30 and wind speed 15
temp = 30
wind_speed = 15
wind_chill = calculate_wind_chill(temp, wind_speed)
print(wind_chill)

# Create a function called 'create_forecast' that takes city, temperature, and condition
# and returns a complete weather forecast sentence

# Test your function with your local weather information

# Create a function called 'convert_to_fahrenheit' that takes celsius and returns fahrenheit
# Formula: (celsius * 9/5) + 32
def convert_to_fahrenheit(temp_c):
    return (temp_c * 9/5) + 32

temperature = 100
print(convert_to_fahrenheit(temperature))

# Test it by converting 25 degrees Celsius to Fahrenheit

# Create a function called 'calculate_rainfall_average' that takes two rainfall amounts
# and returns the average rainfall

# Test it with rainfall amounts like 2.5 and 1.8 inches
