# 1.

def concatenate(*args, **kwargs):
    text = ''.join(args)

    for key in kwargs:
        text = text.replace(key, kwargs[key])

    return text


# 2.

# def concatenate(*args, **kwargs):
#     result = ""
#
#     for arg in args:
#         result += arg
#
#     for key, value in kwargs.items():
#         result = result.replace(key, value)
#     return result


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))

