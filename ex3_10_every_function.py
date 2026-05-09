things = ['Mt. Everest', 'Cagayan River',
          'Alaska', 'New York City', 'Japanese']

print("\nI will demonstrate every function in the Lists Chapter")
print("Accessing Elements in a List, getting one element on a list for example at index 0")
print(things[0])


print("\nOriginal List:")
print(things)
print("Modifying Elements in a List, changin index 0 into 'Keyboard'")
things[0] = 'Keyboard'
print(things)

print("\nCurrent List:")
print(things)
print("Appending Elements to the End of a List, adding 'Logitech'")
things.append('Logitech')
print(things)

print("\nCurrent List:")
print(things)
print("Inserting Elements into a List, inserting 'Vitamins' to index 0")
things.insert(0, 'Vitamins')
print(things)

print("\nCurrent List:")
print(things)
print("Removing an Item Using the del Statement, removing 'Logitech'")
del things[-1]
print(things)

print("\nCurrent List:")
print(things)
print("Removing an Item Using the pop() Method, popping the top of the stack and using it")
popped_things = things.pop()
print(popped_things)
print("The popped element is now gone forever:")
print(things)

print("\nCurrent List:")
print(things)
print("Popping Items from Any Position in a List, popping index 1 'Keyboard' and using it")
popped_any_position = things.pop(1)
print(popped_any_position)
print("The popped element is now gone forever:")
print(things)

print("\nCurrent List:")
print(things)
print("Removing an Item by Value, now we won't be using index, but using VALUE instead, we remove 'Alaska'")
things.remove('Alaska')
print(things)

print("\nCurrent List:")
print(things)
print("Sorting a List Permanently with the sort() Method, it will sort it alphabetically")
things.sort()
print(things)

print("\nCurrent List:")
print(things)
print("Sorting a List Permanently with the sort() Method, we can also do it in reverse-alphabetical order")
things.sort(reverse=True)
print(things)

print("\nCurrent List:")
print(things)
print("Sorting a List Temporarily with the sorted() Function, maintain the original order of a list but present it in a sorted order")
print("sorted() function used:")
print(sorted(things))
print("Original List:")
print(things)

print("\nCurrent List:")
print(things)
print("Printing a List in Reverse Order, it will just reverse the current/made list")
things.reverse()
print(things)

print("\nCurrent List:")
print(things)
print("Finding the Length of a List, using len() function")
print(len(things))
