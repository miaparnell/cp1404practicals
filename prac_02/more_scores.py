"""
Program to get a number of scores, generate random scores, and print the category the score is in.
"""


import random


def main():
    """Generate random scores and print their category."""
    number_of_scores = int(input("Number of scores: "))
    for score in range(number_of_scores):
        score = random.randint(0, 100)
        print(f"{score} is {determine_score_category(score)}")


def determine_score_category(score):
    """Determine what category a score is in."""
    if score < 0 or score > 100:
        return "Invalid score"
    else:
        if score < 50:
            return "bad"
        elif score < 90:
            return "passable"
        else:
            return "excellent"


main()
