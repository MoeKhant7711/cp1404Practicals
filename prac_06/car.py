"""CP1404 Practical - Car class example."""


class Car:
    """Represent a Car object."""

    def __init__(self, name, fuel=0):
        """Initialise a Car instance.

        name: string, the name of the car
        fuel: int, the amount of fuel the car starts with (one unit of fuel drives one kilometre)
        """
        self.name = name
        self.fuel = fuel  # fuel should be an integer or float depending on requirements
        self._odometer = 0

    def add_fuel(self, amount):
        """Add amount to the car's fuel."""
        self.fuel += amount

    def drive(self, distance):
        """Drive the car a given distance.

        Drive the given distance if the car has enough fuel,
        or drive until the fuel runs out.
        Return the distance actually driven.
        """
        if distance > self.fuel:
            distance = self.fuel  # The car can't drive more than the available fuel allows
            self.fuel = 0  # Fuel is depleted after driving as far as possible
        else:
            self.fuel -= distance  # Reduce fuel by the distance driven
        self._odometer += distance  # Increase the odometer by the distance driven
        return distance

    def __str__(self):
        """Return a string representation of the car, showing name, fuel, and odometer."""
        return f"{self.name}, fuel={self.fuel}, odometer={self._odometer}"
