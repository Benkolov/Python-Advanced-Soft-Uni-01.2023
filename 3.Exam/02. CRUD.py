matrix = []

for i in range(6):
    line = input().split()
    matrix.append(line)

position = list(map(int, input().strip("(").strip(")").split(", ")))

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

while True:
    command = input().split(', ')
    current_command = command[0]

    if current_command == "Stop":
        break

    direction = command[1]

    row = position[0] + directions[direction][0]
    col = position[1] + directions[direction][1]
    position = [row, col]

    if current_command == "Create":
        value = command[2]
        if matrix[row][col] == '.':
            matrix[row][col] = value
    elif current_command == "Update":
        value = command[2]
        if matrix[row][col] != '.':
            matrix[row][col] = value

    elif current_command == "Delete":
        if matrix[row][col] != '.':
            matrix[row][col] = '.'

    elif current_command == "Read":
        if matrix[row][col] != '.':
            print(matrix[row][col])


for line in matrix:
    print(*line, sep=" ")
