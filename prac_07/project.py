class Project:
    def __init__(self, name="", start_date="", priority=0, cost_estimate=0, completion_percentage=0):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Format information about projects."""
        return f"{self.name}, start:{self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate}, completion: {self.completion_percentage}%"

    def is_complete(self):
        """Determine if a project is complete."""
        return self.completion_percentage == 100

    def is_not_complete(self):
        """Determine if a project is complete."""
        return self.completion_percentage != 100

    def __gt__(self, other):
        """Determine if a one data is past another date."""
        return self.start_date > other.start_date
