# task5.py

def sum_even(a, b):
    """
    This function returns the sum of all even integers between 'a' and 'b' (inclusive).
    If 'b' is less than 'a', the function returns the sum of all even integers between 'b' and 'a' (inclusive).
    """
    # Determine the start and end values for the range of numbers
    start = a if a < b else b
    end = b if a < b else a
    
    # Initialize the sum to 0
    total = 0
    
    # Iterate over the range of numbers and add the even numbers to the total
    for i in range(start, end+1):
        if i % 2 == 0:
            total += i
    
    # Return the total sum
    return total

# Call the 'sum_even' function with input a = 10, b = 20 and assign the returned value to the variable 'sample'
sample = sum_even(10, 20)

# Print the value of 'sample'
print(sample)
