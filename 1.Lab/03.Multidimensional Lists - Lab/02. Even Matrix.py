n = int(input())
matrix = []

# for i in range(n):
#     matrix.append([])
#     data = [int(x) for x in input().split(", ")]
#     for k in data:
#         if k % 2 == 0:
#             matrix[i].append(k)
#
# print(matrix)

for _ in range(n):
    row = [int(x) for x in input().split(", ")]
    matrix.append(
        [x for x in row if x % 2 == 0]
    )

print(matrix)