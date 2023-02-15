from collections import deque

seats = input().split(', ')
first_sequences = deque([int(x) for x in input().split(', ')])
second_sequences = deque([int(x) for x in input().split(', ')])

rotations = 0
taken_seats = []

while True:
    if rotations == 10:
        break
    if len(taken_seats) == 3:
        break

    first = first_sequences.popleft()
    second = second_sequences.pop()
    ascii_char = chr(first + second)
    comb1 = str(first) + ascii_char
    comb2 = str(second) + ascii_char
    if comb1 in taken_seats or comb2 in taken_seats:
        rotations += 1
        continue
    elif comb1 in seats:
        taken_seats.append(comb1)
        seats.remove(comb1)
    elif comb2 in seats:
        taken_seats.append(comb2)
        seats.remove(comb2)
    else:
        first_sequences.append(first)
        second_sequences.appendleft(second)

    rotations += 1


print(f"Seat matches: {', '.join(taken_seats)}")
print(f"Rotations count: {rotations}")
