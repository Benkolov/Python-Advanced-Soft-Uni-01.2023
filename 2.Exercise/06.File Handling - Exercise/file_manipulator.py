# Import the 'os' module
import os

# Continuously prompt the user for input
while True:
    # Split the input into the command and its parameters
    command, *info = input().split('-')

    # If the command is 'End', break the loop
    if command == "End":
        break

    # If the command is 'Create', create a new file with the given name
    if command == "Create":
        file = open(f'{info[0]}', 'w')
        file.close()

    # If the command is 'Add', add the given text to the end of the file
    elif command == "Add":
        with open(f'{info[0]}', 'a') as file:
            file.write(f"{info[1]}\n")

    # If the command is 'Replace', replace all instances of the first parameter with the second in the file
    elif command == "Replace":
        try:
            # Open the file for reading
            with open(f'{info[0]}', 'r') as file:
                text = file.readlines()

            # Replace all instances of the first parameter with the second in the file
            for i in range(len(text)):
                text[i] = text[i].replace(info[1], info[2])

            # Open the file for writing and overwrite it with the updated text
            with open(f'{info[0]}', 'w') as file:
                file.write(''.join(text))
        except FileNotFoundError:
            # If the file is not found, print an error message
            print("An error occurred!")

    # If the command is 'Delete', delete the file with the given name
    elif command == "Delete":
        try:
            os.remove(f"{info[0]}")
        except FileNotFoundError:
            # If the file is not found, print an error message
            print("An error occurred!")
