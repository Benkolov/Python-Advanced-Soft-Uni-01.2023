from module import mathematical_operation

try:
    data = mathematical_operation(*input('Please enter first number, operator, second number: ') .split(' '))
    print(f"Result is: {data}")
except ValueError:
    print("Enter a valid date!")
