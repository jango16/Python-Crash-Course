cities = {
    'cdo': {
        'country': 'Philippines',
        'population_approx': 728000,
        'one_fact': 'Known as the City of Golden Friendship'
    },
    'cebu': {
        'country': 'Philippines',
        'population_approx': 964000,
        'one_fact': 'One of the oldest cities in the Philippines'
    },
    'davao': {
        'country': 'Philippines',
        'population_approx': 1776000,
        'one_fact': 'Home of Mount Apo, the highest mountain in the Philippines'
    }
}

for city, info in cities.items():
    print(f"{city.title()} City:")
    print(f" Country: {info['country']}")
    print(f" Population: {info['population_approx']:,}")
    print(f" {info['one_fact']}.")
