print("The deli has run out of pastrami.")

sandwhich_orders = ['BLT', 'pastrami', 'Club Sandwhich', 'Reuben', 'pastrami',
                    'Roast Beef Sandwhich', 'Egg Salad Sandwhich', 'pastrami']
finished_sandwiches = []

print("\n# with pastrami list:")
print(sandwhich_orders)

while 'pastrami' in sandwhich_orders:
    sandwhich_orders.remove('pastrami')

print("\n# removed pastramis in the list:")
print(sandwhich_orders)

while sandwhich_orders:
    current_sandwhich = sandwhich_orders.pop()
    finished_sandwiches.append(current_sandwhich)

print("\nThe following sandwhich are finished:")
for finished_sandwhich in finished_sandwiches:
    print(f"{finished_sandwhich}")

print("\nSandwhich Orders list:")
print(sandwhich_orders)
print("\nFinished Sandwhich list:")
print(finished_sandwiches)
