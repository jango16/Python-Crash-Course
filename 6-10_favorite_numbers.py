people = {
    'John': {'fav_numbers': [12, 3], 'age': '16', 'city': 'cdo'},
    'Maria': {'fav_numbers': [121, 23], 'age': '17', 'city': 'cebu'},
    'Carlos': {'fav_numbers': [123, 3213], 'age': '17', 'city': 'davao'},
    'Anna': {'fav_numbers': [1255, 345], 'age': '4', 'city': 'siargao'},
    'David': {'fav_numbers': [1442, 321213], 'age': '12', 'city': 'la union'}
}

for name, info in people.items():
    numbers = ', '.join(str(num) for num in info['fav_numbers'])
    print(f"{name}'s favortite numbers are {numbers}")


# What str(num) does, Converts numbers → strings so .join() can work
# str(23) → "23"
# str(2)  → "2"
# join() → ONLY accepts strings
