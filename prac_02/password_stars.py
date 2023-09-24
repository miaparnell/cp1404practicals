MINIMUM_LENGTH = 8


def main():
    password = input("Password: ")
    password = get_password(password)
    print_stars(password)


def get_password(password):
    while len(password) < MINIMUM_LENGTH:
        print("Password too short")
        password = input("Password: ")
    return password


def print_stars(password):
    for i in range(len(password)):
        print("*", end='')


main()
