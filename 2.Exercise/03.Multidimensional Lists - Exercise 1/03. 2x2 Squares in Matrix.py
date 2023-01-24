# 1.

rows, cols = [int(x) for x in input().split()]

matrix = []

for _ in range(rows):
    matrix.append(input().split())


squares = 0

for row in range(rows - 1):
    for col in range(cols - 1):
        if matrix[row][col] == matrix[row][col + 1] == matrix[row + 1][col] == matrix[row + 1][col + 1]:
            squares += 1

print(squares)


# 2.

rows, cols = [int(x) for x in input().split()]
matrix = [input().split() for x in range(rows)]

equal_block = 0

for row in range(rows - 1):
    for col in range(cols - 1):
        symbol = matrix[row][col]

        if matrix[row][col + 1] == symbol and matrix[row + 1][col] == symbol and matrix[row + 1][col + 1] == symbol:
            equal_block += 1

print(equal_block)