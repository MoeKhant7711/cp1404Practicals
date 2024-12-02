from datetime import datetime

class Project:
    def __init__(self, name, start_date, priority=0, cost_estimate=0.0, completion_percentage=0):
        """Initialize a project with the given values."""
        self.name = name
        self.start_date = start_date if isinstance(start_date, datetime) else datetime.strptime(start_date, '%d/%m/%Y')
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return a string representation for user-friendly display."""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:.2f}, "
                f"completion: {self.completion_percentage}%")

    def __repr__(self):
        """Return a string representation for debugging purposes."""
        return (f"Project({self.name!r}, {self.start_date!r}, priority={self.priority}, "
                f"estimate=${self.cost_estimate:.2f}, completion={self.completion_percentage}%)")

    def __lt__(self, other):
        """Compare projects based on priority for sorting."""
        return self.priority < other.priority
