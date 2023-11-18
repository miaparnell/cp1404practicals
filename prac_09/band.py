class Band:
    """Represent a Band object."""
    def __init__(self, name=""):
        """Initialize a Band instance."""
        self.name = name
        self.members = []

    def __str__(self):
        """Return a string representation of a Band object."""
        member_strings = [str(member) for member in self.members]
        return f"{self.name} ({', '.join(member_strings)})"

    def add(self, musician):
        """Add a musician to the band."""
        self.members.append(musician)

    def play(self):
        """Return a string showing each musician playing their first (or no) instrument."""
        play_strings = [member.play() for member in self.members]
        return '\n'.join(play_strings)


