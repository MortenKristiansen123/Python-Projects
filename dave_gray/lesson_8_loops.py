# Loops


# while loops (will execute a block of code as long as the condition is true)

value = 1

# while value < 10:
#     print(value)
#     if value == 5:
#         break # this will break the loop when value is equal to 5
#     value += 1  # this will print 1 to 9, if we wanted to print 1 to 10 we would use <= instead of <

# while value <= 10:
#     value += 1
#     if value == 5:
#         continue  # this will skip the rest of the code in the loop when value is equal to 5
#     print(value)  # this will print 2 to 10, and skipping 5 because of the continue statement we don't get to the print statement
# else:
#     print("Value is now equal to " + str(value))


# for loops

names = ["Dave", "Sara", "John"]
# the variable x will take the value of each item in the list names, it is just some type of character that we can use to represent the value of the item in the list (it could be anything, but it is common to use x or i, etc.)
# for x in names:
#     print(x)

# for x in "Messissippi":
#     print(x)

# for x in names:
#      if x == "Sara":
#         break
#     print(x)

# as can be seen in the example above, it is very important that the indentation is correct, otherwise the code will not work as expected.
# for x in names:
#     if x == "Sara":
#         break
#     print(x) # this will print Dave and Sara, but not John as he comes after Sara in the list

# for x in names:
#     if x == "Sara":
#         # If x is "Sara", this tells Python to skip the rest of the code inside the loop for this iteration and jump to the next one. Meaning that the print(x) for "Sara" will not be executed.
#         continue
#     print(x) # this will print Dave and John, but not Sara


# for x in range(10):  # Prints the numbers from 0 to 9 (because its giving us a range of 10, which includes 0 therefore it will print 0 to 9)
#     print(x) # Prints 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

# for x in range(2, 4):  # Starts at 2 and stops at 4 (it will include the number that you start on, but not the number that you stop on)
#     print(x)  # Prints 2 and 3

for x in range(5, 101, 5):  # Goes from 0 to a 100 in increments of 5 (it will include the number that you start on, but not the number that you stop on)
    print(x)  # Prints 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95 and 100
else:
    print("Done!")  # This will print Done after the loop is finished.

actions = ["codes", "eats", "sleeps"]

# for name in names:
#     for action in actions:
#         print(name + " " + action) # This will print all the combinations of names and actions, for example: Dave codes, Dave eats, Dave sleeps, Sara codes, Sara eats, Sara sleeps, John codes, John eats and John sleeps.

# for action in actions:  # whatever is on the outside is what happens and it loops through for whatever is on the inside
#     for name in names:
#         print(name + " " + action)

outcomes = ["Well", "Good", "Bad"]

for action in actions:
    for name in names:
        for outcome in outcomes:
            print(name + " " + action + " " + outcome)
