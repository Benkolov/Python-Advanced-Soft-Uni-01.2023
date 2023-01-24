from collections import deque

food = int(input())

orders = list(map(int, input().split()))
queue = deque(orders)

largest_order = max(orders)

print(largest_order)

while queue:
    order = queue.popleft()
    if food >= order:
        food -= order
    else:
        queue.appendleft(order)
        break

if queue:
    print("Orders left:", " ".join(map(str, queue)))
else:
    print("Orders complete")
