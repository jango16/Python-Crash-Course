people = ['Leo', 'Alex', 'Yale', 'Charo', 'Jackelyn', 'Robert']
print(people)
print("I am sorry guys, I can only invite 2 people unfortunately.")

pop1 = people.pop(0)
print(f"I'm sorry {pop1}, I can't invite you to dinner.")
print(people)

pop2 = people.pop(0)
print(f"I'm sorry {pop2}, I can't invite you to dinner.")
print(people)

pop3 = people.pop(0)
print(f"I'm sorry {pop3}, I can't invite you to dinner.")
print(people)

pop4 = people.pop(0)
print(f"I'm sorry {pop4}, I can't invite you to dinner.")
print(people)

print(f"Hi {people[0]}, you are still invited to my dinner tonight.")
print(f"Hi {people[1]}, you are still invited to my dinner tonight.")

del people[0]
del people[0]
new_people = people
print(new_people)
