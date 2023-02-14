import pyfiglet


def print_art(msg):
    ascii_art = pyfiglet.figlet_format(msg)
    print(ascii_art)


text = input()
print_art(text)
