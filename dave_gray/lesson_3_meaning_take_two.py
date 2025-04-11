# my take on the task after watching/doing the lesson


# Attempt 1
# I will use a while loop to keep asking for input until the user enters a number greater than 10
while True:
    meaning = input('Enter a number that is greater than 10\n')
    userinput = int(meaning)

    if userinput > 10:
        print('Currect!')
        break  # Exit the loop
    else:
        print('False!')

# Attempt 2
first_try = True

while True:
    if first_try:
        meaning = input('Enter a number that is greater than 10\n')
        first_try = False
    else:
        meaning = input('Try a different number\n')

    userinput = int(meaning)

    if userinput > 10:
        print('Currect!')
        break
    else:
        print('False!')
