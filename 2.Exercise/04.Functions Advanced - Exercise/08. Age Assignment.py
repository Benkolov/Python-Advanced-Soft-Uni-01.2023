# 1.

def age_assignment(*names, **data):
    result = []
    for letter, age in data.items():
        person_name = ''
        for name in names:
            if name.startswith(letter):
                person_name = name
                break
        result.append(f"{person_name} is {age} years old.")
    return "\n".join(sorted(result))

# 2.

# def age_assignment(*args, **kwargs):
#     result = {}
#
#     for name in args:
#         first_letter = name[0]
#         age = kwargs[first_letter]
#         result[name] = age
#
#     sorted_result = [f'{key} is {value} years old.' for key, value in sorted(result.items(), key=lambda x: x[0])]
#     return '\n'.join(sorted_result)


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
