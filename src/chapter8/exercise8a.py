"""
Let's learn about libraries - pre-written code you can use in your programs!

Libraries save you time by providing useful functions. Instead of writing code to
generate random numbers from scratch, you can use the 'random' library.

The example below shows how to import and use the random module.
"""

import random

# Generate a random temperature between 60 and 90
random_temp = random.randint(60, 90)
print("Random temperature:", random_temp)

# Pick a random city from a list
cities = ["Houston", "Austin", "Dallas", "San Antonio"]
random_city = random.choice(cities)
print("Random city:", random_city)

"""
Notice how we imported the random module at the top, then used its functions
with dot notation (random.randint, random.choice)?

Now let's practice using the random module!
"""

# Create a list of at least 5 weather conditions (like "sunny", "rainy", "cloudy", etc.)

# Use random.choice() to select a random weather condition and print it

# Use random.randint() to generate a random temperature between 50 and 100 and print it
