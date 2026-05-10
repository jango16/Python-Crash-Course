"""A program that takes sandwhich fillings orders."""


def sandwich_fills(count, *fills):
    """this function accepts a list of items a person wants on a sandwich"""
    print(f'\nTest {count}')
    print('Sandwhich fillings ordered:')
    for fill in fills:
        print(f' - {fill}')


sandwich_fills(1, 'Egg Mayonnaise')
sandwich_fills(2, 'Egg Mayonnaise', 'Chicken Salad')
sandwich_fills(3, 'Egg Mayonnaise', 'Chicken Salad', 'Tuna Mayonnaise')
