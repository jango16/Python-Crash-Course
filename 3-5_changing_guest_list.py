people = ["Alex", "Charo", "Jackelyn"]
print(people)

del people[0]
print(f"Unfortunately, {people[0]} can't make it")

people.insert(0, "Jhon")
print(people)
print(f"Hi {people[0]}, I am inviting you to dinner.")
print(f"Hi {people[1]}, I am inviting you to dinner.")
print(f"Hi {people[2]}, I am inviting you to dinner.")
