from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Represent a SilverServiceTaxi object."""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Inisialise a SilverServiceTaxi instance."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def get_fare(self):
        """Get the current fare."""
        return self.flagfall + super().get_fare()

    def __str__(self):
        """Return a string representation of a SilverServiceTaxi object."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

