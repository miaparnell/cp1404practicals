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