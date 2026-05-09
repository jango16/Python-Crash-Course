inquiry_diners = input(
    "\nHi, if I may ask, about how many chairs do you need for the reservation?")
inquiry_diners = int(inquiry_diners)

if inquiry_diners > 8:
    print("\nI am very sorry, you have to wait for a table.")
else:
    print("\nNoted Mam/Sirs, right on time, your dinner table is ready!")
