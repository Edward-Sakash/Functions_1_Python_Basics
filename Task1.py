"""Task 1: Simple functions with single positional arguments
Create two simple functions isOdd and isEven that each take a single Integer and return a Boolean indicating whether the passed value is odd or is even.

An integer is even if it can be divided by 2 to produce another integer value. It is odd when dividing it by two produces a decimal value.

Then use those functions with these test cases:

print(isOdd(1), isEven(1))
print(isOdd(657842), isEven(657842))
print(isOdd(0), isEven(0))
Your result should look like this:
True False
False True
False True"""

# Solution 
def isOdd(num):
    """
    Check if a number is odd.
    Parameters:
    - num: An integer number.
    Returns:
    - True if the number is odd, False otherwise.
    """
    return num % 2 != 0

def isEven(num):
    """
    Check if a number is even.
    Parameters:
    - num: An integer number.
    Returns:
    - True if the number is even, False otherwise.
    """
    return num % 2 == 0

# Test cases
print(isOdd(1), isEven(1))  # Expected output: True False
print(isOdd(657842), isEven(657842))  # Expected output: False True
print(isOdd(0), isEven(0))  # Expected output: False True

print("__________________________________________________")

# Solution 2
def isOdd(num):
    """
    Check if a number is odd.
    Parameters:
    - num: An integer number.
    Returns:
    - True if the number is odd, False otherwise.
    """
    return num // 2 * 2 != num

def isEven(num):
    """
    Check if a number is even.
    Parameters:
    - num: An integer number.
    Returns:
    - True if the number is even, False otherwise.
    """
    return num // 2 * 2 == num

# Test cases
print(isOdd(1), isEven(1))  # Expected output: True False
print(isOdd(657842), isEven(657842))  # Expected output: False True
print(isOdd(0), isEven(0))  # Expected output: False True

