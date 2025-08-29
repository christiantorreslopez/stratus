"""
Now let's learn about using elif (else if) inside functions for multiple conditions!
"""


# Here's an example function that uses if/elif/else for multiple choices
def describe_weather(temp):
    if temp > 85:
        print("It's very hot!")
    elif temp > 70:
        print("It's warm and nice!")
    elif temp > 50:
        print("It's a bit cool!")
    else:
        print("It's cold!")


# Call the function to test it with different temperatures
describe_weather(90)
describe_weather(75)
describe_weather(60)
describe_weather(40)

"""
Notice how elif lets us check multiple conditions in order?
Python checks each condition from top to bottom and runs the first one that's True.
"""

# Example 1: Create a grade evaluation function
# Create a function called 'grade_evaluator' that takes a parameter called 'score'
# - If score is 90 or above: print "Grade: A"
# - Elif score is 80 or above: print "Grade: B"
# - Elif score is 70 or above: print "Grade: C"
# - Else: print "Grade: F"

# Test your function by calling it with different scores like 95, 85, 75, and 65

# Example 2: Create a weather activity recommender function
# Create a function called 'activity_recommender' that takes a parameter called 'weather_condition'
# - If weather_condition equals "sunny": print "Go for a hike!"
# - Elif weather_condition equals "rainy": print "Read a book indoors!"
# - Elif weather_condition equals "snowy": print "Build a snowman!"
# - Else: print "Check the weather and decide!"

# Test your function by calling it with different conditions like "sunny", "rainy", "snowy", and "cloudy"
