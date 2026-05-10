"""A program that stores info about a car in a dictionary"""


def make_car(manufacturer, car_model, **car_info):
    """the function will always receive a manufacturer and model name and will be able to accept an arbitrary number of keyword arguments"""
    car_dict = {}
    car_dict['maker'] = manufacturer.title()
    car_dict['model'] = car_model.title()
    car_dict.update(car_info)

    return car_dict


car = make_car('toyota', 'prius', color='blue', tow_package=True)

print('\nDictionary Created')
print(car)
