#  1.
def sum_negative():
    sum_of_numbers = 0

    for num in numbers:
        if num < 0:
            sum_of_numbers += num

    return sum_of_numbers


def sum_positive():
    sum_of_numbers = 0

    for num in numbers:
        if num > 0:
            sum_of_numbers += num

    return sum_of_numbers


def print_results(positive, negative):
    print(negative)
    print(positive)

    if positive > abs(negative):
        print("The positives are stronger than the negatives")
    else:
        print("The negatives are stronger than the positives")


numbers = [int(x) for x in input().split()]

positive_numbers = sum_positive()
negative_numbers = sum_negative()

print_results(positive_numbers, negative_numbers)


# 2.

# def negative(numbers):
#     a = [x for x in numbers if x < 0]
#     return sum(a)
#
#
# def positive(numbers):
#     b = [x for x in numbers if x > 0]
#     return sum(b)
#
#
# data = [int(x) for x in input().split()]
# print(negative(data))
# print(positive(data))
#
# if abs(negative(data)) > positive(data):
#     print("The negatives are stronger than the positives")
# else:
#     print("The positives are stronger than the negatives")

