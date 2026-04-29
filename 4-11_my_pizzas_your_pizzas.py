fav_pizzas = ['Greenwhich', 'Pizzahut', 'Albertos']
friend_pizzas = fav_pizzas[:]

fav_pizzas.append("Pepperoni")
friend_pizzas.append("Hawaiian")

print("My favorite pizzas area:")
for my_pizza in fav_pizzas:
    print(my_pizza)

print("\nMy friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)
