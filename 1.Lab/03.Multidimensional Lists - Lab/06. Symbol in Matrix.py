size = int(input())

matrix = []

for i in range(size):
    matrix.append(list(input()))

symbol = input()


for i in range(size):
    for j in range(size):
        if matrix[i][j] == symbol:
            print(f"({i}, {j})")
            exit()

print(f"{symbol} does not occur in the matrix")
