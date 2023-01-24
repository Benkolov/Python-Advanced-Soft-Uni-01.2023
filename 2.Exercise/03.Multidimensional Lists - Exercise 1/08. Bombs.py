# 1.

# def get_children(matrix, row, col):
#     possible_children_cords = [
#         [row - 1, col - 1],
#         [row - 1, col],
#         [row - 1, col + 1],
#         [row, col - 1],
#         [row, col + 1],
#         [row + 1, col - 1],
#         [row + 1, col],
#         [row + 1, col + 1],
#     ]
#
# result = [] for child_row, child_col in possible_children_cords: if 0 <= child_row < len(matrix) and 0 <= child_col
# < len(matrix[child_row]) and matrix[child_row][child_col] > 0: result.append([child_row, child_col]) return result
#
#
# size = int(input())
# matrix = []
#
# for _ in range(size):
#     matrix.append([int(x) for x in input().split()])
#
# bombs = input().split()
#
# for bomb in bombs:
#     row, col = [int(x) for x in bomb.split(',')]
#     power = matrix[row][col]
#
#     if power <= 0:
#         continue
#
#     matrix[row][col] = 0
#
#     children = get_children(matrix, row, col)
#     for child_row, child_col in children:
#         matrix[child_row][child_col] -= power
#
# alive_cells_count = 0
# alive_cells_sum = 0
#
# for row in matrix:
#     for el in row:
#         if el > 0:
#             alive_cells_count += 1
#             alive_cells_sum += el
#
# print(f"Alive cells: {alive_cells_count}")
# print(f"Sum: {alive_cells_sum}")
# for row in matrix:
#     print(*row, sep=" ")


# 2.


n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]
coordinates = ((int(x) for x in coordinate.split(",")) for coordinate in input().split())

directions = (
    (-1, 0),  # up
    (1, 0),   # down
    (0, 1),   # right
    (0, -1),  # left
    (-1, 1),  # top-right
    (-1, -1),  # top-left
    (1, -1),  # bottom-left
    (1, 1),  # bottom-right
    (0, 0),  # current
)

for row, col in coordinates:
    if matrix[row][col] <= 0:
        continue

    for x, y in directions:
        r, c = row + x, col + y

        if 0 <= r < n and 0 <= c < n:
            matrix[r][c] -= matrix[row][col] if matrix[r][c] > 0 else 0


alive_cells = [num for row in range(n) for num in matrix[row] if num > 0]
print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")
[print(*matrix[r], sep=" ") for r in range(n)]



