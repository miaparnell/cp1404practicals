from prac_09.unreliable_car import UnreliableCar


def main():
    """Test several cars to ensure the UnreliableCar class works properly."""
    reliable_car = UnreliableCar("Reliable", 100, 95)
    unreliable_car = UnreliableCar("Unreliable", 100, 5)

    for i in range(1, 10):
        print(f"Distance attempted: {i}km:")
        print(f"{reliable_car.name} drove {reliable_car.drive(i):2}km")
        print(f"{unreliable_car.name} drove {unreliable_car.drive(i):2}km")

    print(reliable_car)
    print(unreliable_car)


main()
