# Test for equality and inequality with strings
car = 'subaru'
print("Test for equality and inequality with strings")
print("Variable is [car = 'subaru']")
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

# Test using the lower() method
car = 'subaru'
print("\nTest using the lower() method")
print("Variable is [car = 'subaru']")
print("Is car == 'subaru'? I predict True.")
print(car.lower() == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car.lower() == 'audi')

# Numerical tests involving equality and inequality, greater than and less than, greater than or equal to,  and less than or equal to
number = 16
print("\nNumerical tests")
print("Variable is [number = 16]")
print("Is number == 16? I predict True.")
print(number == 16)

print("\nIs number != 11? I predict True.")
print(number != 11)

print("\nIs number > 15? I predict True.")
print(number > 15)

print("\nIs number < 17? I predict True.")
print(number < 17)

print("\nIs number >= 15? I predict True.")
print(number >= 15)

print("\nIs number <= 17? I predict True.")
print(number <= 17)

# Tests using the and keyword and the or keyword
number = 16
print("\nAND & OR")
print("Variable is [number = 16]")
print("Is number == 16 and != 15? I predict True.")
print(number == 16 and number != 15)

print("\nIs number == 16 or != 15? I predict True.")
print(number == 16 or number != 15)

# Test wether an item is not in a list
numbers = [1, 2, 3, 4, 5]
print("\nTest wether an item is not in a list")
print("Variable is numbers = [1, 2, 3, 4, 5] and fav_number = 16")
fav_number = 16

if fav_number not in numbers:
    print(f"\nMy favorite number {fav_number} is not on the list.")
