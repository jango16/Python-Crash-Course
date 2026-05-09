favorite_places = {
    'Jhon': ['Cebu', 'Siargao', 'Baguio'],
    'Maria': ['Davao', 'Boracay', 'Manila'],
    'Carlos': ['Palawan', 'Iloilo', 'Tagaytay'],
    'Anna': ['Cagayan de Oro', 'Camiguin', 'Bukidnon'],
    'David': ['La Union', 'Vigan', 'Batanes']
}

for person, places in favorite_places.items():
    print(f"{person}'s favorite places are {', '.join(places)}")
