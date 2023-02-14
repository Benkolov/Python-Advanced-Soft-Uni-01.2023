player1, player2 = input().split(", ")
board = [[int(x) if x.isdigit() else x for x in input().split()] for i in range(7)]
score1 = 501
score2 = 501
turn = 1
is_win = False

while True:
    get_coordinate = input()
    list_coordinate = get_coordinate[1:-1].split(', ')
    row, col = [int(x) for x in list_coordinate]

    if row >= 7 or col >= 7:
        turn += 1
        continue

    hit = board[row][col]

    if hit == 'B':
        is_win = True
        if turn % 2 == 1:
            print(f"{player1} won the game with {(turn + 1) // 2} throws!")
        else:
            print(f"{player2} won the game with {turn // 2} throws!")
        break
    elif hit == "D":
        score = 2 * (board[row][0] + board[row][6] + board[0][col] + board[6][col])
        if turn % 2 == 1:
            score1 -= score
        else:
            score2 -= score
        turn += 1
    elif hit == "T":
        score = 3 * (board[row][0] + board[row][6] + board[0][col] + board[6][col])
        if turn % 2 == 1:
            score1 -= score
        else:
            score2 -= score
        turn += 1
    else:
        score = hit
        if turn % 2 == 1:
            score1 -= score
        else:
            score2 -= score
        turn += 1

    if score1 <= 0:
        print(f"{player1} won the game with {(turn + 1) // 2} throws!")
        break
    elif score2 <= 0:
        print(f"{player2} won the game with {turn // 2} throws!")
        break