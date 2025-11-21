"""
Let's practice more advanced loop patterns including nested loops!

Nested loops are loops inside other loops. They're useful when you need to work
with multiple lists or do repeated operations within repeated operations.
"""

# Here's a nested loop example: checking weather for multiple cities over multiple days
cities = ["Houston", "Austin"]
days = ["Monday", "Tuesday", "Wednesday"]

for city in cities:
    for day in days:
        print(day, "forecast for", city)

print()  # Empty line for spacing

"""
Notice how the inner loop (days) completes fully for each iteration of the outer loop (cities)?
This creates all combinations of cities and days.

Now let's practice advanced loop patterns!
"""

# Create two lists: cities = ["Dallas", "San Antonio", "Houston"] and temps = [85, 82, 88]
cities = ["Dallas", "San Antonio", "Houston"]
temps = [85, 82, 88]

# Use a nested loop to print each city with each temperature (all combinations)
for c in cities:
    for t in temps:
        # print(c, t)
        print(c + ': ' + str(t))

# range(start_inclusive, end_exclusive)

# for outer in range(4):
#     for inner in range(4):
#         print(outer, inner)
#         if inner == outer:
#             break

# for VARIABLE in RANGE VVV
# range(start_inclusive, end_exclusive)

for outer in range(4):
    for inner in range(outer + 1):
        print(outer, inner)

"""
0,0

1,0
1,1

2,0
2,1
2,2

3,0
3,1
3,2
3,3
"""





# Create a list: weekly_temps = [70, 75, 80, 85, 75, 72, 68]

# Use a for loop to calculate and print the average temperature

# Create two lists: morning_temps = [65, 68, 70] and evening_temps = [78, 82, 80]

# Use a for loop with range to print both temperatures for each day
