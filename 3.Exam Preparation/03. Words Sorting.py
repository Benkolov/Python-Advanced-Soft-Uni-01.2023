def words_sorting(*words):
    # create the dictionary with the sum of ASCII values of the words
    word_values = {w: sum(ord(c) for c in w) for w in words}

    # sort the dictionary by values in descending order if the sum is odd
    # or by keys in ascending order if the sum is even
    sorted_items = sorted(word_values.items(),
                          key=lambda x: (-x[1] if sum(word_values.values()) % 2 == 1 else x[0]))

    # return the sorted items as a string
    return "\n".join([f"{key} - {value}" for key, value in sorted_items])


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))

# print(
#     words_sorting(
#         'escape',
#         'charm',
#         'eye'
#   ))
#
# print(
#     words_sorting(
#         'cacophony',
#         'accolade'
#   ))


