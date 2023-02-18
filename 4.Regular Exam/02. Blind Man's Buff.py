n, m = map(int, input().split())
playground = []
for i in range(n):
    playground.append(input().split())

# Find the initial position of the blindfolded player
x, y = None, None
for i in range(n):
    for j in range(m):
        if playground[i][j] == 'B':
            x, y = i, j
            break
    if x is not None:
        break

moves = 0
touched = 0
while True:
    command = input()
    if command == 'Finish':
        break

    # Calculate the new position based on the command
    new_x, new_y = x, y
    if command == 'up':
        new_x -= 1
    elif command == 'down':
        new_x += 1
    elif command == 'left':
        new_y -= 1
    elif command == 'right':
        new_y += 1

    # Check if the new position is inside the playground
    if not (0 <= new_x < n and 0 <= new_y < m):
        continue

    # Check if the new position is an obstacle
    if playground[new_x][new_y] == 'O':
        continue

    # Check if the new position is an opponent
    if playground[new_x][new_y] == 'P':
        touched += 1
        playground[new_x][new_y] = '-'

    # Update the position of the blindfolded player
    x, y = new_x, new_y
    moves += 1

    # Check if all opponents have been touched
    if touched == 3:
        break

# Print the game report
print("Game over!")
print(f"Touched opponents: {touched} Moves made: {moves}")
