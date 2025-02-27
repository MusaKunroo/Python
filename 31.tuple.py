# Creating a tuple
my_tuple = (1, 2, 3, 4)
print(my_tuple)  # Output: (1, 2, 3, 4)

# Tuple with different data types
mixed_tuple = (10, "Hello", 3.14, True)
print(mixed_tuple)  # Output: (10, 'Hello', 3.14, True)

# Single element tuple (Needs a comma)
single_tuple = (5,)
print(single_tuple)  # Output: (5,)

# Indexing (Starts from 0)
print(my_tuple[0])  # Output: 1

# Negative Indexing
print(my_tuple[-1])  # Output: 4

# Slicing
print(my_tuple[1:3])  # Output: (2, 3)

# Concatenation
new_tuple = my_tuple + (5, 6)
print(new_tuple)  # Output: (1, 2, 3, 4, 5, 6)

# Repeating
repeat_tuple = ("Hi",) * 3
print(repeat_tuple)  # Output: ('Hi', 'Hi', 'Hi')

# Length
print(len(my_tuple))  # Output: 4

# Count occurrences of an element
print(my_tuple.count(2))  # Output: 1

# Find index of an element
print(my_tuple.index(3))  # Output: 2

