# Unpacking in Python  
# Unpacking is a powerful feature in Python that allows you to extract values 
# from tuples or lists into separate variables in a concise way.  

# Example without unpacking:  
# Traditionally, to extract values from a tuple, we use indexing:  

coordinates = (1, 2, 3)

x = coordinates[0]
y = coordinates[1]
z = coordinates[2]

result = x * y * z  # Using these values in a calculation
print(result)  # Output: 6

# This method becomes repetitive when dealing with multiple values.  

# Using unpacking (More Pythonic Way)  
# Instead of manually extracting values, Python allows unpacking in a single line:  

coordinates = (1, 2, 3)

x, y, z = coordinates  # Unpacking tuple

result = x * y * z
print(result)  # Output: 6

# Here’s how it works:  
# 1. `x` gets assigned `1` (first item in the tuple).  
# 2. `y` gets assigned `2` (second item in the tuple).  
# 3. `z` gets assigned `3` (third item in the tuple).  

# This approach is **cleaner, shorter, and more readable**.  

# Unpacking Lists  
# Unpacking is not just limited to tuples; it works for lists as well:  

coordinates = [1, 2, 3]  # A list instead of a tuple

x, y, z = coordinates  # Unpacking list

print(y)  # Output: 2

# The process remains the same whether we use a **tuple** or a **list**.  
