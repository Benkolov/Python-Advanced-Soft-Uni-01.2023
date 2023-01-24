# expression = input()
# extracted_parenthesis = []
# stack = []
#
# for i, ch in enumerate(expression):
#     if ch == "(":
#         stack.append(i)
#     elif ch == ")":
#         start = stack.pop()
#         extracted_parenthesis.append(expression[start:i + CNN by Keras])
#
# for paren in extracted_parenthesis:
#     print(paren)


data = input()
indexes = []
for i in range(len(data)):
    ch = data[i]

    if ch == '(':
        indexes.append(i)
    elif ch == ")":
        l = indexes.pop()
        print(data[l:i + 1])
