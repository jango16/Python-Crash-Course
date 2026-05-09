person_info_1 = {
    'first_name': 'Jhon',
    'last_name': 'Geralla',
    'city': 'Cebu City'
}

person_info_2 = {
    'first_name': 'Angel',
    'last_name': 'Geralla',
    'city': 'Cebu City'
}

person_info_3 = {
    'first_name': 'Gayns',
    'last_name': 'Geralla',
    'city': 'Cebu City'
}

people = [person_info_1, person_info_2, person_info_3]

for info in people:
    if info['first_name'] == 'Jhon':
        print(
            f"{info['first_name']} {info['last_name']} is my name and I live in {info['city']}.")
    elif info['first_name'] == 'Angel':
        print(
            f"\n{info['first_name']} {info['last_name']} is my Father's name and lives in {info['city']}.")
    elif info['first_name'] == 'Gayns':
        print(
            f"\n{info['first_name']} {info['last_name']} is my Mother's name and lives in {info['city']}.")
