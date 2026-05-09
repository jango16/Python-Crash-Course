responses = {}
recommendation = []

polling_active = True

while polling_active:

    name = input("\nWhat is your name? ")

    response = input(
        "If you could visit one place in the world, where would you go? ")

    responses[name] = response

    repeat = input("\nWould you like to let another person respond? (yes/no) ")

    while repeat.lower() == 'yes':

        recommended_person = input("\nWhat is her/his name?")
        recommendation.append(recommended_person)

        repeat = input(
            "\nWould you like to let another person respond? (yes/no) ")

    if repeat.lower() == 'no':
        polling_active = False

print("\nPolling Results:")
for name, response in responses.items():
    print(f"{name.title()} would like to visit {response.title()}.")

print("\nRecommended Persons:")
for recommended_person in recommendation:
    print(f"- {recommended_person.title()} is invited to respond, and is awaiting for response.")
