def calculate_position(ma, row, col):
    if row < 0:
        row = len(ma) - 1
    if col < 0:
        col = len(ma) - 1
    if row >= len(ma):
        row = 0
    if col >= len(ma):
        col = 0
    return row, col


n = int(input())

matrix = []
player_position = []

for row_index in range(n):
    row_data = input().split()
    if 'P' in row_data:
        player_position = [row_index, row_data.index('P')]
    matrix.append(row_data)

player_path = []
player_path.append(player_position)

while True:
    command = input()
    current_row, current_col = player_position
    if command == 'up':
        rol, col = calculate_position(matrix, current_row-1, current_col)
    elif command == 'down':
        rol, col = calculate_position(matrix, current_row+1, current_col)
    elif command == 'right':
        rol, col = calculate_position(matrix, current_row, current_col+1)
    elif command == 'left':
        rol, col = calculate_position(matrix, current_row, current_col-1)



