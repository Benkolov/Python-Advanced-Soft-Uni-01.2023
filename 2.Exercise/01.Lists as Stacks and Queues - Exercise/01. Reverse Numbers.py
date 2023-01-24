s = input()

numbers = list(map(int, s.split()))

stack = []

for number in numbers:
    stack.append(number)

reversed_numbers = []

while stack:
    reversed_numbers.append(stack.pop())

print(" ".join(map(str, reversed_numbers)))