from icecream import ic


# text = input()
#
# rev = reversed(text)
# reversed_text = "".join(rev)
#
# print(reversed_text)

text = list(input())

while len(text) > 0:
    element = text.pop()
    print(element, end="")
