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
    return "Good morning! It's " + condition + " today. Have a great day!"


# Test your function with "sunny" and print the result
greeting = weather_greeting("sunny")
print(greeting)


# Create a function called 'calculate_wind_chill' that takes temperature and wind speed
# and returns a simple wind chill estimate (temp - wind_speed for simplicity)
def calculate_wind_chill(temperature, wind_speed):
    return temperature - wind_speed


# Test your function with temperature 30 and wind speed 15
wind_chill = calculate_wind_chill(30, 15)
print("With 30°F and 15mph wind, it feels like", wind_chill, "degrees")


# Create a function called 'create_forecast' that takes city, temperature, and condition
# and returns a complete weather forecast sentence
def create_forecast(city, temperature, condition):
    return (
        "Today in "
        + city
        + ", it will be "
        + condition
        + " with a high of "
        + str(temperature)
        + " degrees."
    )


# Test your function with your local weather information
forecast = create_forecast("Dallas", 82, "partly cloudy")
print(forecast)


# Create a function called 'convert_to_fahrenheit' that takes celsius and returns fahrenheit
# Formula: (celsius * 9/5) + 32
def convert_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


# Test it by converting 25 degrees Celsius to Fahrenheit
fahrenheit = convert_to_fahrenheit(25)
print("25°C equals", fahrenheit, "°F")


# Create a function called 'calculate_rainfall_average' that takes two rainfall amounts
# and returns the average rainfall
def calculate_rainfall_average(rainfall1, rainfall2):
    return (rainfall1 + rainfall2) / 2


# Test it with rainfall amounts like 2.5 and 1.8 inches
average_rainfall = calculate_rainfall_average(2.5, 1.8)
print("Average rainfall is", average_rainfall, "inches")
