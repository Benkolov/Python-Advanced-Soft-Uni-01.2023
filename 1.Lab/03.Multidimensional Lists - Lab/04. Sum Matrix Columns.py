dimensions = input().split(", ")
rows = int(dimensions[0])
columns = int(dimensions[1])

matrix = []

for i in range(rows):
    matrix.append(list(map(int, input().split())))

for j in range(columns):
    column_sum = 0
    for i in range(rows):
        column_sum += matrix[i][j]
    print(column_sum)

