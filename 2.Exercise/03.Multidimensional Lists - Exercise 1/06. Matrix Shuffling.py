# 1.

def is_outside(row, col, rows, cols):
    return row < 0 or col < 0 or row >= rows or col >= cols


rows, cols = [int(x) for x in input().split()]

matrix = []

for i in range(rows):
    matrix.append([x for x in input().split()])

while True:
    line = input()
    if line == "END":
        break
    line_parts = line.split()

    if len(line_parts) != 5 or line_parts[0] != "swap":
        print("Invalid input!")
        continue

    row1, col1, row2, col2 = [int(x) for x in line_parts[1:]]

    if is_outside(row1, col1, rows, cols) or is_outside(row2, col2, rows, cols):
        print("Invalid input!")
        continue

    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

    for row in matrix:
        print(*row, sep=" ")


# 2.

def check_valid_indexes(indexes):
    if set(indexes[:2]).issubset(valid_rows) and set(indexes[2:]).issubset(valid_cols):
        return True

    return False


def swap_command(command, indexes):
    if check_valid_indexes(indexes) and command == "swap" and len(indexes) == 4:
        row1, col1, row2, col2 = indexes

        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

        print(*[' '.join(matrix[r])for r in range(rows)], sep='\n')
    else:
        print("Invalid input!")


rows, cols = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]

valid_rows = range(rows)
valid_cols = range(cols)

while True:
    command_type, *info = [int(x) if x.isdigit() else x for x in input().split()]

    if command_type == "END":
        break

    swap_command(command_type, info)
