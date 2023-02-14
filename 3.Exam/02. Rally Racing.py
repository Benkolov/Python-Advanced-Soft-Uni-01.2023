size = int(input())
car_number = input()

matrix = []
car_pos = [0, 0]
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

distance = 0

for _ in range(size):
    line = list(input().split())
    matrix.append(line)

up_tunel_coordinates, down_tunel_coordinates = [(i, matrix[i].index('T')) for i in range(len(matrix)) if 'T' in matrix[i]]


while True:
    command = input()
    if command == "End":
        print(f"Racing car {car_number} DNF.")
        break

    row = directions[command][0] + car_pos[0]
    col = directions[command][1] + car_pos[1]
    car_pos = [row, col]

    if matrix[row][col] == 'T':
        matrix[row][col] = '.'
        distance += 30
        if tuple(car_pos) == up_tunel_coordinates:
            matrix[down_tunel_coordinates[0]][down_tunel_coordinates[1]] = '.'
            car_pos = [down_tunel_coordinates[0], down_tunel_coordinates[1]]
        else:
            matrix[up_tunel_coordinates[0]][up_tunel_coordinates[1]] = '.'
            car_pos = [up_tunel_coordinates[0], up_tunel_coordinates[1]]
    elif matrix[row][col] == 'F':
        distance += 10

        print(f"Racing car {car_number} finished the stage!")
        break
    else:
        distance += 10

matrix[car_pos[0]][car_pos[1]] = 'C'
print(f"Distance covered {distance} km.")
for line in matrix:
    print(''.join(line))
