"""ask 5: Positional and keyword arguments + default values
Create a pig_latin function. This function will receive any amount of String objects. For each word in those strings, it should transform the word according to these rules:

If the word starts with vowel, add ay at the end.
If not, move the first letter to the end and add ay
Example:

Word => Ordway
Apple => Appleay
Additionally, the function will accept a keyword argument suffix that will allow us to change the suffix ay into any other of our choice. If we don't specify this argument, it should keep using ay (default argument).

You will define another keyword argument single with a Boolean value to indicate the type of output we want.

This output should be a list containing all the strings passed for translation (the positional arguments), unless the single argument is set to True, in which case it should return a single String object.

Consider only a, e, i, o and u as vowels.

Attention!! The input strings may have more than one word in them, so you will have to split them first and loop through all the words.

Call the function (using unpacking) with the following test cases:

test1_data = ["Word", "Apple"]
test1_config = {}

test2_data = ["Python", "Functions"]
test2_config = {"suffix": "oy"}

test3_data = ["If the word starts with a vowel", "add the suffix to the word"]
test3_config = {"single": True, "suffix": "ep"}
Your result should look like this:
['Ordway', 'Appleay']
['Ythonpoy', 'Unctionsfoy']
If the word starts with a vowelay add the suffix to the worday"""

# Solution
def pig_latin(*args, suffix='ay', single=False):
    """
    Transform words into Pig Latin.

    Parameters:
    - *args: Variable number of strings.
    - suffix: A string representing the suffix to be added (keyword argument, default='ay').
    - single: A boolean indicating whether to return a single string or a list (keyword argument, default=False).

    Returns:
    - A list of transformed words if single is False, or a single string if single is True.
    """
    transformed_words = []

    for arg in args:
        words = arg.split()
        transformed_words.extend([(word[1:] + word[0] + suffix).capitalize() if word[0].lower() not in 'aeiou' else (word + suffix).capitalize() for word in words])

    if single:
        return ' '.join(transformed_words)
    else:
        return transformed_words

# Test cases
test1_data = ["Word", "Apple"]
test1_config = {}

test2_data = ["Python", "Functions"]
test2_config = {"suffix": "oy"}

test3_data = ["If the word starts with a vowel", "add the suffix to the word"]
test3_config = {"single": True, "suffix": "ep"}

print(pig_latin(*test1_data, **test1_config))  # Expected output: ['Ordway', 'Appleay']
print(pig_latin(*test2_data, **test2_config))  # Expected output: ['Ythonpoy', 'Unctionsfoy']
print(pig_latin(*test3_data, **test3_config))  # Expected output: 'Ifay hetay ordway startsay withay aay owelvay adday hetay suffixay otay hetay ordwayay'

