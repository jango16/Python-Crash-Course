"""A program that builds my profile"""


def build_profile(first, last, **user_info):
    """Build a dictionary containing everything about my self"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    profile.update(user_info)
    return profile


user_profile = build_profile('Jhon', 'Geralla',
                             location='Cebu City',
                             license='ECE, ECT'
                             )

print('\nDictionary:')
print(user_profile)

print('\nFull Name:')
print(f"{user_profile['first_name']} {user_profile['last_name']}")

print('\nUser Info:')
print(f"Location: {user_profile['location']}")
print(f"License: {user_profile['license']}")
