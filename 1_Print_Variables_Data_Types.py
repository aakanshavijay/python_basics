# ============================================================
# PYTHON BASICS
# Print, Variables, Variable Names and Data Types
# ============================================================

# ============================================================
# 1. PRINT()
# ============================================================

# print() is used to display something on the screen.

print("hello")
print("Hi im aakansha")
print("I am learning python")

# We can also print numbers and calculations.

print(3)
print(2 + 4)


# ============================================================
# 2. COMMENTS
# ============================================================

# A comment is a note written in the code.
# Python does not execute comments.
# Comments start with #.

# This is a comment
# print("This line is not executed because it is commented out.")


# ============================================================
# 3. MULTI-LINE STRINGS
# ============================================================

# Triple quotes can be used to write text across multiple lines.

print("""This is a multi-line string.
It can span multiple lines.""")


# ============================================================
# 4. VARIABLES
# ============================================================

# A variable is a name used to store a value.

x = 3
y = "Hello, World!"
a = 'hello world'
A = 10
z = 35.6

# Variables can store different types of values.

apple = "I am an apple"
Apple = 34

print(x)
print(y)
print(a)
print(A)
print(z)


# ============================================================
# 5. VARIABLE NAMES
# ============================================================

# Variable names can contain letters, numbers and underscores.

age = 18
count = 5

# Rules for variable names:
#
# 1. A variable name should start with a letter or underscore.
# 2. A variable name cannot start with a number.
# 3. A variable name can contain letters, numbers and underscores.
# 4. A variable name cannot be a Python keyword.
#
# Example of an invalid variable name:
#
# 3count = 4


# ============================================================
# 6. PYTHON IS CASE-SENSITIVE
# ============================================================

# 'apple' and 'Apple' are different variable names.

apple = "I am an apple"
Apple = 34

print(apple)
print(Apple)


# ============================================================
# 7. CHECKING THE TYPE OF A VARIABLE
# ============================================================

# The type() function tells us what type of data a variable contains.

x = 3
y = "Hello, World!"
z = 35.6

print(type(x))
print(type(y))
print(type(z))


# ============================================================
# 8. MULTIPLE VARIABLES
# ============================================================

# We can assign values to multiple variables at the same time.

a, b, c = 5, 10, 15

print(a)
print(b)
print(c)


# We can also assign the same value to multiple variables.

a = b = c = 20

print(a)
print(b)
print(c)


# ============================================================
# 9. WORKING WITH VARIABLES
# ============================================================

a = 18
b = 5

print(a + b)

c = "Hello"
d = "World"

print(c + d)

# We can also print multiple values together.

print(a, c)


# ============================================================
# 10. PYTHON DATA TYPES
# ============================================================

# Some important Python data types are:

# int
# str
# float
# complex
# list
# tuple
# set
# dict
# bool
# NoneType


# ============================================================
# 11. INTEGER (int)
# ============================================================

# An integer is a whole number.

x = 5
x = -5

print(type(x))


# ============================================================
# 12. STRING (str)
# ============================================================

# A string is text.
# Strings are written inside quotation marks.

x = "5"

print(type(x))

# Notice that 5 and "5" are different types.

x = 5
y = "5"

print(type(x))
print(type(y))


# ============================================================
# 13. FLOAT (float)
# ============================================================

# A float is a number containing a decimal value.

x = 5.0
x = -5.0
x = 5.00

print(type(x))


# ============================================================
# 14. COMPLEX (complex)
# ============================================================

# A complex number can contain a real and imaginary part.

x = 5 + 3j

print(type(x))


# ============================================================
# 15. LIST
# ============================================================

# A list is used to store multiple values together.
#
# Lists are:
# - ordered
# - changeable
# - allow duplicate values
#
# Lists are created using square brackets [].

x = [1, 2, 3, 4, 4, 2, 1, -34, -56]

print(x)
print(type(x))


# ============================================================
# 16. ADDING AN ELEMENT TO A LIST
# ============================================================

# append() adds an element to the end of a list.

x = [1, 2, 3, 4]

x.append(5)

print(x)


# ============================================================
# 17. REMOVING AN ELEMENT FROM A LIST
# ============================================================

# remove() removes an element using its VALUE.

x = [1, 2, 3, 4, 4, 2, 1]

x.remove(2)

print(x)


# ============================================================
# 18. REMOVING AN ELEMENT USING ITS INDEX
# ============================================================

# pop() removes an element using its INDEX.

x = [1, 2, 3, 4, 4, 2, 1]

x.pop(4)

print(x)


# ============================================================
# 19. LISTS CAN CONTAIN STRINGS
# ============================================================

y = ["apple", "banana", "cherry"]

print(y)


# ============================================================
# 20. CHANGING AN ELEMENT IN A LIST
# ============================================================

# Lists are changeable, so we can replace an element.

y = ["apple", "banana", "cherry"]

y[0] = "kiwi"

print(y)


# ============================================================
# 21. ACCESSING ELEMENTS USING INDEX
# ============================================================

# Python starts indexing from 0.

y = ["apple", "banana", "cherry"]

print(y[0])
print(y[1])
print(y[2])


# Negative indexes can be used to access elements from the end.

print(y[-1])
print(y[-2])


# ============================================================
# 22. TUPLE
# ============================================================

# A tuple is another type of collection.

x = (1, 2, 3)

print(type(x))


# A tuple can also be created without brackets.

x = 1, 2, 3

print(type(x))


# ============================================================
# 23. SET
# ============================================================

# A set is a collection of values.

x = {1, 2, 3}

print(type(x))


# ============================================================
# 24. DICTIONARY
# ============================================================

# A dictionary stores data as key-value pairs.

x = {"a": 1, "b": 2}

print(type(x))


# ============================================================
# 25. BOOLEAN (bool)
# ============================================================

# A boolean can have one of two values:
# True
# False

x = True
y = False

print(type(x))
print(type(y))


# ============================================================
# 26. NONE
# ============================================================

# None represents the absence of a value.

x = None

print(type(x))


# ============================================================
# 27. DUPLICATE VALUES IN A LIST
# ============================================================

# Lists allow duplicate values.

a = ["apple", "banana", "cherry", "apple"]

print(a)


# remove() removes one matching value at a time.

a.remove("apple")

print(a)


# We can remove the next occurrence by calling remove() again.

a.remove("apple")

print(a)


# pop() removes an element using its index.

a.pop(1)

print(a)



