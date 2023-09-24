"""
Program to get the user to enter a valid password and print stars according to the length
"""


MINIMUM_LENGTH = 8


def main():
    """Get a password and print a sequence of stars"""
    password = input("Password: ")
    password = get_password(password)
    print_stars(password)


def get_password(password):
    """Determine if a password is valid."""
    while len(password) < MINIMUM_LENGTH:
        print("Password too short")
        password = input("Password: ")
    return password


def print_stars(password):
    """Print stars for the length of a password."""
    for i in range(len(password)):
        print("*", end='')


main()
