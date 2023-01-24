n = int(input())

elements = set()

for i in range(n):
    compound = input().split()
    for element in compound:
        elements.add(element)

# for element in elements:
#     print(element)

print(*elements, sep='\n')
