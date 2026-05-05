pet_1 = {
    'animal': 'dog',
    'owner': 'Jhon'
}

pet_2 = {
    'animal': 'cat',
    'owner': 'Maria'
}

pet_3 = {
    'animal': 'parrot',
    'owner': 'Carlos'
}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    print(f"{pet['owner']} owns a pet {pet['animal'].title()}\n")
