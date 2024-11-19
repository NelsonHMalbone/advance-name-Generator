import random, sys

fileTXT = 'names.txt'

# read the txt file
with open(fileTXT) as file:
    content = file.readlines()



# the print statements to be printed out for when program is ran
greetings = "Please select an option:"
options = """1. Show the total number of names
2. Add a new name 
3. Select a random name
4. Exit
"""
# printing out the statements
print(greetings)
print(options)

while True:
    # have user enter a number 1-4 to continue
    userInput = input('Enter your choice (1-4): ')

    match userInput:
        # getting the total amount of items in a the txt file
        case '1':
            total_names = len(content)
            print(total_names)
