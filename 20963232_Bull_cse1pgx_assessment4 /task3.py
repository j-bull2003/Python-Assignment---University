# task3.py

# Declare and instantiate an empty dictionary 'dict'
dict = {}

# Prompt the user to enter their first name and assign it to the variable 'firstName'
firstName = input("Please enter your first name: ")

# Add the first name to the dictionary 'dict' with the key "firstName"
dict["firstName"] = firstName

# Prompt the user to enter their last name and assign it to the variable 'lastName'
lastName = input("Please enter your last name: ")

# Add the last name to the dictionary 'dict' with the key "lastName"
dict["lastName"] = lastName

# Prompt the user to enter their favorite book title and assign it to the variable 'book'
book = input("Please enter the title of your favorite book: ")

# Add the book title to the dictionary 'dict' with the key "book"
dict["book"] = book

# Prompt the user to enter the number of times they have read their favorite book and assign it to the variable 'time'
time = int(input("Please enter the number of times you have read your favorite book: "))

# Add the number of times the book has been read to the dictionary 'dict' with the key "time"
dict["time"] = time

# Print the dictionary 'dict'
print(dict)
