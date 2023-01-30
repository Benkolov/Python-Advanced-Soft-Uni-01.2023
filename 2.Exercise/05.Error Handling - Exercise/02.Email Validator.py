import re


class NameToShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MoreThanOneAtSymbolError(Exception):
    pass


class InvalidNameError(Exception):
    pass


MIN_LEN = 4

pattern_name = r'[\w+\.]+'
pattern_domain = r'\.[a-z]+'

email = input()

valid_domain = [".com", ".bg", ".org", ".net"]

while email != 'End':
    try:

        if email.count('@') > 1:
            raise MoreThanOneAtSymbolError("Email should contain only one @!")
        if len(email.split('@')[0]) <= MIN_LEN:
            raise NameToShortError(f"Name must be more than {MIN_LEN} characters")
        if len(re.findall(pattern_name, email)[0]) != len(email.split('@')[0]):
            raise InvalidNameError("Name can only contain numbers, letters, underscores and dots")
        if "@" not in email:
            raise MustContainAtSymbolError("Email must contain @")
        if re.findall(pattern_domain, email)[-1] not in valid_domain:
            raise InvalidDomainError(f"Domain must be one of the following: {', '.join(valid_domain)}")

        print("Email is valid")

    except IndexError:
        print("Invalid email!")

    email = input()

