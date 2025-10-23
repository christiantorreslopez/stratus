# Chapter 8: Libraries

## What are Libraries?

A library (also called a module) is a collection of pre-written code that you can use in your programs. Think of it like a toolbox - instead of building every tool from scratch, you can use tools that others have already created.

Python comes with many built-in libraries, and you can also install third-party libraries created by other developers.

## Why Use Libraries?

1. **Save Time** - Don't reinvent the wheel; use existing solutions
2. **Reliability** - Well-tested code that many people use
3. **Functionality** - Access to powerful features without writing complex code
4. **Focus** - Spend time on your specific problem, not building basic tools

## Importing Libraries

To use a library, you need to **import** it at the top of your Python file.

### Import the entire module
```python
import random

# Use functions from the module with dot notation
number = random.randint(1, 10)
```

### Import specific functions
```python
from random import randint, choice

# Use the functions directly without the module name
number = randint(1, 10)
city = choice(["Houston", "Austin", "Dallas"])
```

## Installing Third-Party Libraries

Python has thousands of third-party libraries available through PyPI (Python Package Index). You can install them using `pip`:

```bash
pip install requests
```

Then use them in your code:
```python
import requests

response = requests.get("https://api.weather.gov/...")
```

## Best Practices

1. **Import at the top** - Put all imports at the beginning of your file
2. **Import what you need** - Use `from module import function` for specific functions
3. **Read documentation** - Learn what functions are available in each library
