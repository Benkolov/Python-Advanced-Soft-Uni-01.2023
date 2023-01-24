n, m = map(int, input().split())

set1 = set()
set2 = set()

for i in range(n):
    set1.add(int(input()))
for i in range(m):
    set2.add(int(input()))

common = set1.intersection(set2)
for element in common:
    print(element)


