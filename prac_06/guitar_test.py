from prac_06.guitar import Guitar


def run_tests():
    """Test several arguments about guitars."""
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    second_guitar = Guitar("Second Guitar", 2000, 1000.50)
    third_guitar = Guitar("Third guitar", 1973, 1)
    print(gibson)
    print(second_guitar)

    print(f"{gibson.name} get_age() - Expected 101, got {gibson.get_age()}")
    print(f"{second_guitar.name} get_age() - Expected 23, got {second_guitar.get_age()}")
    print(f"{gibson.name} is_vintage - Expected True, got {gibson.is_vintage()}")
    print(f"{second_guitar.name} is_vintage - Expected False, got {second_guitar.is_vintage()}")
    print(f"{third_guitar.name} is_vintage = Expected True, got {third_guitar.is_vintage()}")


run_tests()
