first_seq = set(map(int, input().split()))
second_seq = set(map(int, input().split()))
num = int(input())

for i in range(num):
    command, number_seq, *seq = input().split()
    data = set(map(int, seq))
    if command == "Add":
        if number_seq == "First":
            first_seq = first_seq.union(data)
        elif number_seq == "Second":
            second_seq = second_seq.union(data)
    elif command == "Remove":
        if number_seq == "First":
            first_seq = first_seq.difference(data)
        elif number_seq == "Second":
            second_seq = second_seq.difference(data)
    elif command == "Check":
        print(first_seq.issubset(second_seq) or second_seq.issubset(first_seq))

print(*sorted(first_seq), sep=", ")
print(*sorted(second_seq), sep=", ")

