"""
Let's learn how to create and use functions!

Functions are like recipes - they contain instructions that you can use over and over.
Think of them as your own custom commands that you create in Python.

The example below shows how to create a simple function and call it.
"""


def show_weather():
    print("Today's weather is beautiful!")


# Call the function
show_weather()

"""
Did you see how we defined the function with 'def' and then called it by using its name
with parentheses? Functions let you organize your code and avoid repeating yourself.

Now let's practice creating your own weather functions!
"""


# Create a function called 'show_temperature' that prints a temperature message
def show_temperature():
    print("The temperature is 75 degrees today")


# Call your function to test it
show_temperature()


# Create a function called 'show_forecast' that prints tomorrow's expected weather
def show_forecast():
    print("Tomorrow will be partly cloudy with a high of 78 degrees")


# Call your show_forecast function
show_forecast()


# Create a function called 'show_season' that prints what season it is and typical weather
def show_season():
    print("It's fall season with mild temperatures and changing leaves")


# Call your show_season function
show_season()


# Create a function called 'weather_advice' that prints advice based on current conditions
def weather_advice():
    print("It's sunny today, so don't forget sunscreen and sunglasses!")


# Call your weather_advice function
weather_advice()

# Now call all your functions one after another to create a complete weather report!
print("Here's your complete weather report:")
show_temperature()
show_forecast()
show_season()
weather_advice()
