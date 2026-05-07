sandwhich_orders = ['BLT', 'Club Sandwhich', 'Reuben',
                    'Roast Beef Sandwhich', 'Egg Salad Sandwhich']
finished_sandwiches = []

for sandwich_order in sandwhich_orders:
    print(f"I made your {sandwich_order}.")

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
