print("Enter pizza toppings that you want on your pizza.")
print("Enter 'quit' to exit program.")

message = ""
while message != 'quit':
    message = input("\nTopping: ")
    if message.lower().strip() == 'quit':
        break
    print(f"Noted, I will add ({message.title()}) to your pizza.")
