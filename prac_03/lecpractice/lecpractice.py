FILENAME = "secret.txt"


# def main():
#     secret = load_number(FILENAME)
#     is_valid_input = False
#     guess = get_valid_number(is_valid_input)
#     while guess != secret:
#         print("Guess again!")
#         guess = int(input("Guess: "))
#     print("You got it")
#
#
# def get_valid_number(is_valid_input):
#     while not is_valid_input:
#         try:
#             guess = int(input("Guess: "))
#             is_valid_input = True
#         except ValueError:
#             print("Invalid integer")
#     return guess
#
#
# def load_number(filename):
#     """Load integer from file"""
#     try:
#         infile = open(filename, "r")
#         number = int(infile.read())
#     except ValueError:
#         print(f"Invalid contents in {filename}")
#         number = 6
#     except FileNotFoundError:
#         print(f"{filename} not found")
#         number = 4
#     else:
#         infile.close()
#     return number


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

# with open(".txt", "r") as in_file:
#     for line in in_file:
#         if line.startswith("#"):
#             print(line)

# names = ["Ada", "Alan", "Bill", "John"]


# things = [True, 1.2, "Good", [1, 10]]
# print(things[-2])
# print("%".join([things[2][1:-1]]))
# print([str(t)[0] for t in things])
# print([len(str(t)) for t in things])
# print([t for t in things if type(t) in (float, int)])
# print([t for t in things if isinstance(t, int)])


# def main():
#     numbers = [1, 4.5, 90, -2, 8, 2]
#     square_numbers(numbers)
#     print(numbers)
#     print("Hello")
#
#
# def square_numbers(numbers):
#     for i in range(len(numbers)):
#         numbers[i] = numbers[i] ** 2
#     return numbers
#
# main()

print("*".join([len(word) for word in "one*two*three".split('*')]))
