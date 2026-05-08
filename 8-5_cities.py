def describe_city(name, country='Iceland'):
    """print a simple sentence"""
    print(f'{name.title()} is in {country}.')


describe_city('Reykjavik')
describe_city('Kópavogur')
describe_city('New York City', 'USA')
