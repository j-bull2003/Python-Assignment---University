# task6.py

class Book:
    """
    This class represents a book with four instance variables: year, title, author, and publisher.
    It has four accessor methods (get_year, get_title, get_author, get_publisher) to retrieve the values
    of these instance variables, and four mutator methods (set_year, set_title, set_author, set_publisher)
    to update the values of these instance variables.
    """
    
    def __init__(self, year, title, author, publisher):
        """
        This constructor initializes the instance variables with the given values.
        """
        self.year = year
        self.title = title
        self.author = author
        self.publisher = publisher
    
    def get_year(self):
        """
        This method returns the value of the instance variable 'year'.
        """
        return self.year
    
    def get_title(self):
        """
        This method returns the value of the instance variable 'title'.
        """
        return self.title
    
    def get_author(self):
        """
        This method returns the value of the instance variable 'author'.
        """
        return self.author
    
    def get_publisher(self):
        """
        This method returns the value of the instance variable 'publisher'.
        """
        return self.publisher
    
    def set_year(self, year):
        """
        This method updates the value of the instance variable 'year' with the given value.
        """
        self.year = year
    
    def set_title(self, title):
        """
        This method updates the value of the instance variable 'title' with the given value.
        """
        self.title = title
    
    def set_author(self, author):
        """
        This method updates the value of the instance variable 'author' with the given value.
        """
        self.author = author
    
    def set_publisher(self, publisher):
        """
        This method updates the value of the instance variable 'publisher' with the given value.
        """
        self.publisher = publisher

# Create an instance of the 'Book' class named 'my_book'
my_book = Book(2020, "The Great Gatsby", "F. Scott Fitzgerald", "Charles Scribner's Sons")

# Print the information of 'my_book' using the appropriate method calls
print("Year:", my_book.get_year())
print("Title:", my_book.get_title())
print("Author:", my_book.get_author())
print("Publisher:", my_book.get_publisher())
