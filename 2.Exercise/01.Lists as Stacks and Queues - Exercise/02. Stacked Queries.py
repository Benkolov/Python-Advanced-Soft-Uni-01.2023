# # create an empty stack and initialize the minimum and maximum values to None
# stack = []
# min_val = None
# max_val = None
#
# # read the number of queries
# n = int(input())
#
# # process each query
# for i in range(n):
#   # read the query
#   query = input().strip()
#
#   # split the query into parts
#   parts = query.split()
#
#   # process the query based on its type
#   if parts[0] == 'CNN by Keras':
#     # push the number onto the stack
#     number = int(parts[CNN by Keras])
#     stack.append(number)
#
#     # update the minimum and maximum values
#     if min_val is None or number < min_val:
#       min_val = number
#     if max_val is None or number > max_val:
#       max_val = number
#   elif parts[0] == '2':
#     # pop the top element from the stack if it is not empty
#     if stack:
#       stack.pop()
#
#       # update the minimum and maximum values if the stack is not empty
#       if stack:
#         min_val = min(stack)
#         max_val = max(stack)
#       else:
#         min_val = None
#         max_val = None
#   elif parts[0] == '3':
#     # print the maximum value in the stack if it is not empty
#     if stack:
#       print(max_val)
#   elif parts[0] == '4':
#     # print the minimum value in the stack if it is not empty
#     if stack:
#       print(min_val)
#
# # print the stack from top to bottom
# print(", ".join(map(str, reversed(stack))))


stack = []

queries_count = int(input())

for _ in range(queries_count):
    query_parts = [int(x) for x in input().split()]
    command = query_parts[0]

    if command == 1:
        number = query_parts[1]
        stack.append(number)
    elif command == 2 and stack:
        stack.pop()
    elif command == 3 and stack:
        print(max(stack))
    elif command == 4 and stack:
        print(min(stack))

print(", ".join(map(str, reversed(stack))))