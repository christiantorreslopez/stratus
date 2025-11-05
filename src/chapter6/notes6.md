# Chapter 6: Loops

## What are Loops?

Loops allow you to repeat code multiple times without writing it over and over. Imagine you have a list of temperatures for a week and want to print each one. Without loops, you'd need to write `print()` seven times. With loops, you write it once and let Python repeat it!

Think of a loop like checking the weather for each day of the week - you're doing the same action repeatedly, just with different data each time.

## For Loops

The most common loop is the **for loop**, which iterates through items in a list (or other collections).

```python
temperatures = [75, 78, 72, 80, 76]

for anything in temperatures:
    print(anything)
```

This prints:
```
75
78
72
80
76
```

The loop takes each item from the list, one at a time, and runs the code inside the loop.

### More For Loop Examples

You can use any variable name for the item:

```python
cities = ["Houston", "Austin", "Dallas"]

for city in cities:
    print("The weather in", city, "is beautiful!")
```

You can perform operations inside loops:

```python
temperatures = [75, 78, 72, 80, 76]

for temp in temperatures:
    celsius = (temp - 32) * 5 / 9
    print(temp, "F is", celsius, "C")
```

## The range() Function

The `range()` function generates a sequence of numbers, which is useful for repeating code a specific number of times:

```python
# Print numbers 0 through 4
for i in range(5):
    print(i)
```

Output:
```
0
1
2
3
4
```

You can specify start, stop, and step:

```python
# Count from 1 to 5
for i in range(1, 6):
    print("Day", i)

# Count by 2s from 0 to 10
for i in range(0, 11, 2):
    print(i)  # 0, 2, 4, 6, 8, 10
```

## While Loops

A **while loop** repeats as long as a condition is True. It's useful when you don't know in advance how many times you need to loop.

```python
temperature = 60

while temperature < 75:
    print("Current temp:", temperature)
    temperature += 5
```

Output:
```
Current temp: 60
Current temp: 65
Current temp: 70
```

**Important:** Make sure your while loop will eventually stop! If the condition is always True, you'll have an infinite loop.

### While Loop Example

```python
rain_chance = 90

while rain_chance > 50:
    print("Rain chance is", rain_chance, "- bring an umbrella!")
    rain_chance -= 10

print("Rain chance is now low!")
```

## Loop Control: break and continue

Sometimes you need to stop a loop early or skip certain iterations.

### break - Exit the loop immediately

```python
temperatures = [75, 78, 72, 95, 76, 74]

for temp in temperatures:
    if temp > 90:
        print("Temperature too high! Stopping check.")
        break
    print("Temperature:", temp)
```

Output:
```
Temperature: 75
Temperature: 78
Temperature: 72
Temperature too high! Stopping check.
```

### continue - Skip to the next iteration

```python
temperatures = [75, 78, -1, 80, -1, 74]

for temp in temperatures:
    if temp < 0:
        continue  # Skip invalid temperatures
    print("Valid temperature:", temp)
```

Output:
```
Valid temperature: 75
Valid temperature: 78
Valid temperature: 80
Valid temperature: 74
```

## Nested Loops

You can put loops inside other loops. This is useful for working with multiple lists:

```python
cities = ["Houston", "Austin"]
days = ["Monday", "Tuesday"]

for city in cities:
    for day in days:
        print(city, day)
```

Output:
```
Houston Monday
Houston Tuesday
Austin Monday
Austin Tuesday
```

## Why Use Loops?

1. **Avoid Repetition** - Write code once, run it many times
2. **Process Collections** - Work with every item in a list easily
3. **Unknown Quantities** - Handle lists of any size with the same code
4. **Cleaner Code** - More readable than copying/pasting the same code
5. **Flexibility** - Easy to modify behavior for all iterations at once

Loops are fundamental to programming. You'll use them constantly to process data, validate input, and automate repetitive tasks!
