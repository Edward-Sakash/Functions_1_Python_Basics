"""Task 4: Packing and unpacking positional arguments
Create a function sumAll that gets the sum of all values in different lists. The function will accept any number of lists, each containing a variable amount of integers.

The function should return the sum of all numbers in any of those lists and it must accept any number of parameters (use packing).

Then, define the test cases using this code (use unpacking):

test1 = [[0, 2, 4, 5]]
test2 = [
    [0, 2, 4, 5],
    [6],
    [0, 2, 4, 5, 1, 4, 3, 2]
]
Your result should look like this:
11
38"""

# Solution 1
def sumAll(*args):
    """
    Calculate the sum of all values in multiple lists.
    Parameters:
    - *args: Variable number of lists.
    Returns:
    - The sum of all numbers in the provided lists.
    """
    total_sum = 0

    for lst in args:
        total_sum += sum(lst)

    return total_sum

# Test cases
test1 = [[0, 2, 4, 5]]
test2 = [
    [0, 2, 4, 5],
    [6],
    [0, 2, 4, 5, 1, 4, 3, 2]
]

print(sumAll(*test1))  # Expected output: 11
print(sumAll(*test2))  # Expected output: 38
