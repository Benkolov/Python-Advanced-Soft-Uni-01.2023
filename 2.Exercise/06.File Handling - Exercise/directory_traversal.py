import os

def save_extensions(dir_name, first_level=False):
    """This function saves all the extensions in a dictionary and returns the dictionary."""
    extensions = {}
    for filename in os.listdir(dir_name):
        file = os.path.join(dir_name, filename)

        if os.path.isfile(file):
            # Get the extension of the file
            extension = filename.split('.')[-1]

            # If the extension is not already in the dictionary, add it
            if extension not in extensions:
                extensions[extension] = []

            # Add the file to the list of files for this extension
            extensions[extension].append(filename)
        elif os.path.isdir(file) and not first_level:
            # If the file is a directory, call the function recursively on the directory
            save_extensions(file, first_level=True)
    return extensions


directory = input()
extensions = save_extensions(directory)
# Sort the extensions in the dictionary alphabetically by key
extensions = sorted(extensions.items(), key=lambda x: x[0])

result = []

# For each extension and its associated files, add them to the result list
for extension, files in extensions:
    result.append(f".{extension}")
    for file in sorted(files):
        result.append(f"---{file}")

# Write the result list to a file named 'report.txt'
with open('report.txt', 'w') as file:
    file.write('\n'.join(result))
