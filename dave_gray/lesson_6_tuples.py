# Tuples
# Tuples are similar to lists, but they are immutable (cannot be changed after creation).

mytuple = tuple((1, "Morten", 3, True, 5))

# Tuples can be created using parentheses or the tuple() constructor.
# They can contain any data type, including other tuples.
anothertuple = (1, 2, 4, 8, 16)

print(mytuple)  # Output: (1, Morten, 3, True, 5)
print(type(mytuple))  # Output: <class 'tuple'>
print(type(anothertuple))  # Output: <class 'tuple'>

# Convert tuple to list ~ creates a list from the tuple
newlist = list(mytuple)
print(newlist)  # Output: [1, 'Morten', 3, True, 5]
# Append to the newlist that was created from the tuple
newlist.append("Niels")
# Convert list back to tuple so that Niels was added to the tuple
newtuple = tuple(newlist)
print(newtuple)  # Output: (1, 'Morten', 3, True, 5, 'Niels')
# Output: (1, Morten, 3, True, 5) # Original tuple is unchanged of course
print(mytuple)

# if the * is on three the output would be [4, 8, 16] and likewise if it was on hey the output would be
# [1, 2, 4] and the rest would be unpacked into the other variables
(hey, *two, three) = anothertuple  # Unpacking the tuple into variables
print(hey)  # Output: 1
print(two)  # Output: [2, 4, 8]
print(three)  # Output: 16

# Output: 1 # Count the number of occurrences of 4 in the tuple so if the number 4 was in the tuple twice it would be 2 and so on
print(anothertuple.count(4))
