# Chapter 3: Creating Your Own Functions

Remember in Chapter 0 when you learned that `print()` is a function - a command that tells the computer what to do? You've been using functions that Python already knows about. Now it's time to create your own!

## Creating Your Own Functions

Just like you learned in Chapter 0 that `print()` is a function, you can create your own functions using the `def` keyword:

```python
def announce_name(name):
    print(name)
```

Notice how the `print` code is indented. Python relies on indentation to understand what is part of a function.

Remember: to call the function, you simply use its name followed by parentheses:

```python
show_weather()  # Output: Today's weather is sunny!
```

## Functions with Parameters

Remember how `print()` takes arguments? Your functions can too! We call these **parameters** when defining the function:

```python
def show_weather(condition):
    print("Today's weather is", condition + "!")

show_weather("sunny")   # Output: Today's weather is sunny!
show_weather("rainy")   # Output: Today's weather is rainy!
```

Just like `print("Hello")` where `"Hello"` is the argument you give to `print()`, here `"sunny"` is the argument you give to your `show_weather()` function.

## Zero or more parameters

Turns out functions can have zero or more parameters. Let's look at some examples:

```python
def greet():
    print("Hello!")

def add_two_numbers(a, b):
    print(a + b)

def add_three_numbers(a, b, c):
    print(a + b + c)
```

## Functions that Return Values

So far, we've been using functions that print results. But what if you want to use the result later? That's where return values come in.

```python
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

temp_celsius = convert_to_celsius(75)
# print("75°F is", temp_celsius, "°C")  # Output: 75°F is 23.888... °C
```

## Why Create Your Own Functions?

You might wonder: "Why create my own functions when `print()` already works?" Great question! Here's why:

1. **Avoid repetition** - Instead of writing the same code over and over, write it once in a function
2. **Organization** - Break big weather reports into smaller, manageable pieces
3. **Flexibility** - Change one function and it updates everywhere you use it
4. **Readability** - `create_weather_report()` is clearer than lots of individual `print()` statements
