# Chapter 9: File I/O

## What is File I/O?

File I/O (Input/Output) lets your programs read from and write to files. Until now, all your data has been stored in memory - when your program ends, everything is lost. Files allow you to:

- Save data permanently
- Read data from external sources
- Share data between programs
- Store large datasets

Think of it like saving weather data to a file so you can analyze it later!

## Opening Files

Python's `open()` function is used to work with files. You specify the filename and the **mode**:

```python
file = open("weather.txt", "r")  # Open for reading
```

### File Modes

- `"r"` - **Read** mode (default) - read existing file
- `"w"` - **Write** mode - create new file or overwrite existing
- `"a"` - **Append** mode - add to end of existing file

## The `with` Statement

The `with` statement automatically closes files for you, even if errors occur:

```python
with open("weather.txt", "r") as file:
    content = file.read()
    print(content)
# File is automatically closed here
```

**Always use `with` when working with files!** It prevents errors and resource leaks.

## Reading Files

### Read Entire File

```python
with open("temperatures.txt", "r") as file:
    content = file.read()
    print(content)
```

### Read Line by Line

```python
with open("temperatures.txt", "r") as file:
    for line in file:
        print(line.rstrip())  # rstrip() removes trailing newline
```

### Read All Lines into a List

```python
with open("temperatures.txt", "r") as file:
    lines = file.readlines()
    print(lines)  # List of lines
```

## Writing Files

### Write Mode (`"w"`)

**Warning:** This will overwrite the entire file!

```python
with open("forecast.txt", "w") as file:
    file.write("Houston: 85 degrees\n")
    file.write("Austin: 82 degrees\n")
```

### Append Mode (`"a"`)

Adds to the end without deleting existing content:

```python
with open("forecast.txt", "a") as file:
    file.write("Dallas: 88 degrees\n")
```

## Working with CSV Files

CSV (Comma-Separated Values) files store data in tables. Each line is a row, and commas separate columns.

Example `weather.csv`:
```
City,Temperature,Condition
Houston,85,sunny
Austin,82,cloudy
Dallas,88,sunny
```

### Reading CSV Files

#### Manual Method (splitting by comma)

```python
with open("weather.csv", "r") as file:
    for line in file:
        city, temp, condition = line.rstrip().split(",")
        print(f"{city}: {temp}°F, {condition}")
```

#### Using csv Module

```python
import csv

with open("weather.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    for row in reader:
        city, temp, condition = row
        print(f"{city}: {temp}°F, {condition}")
```

#### Using csv.DictReader (Recommended!)

```python
import csv

with open("weather.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row['City']}: {row['Temperature']}°F, {row['Condition']}")
```

### Writing CSV Files

#### Manual Method

```python
with open("weather.csv", "w") as file:
    file.write("City,Temperature,Condition\n")
    file.write("Houston,85,sunny\n")
    file.write("Austin,82,cloudy\n")
```

#### Using csv.DictWriter (Recommended!)

```python
import csv

cities = [
    {"City": "Houston", "Temperature": 85, "Condition": "sunny"},
    {"City": "Austin", "Temperature": 82, "Condition": "cloudy"},
    {"City": "Dallas", "Temperature": 88, "Condition": "sunny"}
]

with open("weather.csv", "w", newline="") as file:
    fieldnames = ["City", "Temperature", "Condition"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()  # Write column names
    writer.writerows(cities)  # Write all rows
```

## Common Patterns

### Check if File Exists

```python
import os

if os.path.exists("weather.txt"):
    print("File exists!")
else:
    print("File not found!")
```

### Read and Process Data

```python
temperatures = []

with open("temps.txt", "r") as file:
    for line in file:
        temp = int(line.rstrip())
        temperatures.append(temp)

average = sum(temperatures) / len(temperatures)
print("Average temperature:", average)
```

### Write a List to File

```python
cities = ["Houston", "Austin", "Dallas"]

with open("cities.txt", "w") as file:
    for city in cities:
        file.write(city + "\n")
```

## Important Tips

1. **Always use `with`** - It closes files automatically
2. **Use `rstrip()`** - Remove trailing newlines when reading
3. **Add `\n`** - When writing, Python doesn't add newlines automatically
4. **Use CSV for tables** - Don't manually parse complex data
5. **Handle errors** - Files might not exist or be accessible

## File Paths

### Relative Paths
Relative to your current directory:
```python
with open("weather.txt", "r") as file:  # Same directory
with open("data/weather.txt", "r") as file:  # In 'data' folder
```

### Absolute Paths
Full path from root:
```python
with open("/Users/username/weather.txt", "r") as file:
```

## Common Errors

```python
# FileNotFoundError - File doesn't exist
with open("missing.txt", "r") as file:
    content = file.read()

# Solution: Check if file exists first or use try/except
```

## Why File I/O Matters

File I/O is essential for real-world programming:
- Store user data (settings, profiles)
- Log program activity
- Import/export data (weather records, sales data)
- Share data between programs
- Work with large datasets that don't fit in memory

Understanding file operations opens up countless possibilities for building practical applications!
