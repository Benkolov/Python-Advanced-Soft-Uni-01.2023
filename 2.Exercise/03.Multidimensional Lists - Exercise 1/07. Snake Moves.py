# 1.

rows, columns = [int(x) for x in input().split()]
word = input()
index = 0
for row in range(rows):
    elements = [None] * columns
    start, end, step = (0, columns, 1) if row % 2 == 0 else (columns - 1, -1, -1)

    for col in range(start, end, step):
        elements[col] = word[index % len(word)]
        index += 1

    print(''.join(elements))

# 2.

from collections import deque

rows, cols = [int(x) for x in input().split()]
word = list(input())

word_copy = deque(word)

for row in range(rows):
    while len(word_copy) < cols:
        word_copy.extend(word)

    if row % 2 == 0:
        print(*[word_copy.popleft() for _ in range(cols)], sep="")
    else:
        print(*[word_copy.popleft() for _ in range(cols)][::-1], sep="")
