"""
CP1404 Prac_06 - guitar.py
Mia Parnell
Estimated time: 35 minutes
Actual time: 40 minutes
"""

CURRENT_YEAR = 2023


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        """Define information about the Guitar class."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Format information about guitars."""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def get_age(self):
        """Determine the age of a guitar."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if a guitar is vintage."""
        return self.get_age() >= 50