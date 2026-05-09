people = {
    'John': {'fav_number': '23', 'age': '16', 'city': 'cdo'},
    'Maria': {'fav_number': '1', 'age': '17', 'city': 'cebu'},
    'Carlos': {'fav_number': '44', 'age': '17', 'city': 'davao'},
    'Anna': {'fav_number': '5', 'age': '4', 'city': 'siargao'},
    'David': {'fav_number': '67', 'age': '12', 'city': 'la union'}
}

for name, info in people.items():
    print(f"{name}:")
    print(f"Favorite Number: {info['fav_number']}")
    print(f"Age: {info['age']}")
    print(f"City: {info['city'].title()}\n")
