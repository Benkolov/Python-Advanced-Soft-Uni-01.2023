players = input().split(', ')

matrix = []

for i in range(6):
    line = input().split()
    matrix.append(line)

turn = 0
rest = {
    'Tom': False,
    'Jerry': False
}
while True:
    row, col = eval(input())
    player = players[turn % 2]

    if not rest[player]:

        if matrix[row][col] == 'E':
            print(f"{player} found the Exit and wins the game!")
            break
        elif matrix[row][col] == 'T':
            if player == 'Tom':
                print(f"{player} is out of the game! The winner is Jerry.")
                break
            else:
                print(f"{player} is out of the game! The winner is Tom.")
                break
        elif matrix[row][col] == 'W':
            print(f"{player} hits a wall and needs to rest.")
            rest[player] = True
        turn += 1

    else:
        rest[player] = False
        turn += 1
