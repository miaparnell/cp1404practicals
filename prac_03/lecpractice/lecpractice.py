FILENAME = "secret.txt"


def main():
    secret = load_number(FILENAME)
    is_valid_input = False
    guess = get_valid_number(is_valid_input)
    while guess != secret:
        print("Guess again!")
        guess = int(input("Guess: "))
    print("You got it")


def get_valid_number(is_valid_input):
    while not is_valid_input:
        try:
            guess = int(input("Guess: "))
            is_valid_input = True
        except ValueError:
            print("Invalid integer")
    return guess


def load_number(filename):
    """Load integer from file"""
    try:
        infile = open(filename, "r")
        number = int(infile.read())
    except ValueError:
        print(f"Invalid contents in {filename}")
        number = 6
    except FileNotFoundError:
        print(f"{filename} not found")
        number = 4
    else:
        infile.close()
    return number


# main()

# with open("dataex.txt", "r") as in_file:
#     in_file.readline() # makes this ignore header
#     for line in in_file:
#         # print(line)
#         parts = line.strip().split(',')
#         name = parts[0]
#         age = int(parts[1])
#         # print(parts)
#         # print(parts[0], "is", parts[1], "years old")
#         print(f"{name} will be {age + 1} years old next year")

with open(".txt", "r") as in_file:
    for line in in_file:
        if line.startswith("#"):
            print(line)
