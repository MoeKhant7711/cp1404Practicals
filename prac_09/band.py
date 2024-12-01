class Band:
    def __init__(self, band=""):
        """Initialise instance"""
        self.band = band
        self.musicians = []

    def __str__(self):
        """Return string representation"""
        return f"{self.band}({self.musicians})"

    def __repr__(self):
        """Return a string"""
        return str(self)

    def add(self, musician):
        """Add musician"""
        return self.musicians.append(musician)

    def play(self):
        """Let each musician play their instruments"""
        return "\n".join([musician.play() for musician in self.musicians])
