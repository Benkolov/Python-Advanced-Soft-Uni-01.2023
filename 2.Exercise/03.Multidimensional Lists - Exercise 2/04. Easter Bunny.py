size = int(input())

matrix = []
bunny_pos = []
best_path = []

best_direction = None
eggs = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(size):
    line = input().split()
    matrix.append(line)

    if 'B' in line:
        bunny_pos = [row, line.index('B')]

for direction, position in directions.items():
    row, col = [
        bunny_pos[0] + position[0],
        bunny_pos[1] + position[1],
    ]
    path = []
    collected_eggs = 0

    while 0 <= row < size and 0 <= col < size:
        if matrix[row][col] == 'X':
            break

        collected_eggs += int(matrix[row][col])
        path.append([row, col])

        row += position[0]
        col += position[1]

    if collected_eggs >= eggs:
        eggs = collected_eggs
        best_direction = direction
        best_path = path


print(best_direction)
print(*best_path, sep='\n')
print(eggs)

