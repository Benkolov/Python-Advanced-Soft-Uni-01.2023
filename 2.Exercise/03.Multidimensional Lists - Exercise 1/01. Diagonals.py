# 1.

matrix = [[int(x) for x in input().split(", ")] for _ in range(int(input()))]

primary_diagonal = [matrix[i][i] for i in range(len(matrix))]

secondary_diagonal = [matrix[i][len(matrix) - i - 1] for i in range(len(matrix))]

print(f"Primary diagonal: {', '.join(map(str, primary_diagonal))}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(map(str, secondary_diagonal))}. Sum: {sum(secondary_diagonal)}")


# 2.

size = int(input())

matrix = []
for i in range(size):
    matrix.append([int(x) for x in input().split(", ")])

primary = []
secondary = []
for idx in range(size):
    primary.append(matrix[idx][idx])
    secondary.append(matrix[idx][size - 1 - idx])

print(f"Primary diagonal: {', '.join([str(x) for x in primary])}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary)}. Sum: {sum(secondary)}")


# 3.

n = int(input())

matrix = [[int(el) for el in input().split(',')] for _ in range(n)]
primary = [matrix[r][r] for r in range(n)]
secondary = [matrix[r][n - r - 1] for r in range(n - 1, -1, -1)]

print(f"Primary diagonal: {', '.join([str(x) for x in primary])}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary][::-1])}. Sum: {sum(secondary)}")
