"""
Now let's learn about pandas - a powerful library for working with data!

Pandas makes it easy to organize data in tables (called DataFrames) and analyze it.
Think of a DataFrame like a spreadsheet with rows and columns.

The example below shows how to create and work with weather data using pandas.
"""

import pandas as pd

# Create a DataFrame with city weather data
weather_data = {
    "City": ["Houston", "Austin", "Dallas"],
    "Temperature": [85, 82, 88],
    "Condition": ["sunny", "cloudy", "sunny"],
}

df = pd.DataFrame(weather_data)
print("Weather DataFrame:")
print(df)

# Access a specific column
print("\nTemperatures:")
print(df["Temperature"])

# Calculate the average temperature
average_temp = df["Temperature"].mean()
print("\nAverage temperature:", average_temp)

"""
Notice how pandas organizes data into a table format? Each column has a name,
and pandas provides easy methods like .mean() to analyze the data.

Now let's practice using pandas!
"""

# Create a dictionary with data for 5 cities: city names, temperatures, and humidity levels

# Create a DataFrame from your dictionary and print it

# Print just the Temperature column

# Calculate and print the average humidity using .mean()

# Calculate and print the maximum temperature using .max()
