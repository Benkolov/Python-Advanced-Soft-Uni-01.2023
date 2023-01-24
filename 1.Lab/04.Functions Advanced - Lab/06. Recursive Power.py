def recursive_power(number, power):
    if power == 0:
        return 1
    return number * recursive_power(number, power - 1)


print(recursive_power(2, 10))
# print(recursive_power(10, 100))
# print(recursive_power(2, 3))
# print(recursive_power(5, 2))
# print(recursive_power(7, 4))
