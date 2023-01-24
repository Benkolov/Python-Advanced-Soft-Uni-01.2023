n = int(input())

odd_set = set()
even_set = set()

for i in range(1, n + 1):
    name = input()
    sum_ascii = sum(ord(ch) for ch in name) // i

    if sum_ascii % 2 == 0:
        even_set.add(sum_ascii)
    else:
        odd_set.add(sum_ascii)

sum_odd = sum(odd_set)
sum_even = sum(even_set)

if sum_odd == sum_even:
    result = odd_set.union(even_set)
elif sum_even > sum_odd:
    result = odd_set.symmetric_difference(even_set)
elif sum_odd > sum_even:
    result = odd_set.difference(even_set)

print(*result, sep=", ")

