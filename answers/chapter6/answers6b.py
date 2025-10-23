"""
Now let's learn about while loops and loop control (break and continue)!

While loops repeat as long as a condition is True. They're useful when you don't
know in advance how many times you need to loop.
"""

# Here's a while loop that counts up
temperature = 60

while temperature < 75:
    print("Current temperature:", temperature, "degrees")
    temperature += 5

print("Temperature reached:", temperature)

"""
Notice how the while loop keeps going until the condition becomes False?
Be careful - if the condition is always True, the loop will run forever!

Now let's practice while loops and loop control!
"""

# Create a variable called 'rain_chance' and set it to 100
rain_chance = 100

# Use a while loop to print the rain chance and decrease it by 10 each time until it's below 50
while rain_chance >= 50:
    print("Rain chance:", rain_chance, "%")
    rain_chance -= 10

# Create a list: temperatures = [75, 78, 95, 72, 80, 76]
temperatures = [75, 78, 95, 72, 80, 76]

# Use a for loop with break: print each temperature, but stop if you find a temperature above 90
for temp in temperatures:
    if temp > 90:
        print("Temperature too high:", temp, "- stopping check")
        break
    print("Temperature:", temp)

# Create a list: forecast = [72, -1, 75, 78, -1, 80] (where -1 means no data)
forecast = [72, -1, 75, 78, -1, 80]

# Use a for loop with continue: print only valid temperatures (skip -1 values)
for temp in forecast:
    if temp == -1:
        continue
    print("Valid temperature:", temp)
