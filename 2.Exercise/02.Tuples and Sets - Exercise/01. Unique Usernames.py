number = int(input())

unique_name = set()

for i in range(number):
    username = input()
    unique_name.add(username)

print("\n".join(unique_name))