matrix = []
pos_rover = []
for i in range(6):
    line = input().split()
    matrix.append(line)

    if "E" in line:
        pos_rover = [i, line.index('E')]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

deposits = {
    'Water': 0,
    'Metal': 0,
    'Concrete': 0
}

commands = input().split(', ')

for command in commands:
    row = directions[command][0] + pos_rover[0]
    col = directions[command][1] + pos_rover[1]
    if row >= len(matrix):
        row -= len(matrix)
    if row < 0:
        row += len(matrix)
    if col >= len(matrix):
        col -= len(matrix)
    if col < 0:
        col += len(matrix)

    pos_rover = [row, col]
    if matrix[row][col] == 'W':
        deposits['Water'] += 1
        print(f"Water deposit found at ({row}, {col})")
    elif matrix[row][col] == 'M':
        deposits['Metal'] += 1
        print(f"Metal deposit found at ({row}, {col})")
    elif matrix[row][col] == 'C':
        deposits['Concrete'] += 1
        print(f"Concrete deposit found at ({row}, {col})")
    elif matrix[row][col] == 'R':
        print(f"Rover got broken at ({row}, {col})")
        break

is_suitable = True
for deposit, count in deposits.items():
    if count == 0:
        is_suitable = False

if is_suitable:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
