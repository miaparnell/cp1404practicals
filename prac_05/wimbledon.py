"""
Wimbledon
Estimated: 30 minutes
Actual: 40 minutes
"""

COUNTRY_INDEX = 1
CHAMPION_INDEX = 2


def main():
    """Get records from a file, filter its contents, and display results about champions"""
    records = get_records()
    champion_to_count, countries = filter_records(records)
    display_results(champion_to_count, countries)


def get_records():
    """Get records from a .csv file."""
    with open("wimbledon.csv", "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        records = []
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
        in_file.close()
        return records


def filter_records(records):
    """Filter the records to get champion's names, win count, and countries."""
    champion_to_count = {}
    countries = set()
    for record in records:
        countries.add(record[COUNTRY_INDEX])
        try:
            champion_to_count[record[CHAMPION_INDEX]] += 1
        except KeyError:
            champion_to_count[record[CHAMPION_INDEX]] = 1
    return champion_to_count, countries


def display_results(champion_to_count, countries):
    """Display champion's names, win count, and the countries that have won."""
    print("Wimbledon champions: ")
    for champion, count in champion_to_count.items():
        print(champion, count)
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(','.join(country for country in sorted(countries)))


main()
