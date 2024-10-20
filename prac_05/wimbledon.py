FILENAME = "wimbledon.csv"

def main():
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        data = in_file.readlines()

    champions = get_data(data, 2)  
    countries = get_data(data, 1)  

    country_counts = count_item(countries)
    champion_counts = count_item(champions)

    print("Wimbledon Champions:")
    for name in sorted(champion_counts.keys()):
        print(f"{name}: {champion_counts[name]}")

    sorted_countries = sorted(country_counts.keys())
    print(f"\nThese {len(sorted_countries)} countries have won Wimbledon:")
    print(", ".join(sorted_countries))

def get_data(data, column_index):
    items = []
    for line in data[1:]:  # Skip the header
        columns = line.strip().split(",")
        if len(columns) > column_index:  
            items.append(columns[column_index])
    return items

def count_item(items):
    item_counts = {}
    for item in items:
        item_counts[item] = item_counts.get(item, 0) + 1
    return item_counts

main()
