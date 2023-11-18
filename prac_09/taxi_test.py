from prac_09.car import Car

from prac_09.taxi import Taxi


def main():
    """Test taxis to ensure the Taxi class is working."""
    my_taxi = Taxi("Prius 1", 100)
    my_taxi.drive(40)
    print(my_taxi)
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(my_taxi)


main()
