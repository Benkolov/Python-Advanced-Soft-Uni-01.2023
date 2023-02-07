# Define a list of symbols to replace
symbols = ["-", ",", ".", "!", "?"]

# Open the text file and read its lines as a list
with open("text.txt") as eve_lines_file:
    text = eve_lines_file.read().splitlines()

# Loop through every other line of the text
for row in text[::2]:
    # Replace all symbols in the line with '@' using a translation table
    row = row.translate(str.maketrans("".join(symbols), "@" * len(symbols)))

    # Split the row into words, reverse the list, and print the words separated by spaces
    print(*row.split()[::-1], sep=" ")
    