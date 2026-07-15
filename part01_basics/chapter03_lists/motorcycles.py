motorcycles = ["honda", "suzuki", "yamaha"]
print(motorcycles)

# Modifying elements in a List
motorcycles[0] = 'ducati'
print(motorcycles)

# Adding elements to a List
motorcycles.append('Pioneer 1')
print(motorcycles)

# Removing an Item using the Del Statement
del motorcycles[3]
print(motorcycles)

# Removing an Item using the Pop() method
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)
print("The last motorcycles that i owned was a " + popped_motorcycles.title() + ".")

# first_owned = motorcycles.pop(0)
# print("The first motorcycles that i owned was a " + first_owned.title() + ".")

# Removing an Item by value
# ['ducati', 'suzuki']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")