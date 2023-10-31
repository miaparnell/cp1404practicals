"""
CP1404 Prac 06
Mia Parnell
Estimated time to complete: 45 minutes
Actual time: 35 minutes
"""


class ProgrammingLanguage:
    """Define a ProgrammingLanguage class."""
    def __init__(self, name, typing, reflection, year):
        """Define different pieces of information about the languages."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determine if a language is dynamically typed."""
        return self.typing == "Dynamic"

    def __str__(self):
        """Format information about the languages."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
