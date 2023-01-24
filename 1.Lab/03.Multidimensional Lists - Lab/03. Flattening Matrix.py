n = int(input())

flattening_matrix = []

for i in range(n):
    data = [int(x) for x in input().split(", ")]
    for k in data:
        flattening_matrix.append(k)

print(flattening_matrix)