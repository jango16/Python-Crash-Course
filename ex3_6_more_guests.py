people = ["Alex", "Charo", "Jackelyn"]
print(people)
print(f"{people[0]}, I found out the you can get a bigger table.")
print(f"{people[1]}, I found out the you can get a bigger table.")
print(f"{people[2]}, I found out the you can get a bigger table.")

people.insert(0, "Leo")
print(f"Hi {people[0]}, I am inviting you to dinner.")
print(people)

people.insert(2, "Yale")
print(f"Hi {people[2]}, I am inviting you to dinner.")
print(people)

people.append("Robert")
print(f"Hi {people[-1]}, I am inviting you to dinner.")
print(people)
