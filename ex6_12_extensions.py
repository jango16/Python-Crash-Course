# Each city should have: multiple facts (list)
# Print: all info
# Add a condition: Only show cities with population > 1,000,000

cities = {
    'cdo': {
        'country': 'Philippines',
        'population': 728000,
        'facts': [
            'Known as the City of Golden Friendship',
            'Popular for whitewater rafting'
        ]
    },
    'cebu': {
        'country': 'Philippines',
        'population': 964000,
        'facts': [
            'One of the oldest cities in the Philippines',
            'Known as the Queen City of the South'
        ]
    },
    'davao': {
        'country': 'Philippines',
        'population': 1776000,
        'facts': [
            'Home of Mount Apo',
            'Known for durian fruit'
        ]
    }
}

for city, info in cities.items():
    if info['population'] > 1000000:
        print(f"{city.title()} City:")
        print(f" Country: {info['country']}")
        print(f" Population: {info['population']:,}")
        print(" Facts:")
        for fact in info['facts']:
            print(f" - {fact}.")
