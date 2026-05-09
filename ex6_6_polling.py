favorite_languages_poll = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

friends = ['jen', 'sarah', 'muhamad', 'mely', 'jason']
for name in friends:
    if name in favorite_languages_poll.keys():
        print(f"{name.title()}, thank you for responding in the poll.")
    else:
        print(f"{name.title()}, please respond to the poll, thank you!")
