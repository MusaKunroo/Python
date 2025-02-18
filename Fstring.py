#"format" refers to the way a string is structured by inserting values into specific places within the string.
#Before Python 3.6 (Using .format())
#The .format() method was used to insert values into a string:
#! name = "Alice"
#! age = 25
#! print("My name is {} and I am {} years old.".format(name, age))
# With F-Strings (Python 3.6+)
# F-strings provide a more readable way to insert variables:
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")
