MENU = """
(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""


def main():
    score = get_valid_score("Score: ", 0, 100)
    print(MENU)
    choice = input("Choice: ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score("Score: ", 0, 100)
        elif choice == "P":
            print(determine_score_category(score))
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid input")
        print(MENU)
        choice = input("Choice: ").upper()
    print("Goodbye!")


def get_valid_score(prompt, low, high):
    score = int(input(prompt))
    while score < low or score > high:
        print("Invalid input")
        score = int(input(prompt))
    return score


def determine_score_category(score):
    """Determine what category a score is in."""
    if score < 0 or score > 100:
        return "Invalid score"
    else:
        if score < 50:
            return "Your score is bad"
        elif score < 90:
            return "You passed"
        else:
            return "You did excellent!"


def print_stars(score):
    for i in range(score):
        print("*", end='')


main()
