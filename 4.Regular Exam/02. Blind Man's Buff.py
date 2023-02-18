n, m = map(int, input().split())
playground = []
for i in range(n):
    playground.append(input().split())

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

    new_x, new_y = x, y
    if command == 'up':
        new_x -= 1
    elif command == 'down':
        new_x += 1
    elif command == 'left':
        new_y -= 1
    elif command == 'right':
        new_y += 1

    if not (0 <= new_x < n and 0 <= new_y < m):
        continue

    if playground[new_x][new_y] == 'O':
        continue

    if playground[new_x][new_y] == 'P':
        touched += 1
        playground[new_x][new_y] = '-'

    x, y = new_x, new_y
    moves += 1

    if touched == 3:
        break

print("Game over!")
print(f"Touched opponents: {touched} Moves made: {moves}")
