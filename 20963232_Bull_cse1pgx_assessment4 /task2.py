# task2.py

# Declare and instantiate an empty list 'lst'
lst = []

# Prompt the user to enter their first name and assign it to the variable 'firstName'
firstName = input("Please enter your first name: ")

# Append 'firstName' to the list 'lst'
lst.append(firstName)

# Prompt the user to enter their last name and assign it to the variable 'lastName'
lastName = input("Please enter your last name: ")

# Append 'lastName' to the list 'lst'
lst.append(lastName)

# Prompt the user to enter their favorite book title and assign it to the variable 'book'
book = input("Please enter the title of your favorite book: ")

# Append 'book' to the list 'lst'
lst.append(book)

# Prompt the user to enter the number of times they have read their favorite book and assign it to the variable 'time'
time = int(input("Please enter the number of times you have read your favorite book: "))

# Append 'time' to the list 'lst'
lst.append(time)

# Print the list 'lst'
print(lst)
