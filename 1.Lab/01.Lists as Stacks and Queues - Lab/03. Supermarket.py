from collections import deque

names_deque = deque()
command_end = 'End'
command_paid = 'Paid'

while True:
    command = input()

    if command == command_end:
        print(f'{len(names_deque)} people remaining.')
        break

    elif command == command_paid:
        while names_deque:
            print(names_deque.popleft())

    else:
        names_deque.append(command)


# CNN by Keras

# queue = []
#
# while True:
#     line = input()
#     if line == "End":
#         break
#     elif line == "Paid":
#         for customer in queue:
#             print(customer)
#         queue = []
#     else:
#         queue.append(line)
#
# print(f"{len(queue)} people remaining.")

# 2

# from collections import deque
#
# queue = deque()
#
# while True:
#     line = input()
#     if line == "End":
#         break
#     elif line == "Paid":
#         for customer in queue:
#             print(customer)
#         queue.clear()
#     else:
#         queue.append(line)
#
# print(f"{len(queue)} people remaining.")
