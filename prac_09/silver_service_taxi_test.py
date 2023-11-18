from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Test the SilverServiceTaxi class to ensure it works properly."""
    my_taxi = SilverServiceTaxi("Taxi 1", 100, 2)
    my_taxi.drive(18)
    print(my_taxi)
    print(f"Fare (rounded) is ${my_taxi.get_fare():.2f}")


main()
