def repeat_text(current_text, current_number):
    return current_text * current_number


try:
    text = input()
    number = int(input())
    print(repeat_text(text, number))

except ValueError:
    print("Variable times must be an integer")
