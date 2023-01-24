numbers = input().split()

counts = {}

for number in numbers:
    number = round(float(number), 1)
    if number in counts:
        counts[number] += 1
    else:
        counts[number] = 1

for number, count in counts.items():
    print(f"{number} - {count} times")
