number = int(input())

unique_names = set()

for i in range(number):
    name = input()
    unique_names.add(name)

for name in unique_names:
    print(name)
