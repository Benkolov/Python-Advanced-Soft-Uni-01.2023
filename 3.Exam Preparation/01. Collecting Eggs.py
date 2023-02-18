from collections import deque

eggs = deque([int(x) for x in input().split(', ')])
pieces_of_paper = deque([int(x) for x in input().split(', ')])
full_boxes = 0
while eggs and pieces_of_paper:
    egg = eggs.popleft()
    if egg <= 0:
        continue

    if egg == 13:
        l = pieces_of_paper.pop()
        f = pieces_of_paper.popleft()
        pieces_of_paper.appendleft(l)
        pieces_of_paper.append(f)
        continue

    paper = pieces_of_paper.pop()

    if egg + paper <= 50:
        full_boxes += 1

if full_boxes > 0:
    print(f"Great! You filled {full_boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    print(f"Eggs left: {', '.join(map(str, eggs))}")
if pieces_of_paper:
    print(f"Pieces of paper left: {', '.join(map(str, pieces_of_paper))}")
