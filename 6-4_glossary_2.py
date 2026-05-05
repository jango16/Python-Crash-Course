python_terms = {
    'variable': 'A container used to store data values.',
    'list': 'A collection of items stored in a single variable.',
    'tuple': 'An immutable collection of items.',
    'dictionary': 'A collection of key-value pairs.',
    'loop': 'A control structure used to repeat a block of code.',
    'function': 'A block of reusable code that performs a specific task.',
    'string': 'A sequence of characters enclosed in quotes.',
    'integer': 'A whole number without a decimal point.',
    'boolean': 'A data type with two values: True or False.',
    'comment': 'A note in the code that is ignored by Python.'

}

for terms, meaning in python_terms.items():
    print(f"\n{terms.title()}:")
    print(f"{meaning.title()}")
