"""Musician class for CP1404"""

class Musician:
    """Musician class to manage a musician's name and their instrument collection."""

    def __init__(self, name=""):
        """
        Initialize a Musician instance.

        :param name: str, name of the musician (default is an empty string)
        """
        self.name = name
        self.instruments = []

    def __str__(self):
        """
        Return a string representation of the Musician.

        :return: str, the musician's name and their instrument collection
        """
        instruments = ", ".join(str(instrument) for instrument in self.instruments) or "No instruments"
        return f"{self.name}: {instruments}"

    def __repr__(self):
        """
        Return a string representation for debugging purposes.

        :return: str, dictionary-like view of the musician's attributes
        """
        return f"Musician(name={self.name!r}, instruments={self.instruments!r})"

    def add_instrument(self, instrument):
        """
        Add an instrument to the musician's collection.

        :param instrument: Instrument to add (should be a Guitar or similar object)
        """
        self.instruments.append(instrument)

    def play(self):
        """
        Return a string showing the musician playing their first instrument (if available).

        :return: str, message indicating the instrument being played or a prompt to add an instrument
        """
        if not self.instruments:
            return f"{self.name} needs an instrument!"
        return f"{self.name} is playing: {self.instruments[0]}"

if __name__ == "__main__":
    from guitar import Guitar

    # Create a new musician
    musician = Musician()
    assert not musician.name  # Test initial name is empty
    assert not musician.instruments  # Test initial instrument list is empty

    # Assign a name and add instruments
    musician.name = "Lincoln Brewster"
    musician.add_instrument(Guitar("Fender Lincoln Brewster Stratocaster", 2020, 3419.0))
    musician.add_instrument(Guitar("Ernie Ball Music Man Silhouette Special", 1993, 2499.0))

    # Print details about the musician
    print(musician)  # Output should include the musician's name and instruments
    print(musician.play())  # Output should show the first instrument being played
