text = input()

frequencies = {}

for ch in text:
    if ch in frequencies:
        frequencies[ch] += 1
    else:
        frequencies[ch] = 1

for ch, frequency in sorted(frequencies.items()):
    print(f"{ch}: {frequency} time/s")

# from collections import Counter
#
# text = input()
#
# frequencies = Counter(text)
#
# for ch, frequency in sorted(frequencies.items()):
#     print(f"{ch}: {frequency} time/s")