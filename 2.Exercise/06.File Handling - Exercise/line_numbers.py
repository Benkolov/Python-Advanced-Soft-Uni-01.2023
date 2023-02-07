from string import punctuation

# Open the text file and read its lines as a list
with open("text.txt") as text_file:
    text = text_file.readlines()

# Open a new file for writing the output
output_file = open('output.txt', 'w')

# Loop through all the lines of the text
for i in range(len(text)):
    row = text[i]

    # Initialize variables to keep track of the number of letters and punctuation marks
    letters = 0
    marks = 0

    # Loop through each symbol in the row
    for symbol in row:
        # If the symbol is an alphabetic character, increase the letter count
        if symbol.isalpha():
            letters += 1
        # If the symbol is a punctuation mark, increase the marks count
        elif symbol in punctuation:
            marks += 1

    # Write the line number, the line without the trailing newline character, and the count of letters and marks to
    # the output file
    output_file.write(f"Line {i + 1}: {''.join(row[:-1])} ({letters})({marks})\n")

# Close the output file
output_file.close()
