print("The price of the tickets depends on the person's age.")
print("Input 'quit' to exit the program.")

active = True
message = " "
while active:
    message = input("\nAge: ")

    if message.lower().strip() == 'quit':
        active = False

    else:
        message = int(message)

        if message < 3:
            print("The ticket is free.")

        elif 3 <= message <= 12:
            print("The ticket is $10.")

        elif message > 12:
            print("The ticket is $15.")

        break
