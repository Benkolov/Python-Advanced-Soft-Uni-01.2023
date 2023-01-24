# 1.

size = int(input())

matrix = []
for i in range(size):
    matrix.append([int(x) for x in input().split()])

primary = []
secondary = []
for idx in range(size):
    primary.append(matrix[idx][idx])
    secondary.append(matrix[idx][size - 1 - idx])

primary_sum = sum(primary)
secondary_sum = sum(secondary)

print(abs(primary_sum - secondary_sum))


# 2.

n = int(input())

matrix = [[int(x) for x in input().split()] for i in range(n)]

primary, secondary = 0, 0

for i in range(n):
    primary += matrix[i][i]
    secondary += matrix[n - i - 1][i]

print(abs(primary - secondary))