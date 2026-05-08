def make_shirt(text, size='Large'):
    print(
        f'You ordered {size.title()}-sized T-shirt with "{text}" printed on it.')


make_shirt('I love Python')
make_shirt('I love Python', size='medium')
make_shirt('ECE', 'small')
