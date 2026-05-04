numbers = list(range(1, 10))

suffix_1 = 'st'
suffix_2 = 'nd'
suffix_3 = 'rd'
suffix_the_rest = 'th'

for number in numbers:
    if number == 1:
        print(f"{numbers[0]}{suffix_1}")
    elif number == 2:
        print(f"{numbers[1]}{suffix_2}")
    elif number == 3:
        print(f"{numbers[2]}{suffix_3}")
    else:
        print(f"{number}{suffix_the_rest}")
