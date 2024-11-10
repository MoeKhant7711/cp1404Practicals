CURRENT_YEAR = 2024
VINTAGE_THRESHOLD = 50  


class Guitar:
    """Class to represent a guitar with a name, year, and cost."""
    
    def __init__(self, name="", year=0, cost=0):
        """Initialize a Guitar with a name, year, and cost."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the guitar for user-friendly display."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Calculate and return the age of the guitar based on the current year."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if the guitar is considered vintage (50+ years old)."""
        return self.get_age() >= VINTAGE_THRESHOLD

    def __lt__(self, other):
        """Less-than comparison based on the guitar's year (older guitars come first)."""
        return self.year < other.year
