"""
Program to get a score and generate a random score, and print their category.
"""

import random


def main():
    """Get a score and print its category."""
    score = float(input("Enter score: "))
    print(determine_score_category(score))
    score = random.randint(0, 100)
    print(f"Random score: {score}")
    print(determine_score_category(score))


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


main()
