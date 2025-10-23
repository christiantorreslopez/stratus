"""
Let's learn about reading and writing files!

Files let your programs save data permanently. When you write to a file,
the data stays there even after your program ends.

The example below shows how to write to a file and read from it.
"""

# Write to a file
with open("temperature.txt", "w") as file:
    file.write("85\n")
    file.write("82\n")
    file.write("88\n")

# Read from a file
with open("temperature.txt") as file:
    content = file.read()
    print("File contents:")
    print(content)

"""
Notice how we used 'with open()' to work with files? The 'with' statement
automatically closes the file for us. We used "w" mode to write and "r" mode to read.

Now let's practice reading and writing files!
"""

# Write three city names to a file called "cities.txt", one per line
with open("cities.txt", "w") as file:
    file.write("Houston\n")
    file.write("Austin\n")
    file.write("Dallas\n")

# Read the contents of "cities.txt" and print them
with open("cities.txt") as file:
    content = file.read()
    print("Cities:")
    print(content)

# Create a list of temperatures: [75, 78, 72, 80, 76]
temperatures = [75, 78, 72, 80, 76]

# Write each temperature to a file called "temps.txt", one per line
with open("temps.txt", "w") as file:
    for temp in temperatures:
        file.write(str(temp) + "\n")

# Read "temps.txt" line by line and print each line (use rstrip() to remove newlines)
with open("temps.txt") as file:
    for line in file:
        print(line.rstrip())
