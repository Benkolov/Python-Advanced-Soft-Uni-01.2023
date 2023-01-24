import re

n = int(input())

longest_intersection = []
length_longest_intersection = 0

for i in range(n):
    range1, range2 = input().split('-')

    start1, end1 = map(int, re.split(',', range1))
    start2, end2 = map(int, re.split(',', range2))

    intersection = [max(start1, start2), min(end1, end2)]

    if intersection[1] - intersection[0] + 1 > length_longest_intersection:
        longest_intersection = intersection
        length_longest_intersection = intersection[1] - intersection[0] + 1

print(f"Longest intersection is {[i for i in range(longest_intersection[0], longest_intersection[1] + 1)]} "
      f"with length {length_longest_intersection}")

