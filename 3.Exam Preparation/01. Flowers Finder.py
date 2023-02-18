from collections import deque

vowels = deque(input().split())
consonants = deque(input().split())

words = {
    "rose": ['r', 'o', 's', 'e'],
    "tulip": ['t', 'u', 'l', 'i', 'p'],
    "lotus": ['l', 'o', 't', 'u', 's'],
    "daffodil": ['d', 'a', 'f', 'f', 'o', 'd', 'i', 'l'],
}
result = False
while vowels and consonants:
    if result:
        break
    vowel = vowels.popleft()
    consonant = consonants.pop()

    for key, value in words.items():
        if vowel in value:
            while vowel in value:
                value.remove(vowel)
        if consonant in value:
            while consonant in value:
                value.remove(consonant)
        if len(value) == 0:
            print(f"Word found: {key}")
            result = True
            break

if not result:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")

if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
