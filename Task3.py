"""Task 3: Multiple keyword arguments of different types
Create a single function greet that greets a person differently depending on the time of the day.

To do that, you will need to define two parameters on the header, one of type String and the other one of type Date. You must define them as keyword arguments and name them name and date.

If the time of the date is before 12:00PM the function will return "Good Morning, name_of_the_person!", if not it will return "Good Afternoon, name_of_the_person!".

You can extended it to say Good Night at another time, if you like.

Use the following test cases:

print(greet(
    name="John",
    date=datetime.datetime(2021, 5, 7, 11, 59, 59)
    ))
print(greet(
    date=datetime.datetime(2021, 5, 7, 12, 0, 1),
    name="John"
    ))
Your result should look like this:
Good Morning, John!
Good Afternoon, John!"""

# Solution
import datetime

def greet(name=None, date=None):
    """
    Greet a person differently based on the time of the day.
    Parameters:
    - name: A string representing the name of the person (keyword argument).
    - date: A datetime object representing the current date and time (keyword argument).
    Returns:
    - A greeting message based on the time of the day and the person's name.
    """
    if date is None:
        date = datetime.datetime.now()

    if name is None:
        name = "Guest"

    if date.time() < datetime.time(12):
        return f"Good Morning, {name}!"
    elif date.time() < datetime.time(18):
        return f"Good Afternoon, {name}!"
    else:
        return f"Good Night, {name}!"

# Test cases
print(greet(name="John", date=datetime.datetime(2021, 5, 7, 11, 59, 59)))
print(greet(date=datetime.datetime(2021, 5, 7, 12, 0, 1), name="John"))
