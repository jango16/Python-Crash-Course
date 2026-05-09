def city_country(city, country):
    address = f'"{city}, {country}"'
    return address.title()


country_pairs = {
    'Tokyo': 'Japan',
    'Paris': 'France',
    'Cairo': 'Egypt'
}

for city2, country2 in country_pairs.items():
    print(city_country(city2, country2))
