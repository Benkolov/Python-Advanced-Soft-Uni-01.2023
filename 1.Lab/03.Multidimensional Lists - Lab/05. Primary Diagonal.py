size = int(input())

matrix = []

for i in range(size):
    matrix.append(list(map(int, input().split())))

diagonal_sum = 0

for i in range(size):
    diagonal_sum += matrix[i][i]

print(diagonal_sum)
