rows, columns = input().split(', ')

matrix = []
matrix_sum = 0
for row in range(int(rows)):
    matrix.append([])
    data = [int(x) for x in input().split(", ")]
    for column in range(int(columns)):
        matrix[row].append(data[column])
        matrix_sum += data[column]

print(matrix_sum)
print(matrix)