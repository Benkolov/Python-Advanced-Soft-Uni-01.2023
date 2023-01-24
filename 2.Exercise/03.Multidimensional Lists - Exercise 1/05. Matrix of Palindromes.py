# 1.

# r, c = map(int, input().split())
# matrix = []
# for i in range(r):
#     row = []
#     first = chr(ord('a') + i)
#     last = first
#
#     for j in range(c):
#         middle = chr(ord('a') + i + j)
#         palindrome = first + middle + last
#         row.append(palindrome)
#
#     matrix.append(row)
#
# for row in matrix:
#     print(' '.join(row))


# 2.

rows, cols = map(int, input().split())

start_end = ord('a')

for row in range(start_end, start_end + rows):
    for col in range(start_end, start_end + cols):
        print(f"{chr(row)}{chr(row + col - start_end)}{chr(row)}", end=" ")

    print()