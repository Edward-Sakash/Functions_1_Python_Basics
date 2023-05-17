"""ask 2: Multiple positional arguments of different types
Create a single function getParity that does the same thing as the two functions in the previous task. This new function will accept a new positional argument of type String that will contain the type of parity we want to get (either odd or even).

If the argument parity is different than odd and even then it should output a string message Parity indicated is unknown.

Then design your own test cases to replicate the ones in the previous task but using the new function. Add also the following test case at the end:

print(getParity(-2, 'number'))
Your result should look like this:
True False
False True
False True
Parity indicated is unknown"""

# Solution 1
def getParity(num, parity):
    """
    Check the parity of a number based on the given parity type.

    Parameters:
    - num: An integer number.
    - parity: A string indicating the desired parity type ('odd' or 'even').

    Returns:
    - True if the number has the desired parity, False otherwise.
    - If the parity indicated is unknown, returns a string message.
    """
    if parity == 'odd':
        return num % 2 != 0
    elif parity == 'even':
        return num % 2 == 0
    else:
        return 'Parity indicated is unknown'

# Test cases
print(getParity(1, 'odd'), getParity(1, 'even'))  # Expected output: True False
print(getParity(657842, 'even'), getParity(657842, 'odd'))  # Expected output: False True
print(getParity(0, 'even'), getParity(0, 'odd'))  # Expected output: False True
print(getParity(-2, 'number'))  # Expected output: Parity indicated is unknown

print("______________________________________________________")

# Solution 2
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

def getParity(num, parity):
    """
    Check the parity of a number based on the given parity type.
    Parameters:
    - num: An integer number.
    - parity: A string indicating the desired parity type ('odd' or 'even').
    Returns:
    - True if the number has the desired parity, False otherwise.
    - If the parity indicated is unknown, returns a string message.
    """
    parity_functions = {
        'odd': isOdd,
        'even': isEven
    }

    if parity in parity_functions:
        return parity_functions[parity](num)
    else:
        return 'Parity indicated is unknown'

# Test cases
print(getParity(1, 'odd'), getParity(1, 'even'))  # Expected output: True False
print(getParity(657842, 'even'), getParity(657842, 'odd'))  # Expected output: False True
print(getParity(0, 'even'), getParity(0, 'odd'))  # Expected output: False True
print(getParity(-2, 'number'))  # Expected output: Parity indicated is unknown
