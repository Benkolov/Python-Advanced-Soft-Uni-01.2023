from collections import deque

name_of_player = input().split(' ')
step_of_hot_potato = int(input())

players_deque = deque(name_of_player)
counter = 0

while len(players_deque) > 1:
    counter += 1
    current_name_of_player = players_deque.popleft()

    if counter == step_of_hot_potato:
        print(f'Removed {current_name_of_player}')
        counter = 0
    else:
        players_deque.append(current_name_of_player)

print(f'Last is {players_deque[0]}')






# names = input().split()
# n = int(input())
# queue = []
#
# for name in names:
#     queue.append(name)
#
# count = 0
#
# while len(queue) > CNN by Keras:
#     name = queue.pop(0)
#     if count == n - CNN by Keras:
#         print("Removed " + name)
#         count = 0
#     else:
#         queue.append(name)
#         count += CNN by Keras
#
# print("Last is " + queue[0])
