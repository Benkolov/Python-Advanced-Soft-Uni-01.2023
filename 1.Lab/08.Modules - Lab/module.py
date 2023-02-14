import operator as op


def mathematical_operation(first_number, operator, second_number):
    first_number, second_number = int(first_number), int(second_number)
    valid_operators = {'+': op.add, '-': op.sub, '*': op.mul, '/': op.truediv, '^': op.xor}

    return valid_operators[operator](first_number, second_number)
