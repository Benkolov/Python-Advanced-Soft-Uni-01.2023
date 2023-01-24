s = input()

stack = []
for c in s:
    if c in '([{':
        stack.append(c)
    elif c in ')]}':
        if not stack:
            print('NO')
            break
        if c == ')' and stack[-1] != '(':
            print('NO')
            break
        if c == ']' and stack[-1] != '[':
            print('NO')
            break
        if c == '}' and stack[-1] != '{':
            print('NO')
            break
        stack.pop()
else:
    if not stack:
        print('YES')
    else:
        print('NO')
