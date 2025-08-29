# Chapter 2: Data Types - Strings, Ints, Floats

## What are Data Types?

Data types are like different categories of information. Just like you organize things in your room into different types (clothes, books, games), Python organizes data into different types.

The three main types you'll use are:
- **Strings** - Text (like words and sentences)
- **Integers** - Whole numbers (5, 100, -3)
- **Floats** - Decimal numbers (3.14, 2.5, -1.2, 1.0)

## Strings

Strings are text wrapped in quotes. Think of them like a string of letters tied together.

```python
weather_condition = "sunny"
city = "Austin"
```

You can use single quotes `'` or double quotes `"` in most cases. You can stick with double quotes for simplicity.

## Integers (also called int)

Integers are whole numbers without decimal points. Like counting objects - you can have 1 degree, 2 degrees, but not 1.5 degrees when talking about whole temperature readings.

```python
high_temp = 85
low_temp = 40
```

You can perform math operations with integers:

```python
high_temp = 85
low_temp = 40
print(high_temp + low_temp)  # Addition
print(high_temp - low_temp)  # Subtraction
print(high_temp * 2)         # Multiplication
print(high_temp // low_temp) # Floor Division. You'll get 2.0
print(high_temp / low_temp)  # Division. You'll get 2.125
```

## Floats

Floats are numbers with decimal points. Like measuring precise temperature - you might have 75.3 degrees or 2.5 inches of rainfall.

```python
high_temp = 85.4
low_temp = 40.3
```

You can also perform math operations with floats:

```python
high_temp = 85.4
low_temp = 40.3
print(high_temp + low_temp)  # Addition
print(high_temp - low_temp)  # Subtraction
print(high_temp * 2)         # Multiplication
print(high_temp / low_temp)  # Division. You'll get 2.119
print(high_temp // low_temp) # Floor Division. You'll get 2.0
```

## Note on ints vs floats

Math operations automatically convert integers to floats when needed.
- Addition: Adding an integer to a float results in a float.
- Subtraction: Subtracting an integer from a float results in a float. Same for a float from an int.
- Multiplication: Multiplying an integer by a float results in a float.
- Floor Division: Using two slashes will return an integer if both numbers are integers. If either number is a float, it will return a float.
- Division: Using one slash will always return a float.

## Math with Strings?

One common operation with strings is concatenation, which uses the `+` operator to join them together.

```python
city = "Dallas"
state = "Texas"
location = city + ", " + state
print(location)  # Output: Dallas, Texas
```

You can even use multiplication with strings like this:

```python
repeat = "Hello! "
print(repeat * 3)  # Output: Hello! Hello! Hello!
```

However, subtraction and division don't work with strings:

```python
print(city - state)  # Error!
print(city / state)  # Error!
```
