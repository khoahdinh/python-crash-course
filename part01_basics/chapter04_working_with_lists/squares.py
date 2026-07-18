# squares = []

# for value in range(1, 11):
#     squares.append(value**2)


# A list comprehension combines the for loop and the creation of new elements into one line
# and automatically appends each new element
squares = [value**2 for value in range(1, 11)]

print(squares)

# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
