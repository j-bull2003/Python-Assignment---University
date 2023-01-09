# task4.py

import random

# Assign a random number between 1 and 10 (inclusive) to the variable 'pin'
pin = random.randint(1, 10)

# Initialize a flag variable to indicate whether the login was successful
loginSuccessful = False

# Prompt the user to enter a number between 1 and 10 (inclusive) and assign it to the variable 'attempt'
while not loginSuccessful:
    attempt = int(input("Please enter a number between 1 and 10: "))
    if attempt == pin:
        # If the attempt is equal to the pin, set the flag variable to True and print a success message
        loginSuccessful = True
        print("Login is successful!")
    else:
        # If the attempt is not equal to the pin, print an error message
        print("Access is denied")
