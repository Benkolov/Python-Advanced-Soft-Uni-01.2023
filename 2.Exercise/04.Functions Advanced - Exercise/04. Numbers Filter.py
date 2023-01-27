# 1.

def even_odd_filter(**numbers):
    if 'odd' in numbers:
        numbers['odd'] = [n for n in numbers['odd'] if n % 2 == 1]

    if 'even' in numbers:
        numbers['even'] = list(filter(lambda x: x % 2 == 0, numbers['even']))

    return dict(sorted(numbers.items(), key=lambda x: -len(x[1])))

# 2.

# def even_odd_filter(**kwargs):
#     filtered_lists = {}
#     for key, values in kwargs.items():
#
#         if key == "even":
#             filtered_num = [x for x in values if x % 2 == 0]
#         elif key == "odd":
#             filtered_num = [x for x in values if x % 2 == 1]
#
#         filtered_lists[key] = filtered_num
#
#     return {k: v for k, v in sorted(filtered_lists.items(), reverse=False)}


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))

print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))

