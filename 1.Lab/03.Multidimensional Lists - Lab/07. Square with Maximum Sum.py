dimensions = input().split(", ")
rows = int(dimensions[0])
columns = int(dimensions[1])

matrix = []

for i in range(rows):
    matrix.append(list(map(int, input().split(", "))))

max_sum = float("-inf")
max_sub_matrix = [[0, 0], [0, 0]]

for i in range(rows - 1):
    for j in range(columns - 1):
        sub_matrix = [[matrix[i][j], matrix[i][j + 1]], [matrix[i + 1][j], matrix[i + 1][j + 1]]]
        sub_matrix_sum = sum([sum(row) for row in sub_matrix])
        if sub_matrix_sum > max_sum:
            max_sum = sub_matrix_sum
            max_sub_matrix = sub_matrix


print("\n".join([" ".join(map(str, row)) for row in max_sub_matrix]))
print(max_sum)
