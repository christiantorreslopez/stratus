"""
Now let's learn about CSV files - a common format for storing tabular data!

CSV stands for Comma-Separated Values. Each line is a row, and commas separate
the columns. Python's csv module makes it easy to read and write CSV files.

The example below shows how to work with CSV files.
"""

import csv

# Write to a CSV file
with open("weather.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["City", "Temperature"])
    writer.writeheader()
    writer.writerow({"City": "Houston", "Temperature": 85})
    writer.writerow({"City": "Austin", "Temperature": 82})

# Read from a CSV file
with open("weather.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row['City']}: {row['Temperature']}°F")

"""
Notice how csv.DictWriter and csv.DictReader use dictionaries? This makes
it easy to work with column names instead of worrying about column positions.

Now let's practice working with CSV files!
"""

# Create a list of dictionaries with city weather data (at least 3 cities)
# Each dictionary should have: City, Temperature, Condition
weather_data = [
    {"City": "Houston", "Temperature": 85, "Condition": "sunny"},
    {"City": "Austin", "Temperature": 82, "Condition": "cloudy"},
    {"City": "Dallas", "Temperature": 88, "Condition": "sunny"},
    {"City": "San Antonio", "Temperature": 86, "Condition": "partly cloudy"},
]

# Write your weather data to a file called "forecast.csv" using csv.DictWriter
with open("forecast.csv", "w", newline="") as file:
    fieldnames = ["City", "Temperature", "Condition"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(weather_data)

# Read "forecast.csv" using csv.DictReader and print each city's forecast
print("\nAll forecasts:")
with open("forecast.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row['City']}: {row['Temperature']}°F, {row['Condition']}")

# Read "forecast.csv" again and print only cities with temperature above 80
print("\nCities above 80°F:")
with open("forecast.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if int(row["Temperature"]) > 80:
            print(f"{row['City']}: {row['Temperature']}°F")
