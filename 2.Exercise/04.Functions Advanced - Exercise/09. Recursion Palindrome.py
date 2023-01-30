# 1.

def palindrome(word, left_index, right_index=-1):
    if left_index == len(word) // 2:
        return f"{word} is a palindrome"

    if word[left_index] != word[right_index]:
        return f"{word} is not a palindrome"

    return palindrome(word, left_index + 1, right_index - 1)


# 2.

# def palindrome(word, index):
#     if index >= len(word) // 2:
#         return f"{word} is a palindrome"
#     if word[index] != word[-index-1]:
#         return f"{word} is not a palindrome"
#     return palindrome(word, index+1)


# 3.

# def palindrome(word, idx):
#     if idx >= len(word) // 2:
#         return f"{word} is a palindrome"
#
#     left = word[idx]
#     right = word[-1 - idx]
#
#     if left != right:
#         return f"{word} is not a palindrome"
#
#     return palindrome(word, idx + 1)


print(palindrome("abcba", 0))
print(palindrome("peter", 0))
