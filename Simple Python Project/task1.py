# task1.py

# Prompt the user to enter their first name and assign it to the variable 'firstName'
firstName = input("Please enter your first name: ")

# Prompt the user to enter their last name and assign it to the variable 'lastName'
lastName = input("Please enter your last name: ")

# Prompt the user to enter their favorite book title and assign it to the variable 'book'
book = input("Please enter the title of your favorite book: ")

# Prompt the user to enter the number of times they have read their favorite book and assign it to the variable 'time'
time = int(input("Please enter the number of times you have read your favorite book: "))

# Print the full name, book title, and number of times the book has been read
print("Full Name:", firstName + " " + lastName)
print("Book Title:", book)
print("Number of Times Read:", time)
