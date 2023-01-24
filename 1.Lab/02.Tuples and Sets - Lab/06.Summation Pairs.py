from itertools import combinations

# Read the list of numbers and the target number
numbers_str = input()
target = int(input())

# Convert the list of numbers to a set
numbers = set(map(int, numbers_str.split()))

# Initialize the set for the pairs
pairs = set()

# Find the pairs of numbers whose sum equals the target number
for pair in combinations(numbers, 2):
    if sum(pair) == target:
        pairs.add(pair)

# Print the number of pairs
print(f"Iterations done: {len(list(combinations(numbers, 2)))}")

# Print the pairs
for pair in pairs:
    print(pair)

