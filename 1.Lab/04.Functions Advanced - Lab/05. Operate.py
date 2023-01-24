def operate(operator, *args):
    result = args[0]
    for i in range(1, len(args)):
        if operator == "+":
            result += args[i]
        elif operator == "-":
            result -= args[i]
        elif operator == "*":
            result *= args[i]
        elif operator == "/":
            result /= args[i]
    return result


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
print(operate("+", 1, 2, 3, 4))
print(operate("-", 10, 5, 3, 1))
print(operate("*", 1, 2, 3, 4))
print(operate("/", 8, 2, 2))
