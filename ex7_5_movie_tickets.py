ask_age_prompt = "Hi, may I know your age?"

age = " "
while age:
    age = int(input(ask_age_prompt))

    if age < 3:
        print("The ticket is free.")

    elif 3 <= age <= 12:
        print("The ticket is $10.")

    elif age > 12:
        print("The ticket is $15.")

    break
