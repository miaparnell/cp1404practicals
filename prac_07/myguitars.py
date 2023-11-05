from guitar import Guitar


def main():
    """Read file of programming language details, save as objects, display."""
    guitars = []
    in_file = open('guitars.csv', 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    in_file.close()

    for guitar in guitars:
        print(guitar)

    guitars.sort()
    print("Guitars sorted by year: ")
    for guitar in guitars:
        print(guitar)

    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost : $"))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{new_guitar} added.")
        name = input("Name: ")

    with open('guitars.csv', 'w', newline="") as out_file:
        for guitar in guitars:
            guitar_string = f"{guitar.name},{str(guitar.year)},{str(guitar.cost)}\n"
            out_file.write(guitar_string)
        out_file.close()


main()
