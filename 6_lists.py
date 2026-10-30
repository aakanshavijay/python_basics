# COLLECTIONS

#Suppose a teacher needs to store the marks of five students.
#One approach is to create five variables
#This works for five students, but what if there are 50 students? Or 500?

#A collection lets us group multiple values under one variable name.

# Python provides several collection types, each useful for a different purpose:
# - List: a collection of items that can be changed.
# - Tuple: a collection of items that cannot be changed after creation.
# - Dictionary: a collection that stores key-value pairs.
# - Set: a collection of unique values, without duplicate elements.


#LISTS
# A list stores multiple items in a single variable. 
# Lists are written using square brackets [], with commas separating the elements.

fruits = ["apple", "banana", "mango"]

# Lists can contain numbers, strings, booleans, and even a mixture of data types.

# indexing, the first item has index 0, the second item has index 1, and so on.
# negative indexing starts from the end of the list, with -1 being the last item, -2 being the second last item, and so on.

print(len(fruits))

# content of the list can be changed- this property is called mutability. We can add, remove, or change items in a list.

#updating an item in a list
fruits[1] = "orange"
print(fruits)

#adding an item to a list
fruits.append("grape")
print(fruits)

#inserting an item at a specific index
fruits.insert(1, "kiwi")
print(fruits)

#removing an item from a list
fruits.remove("mango")
print(fruits)

#popping an item from a list (removes the last item by default)
fruits.pop()
print(fruits)

# The distinction is useful:
# - remove(value) removes by value.
# - pop(index) removes by position and returns the removed item.

fruits.sort() # sorts the list in ascending order
fruits.reverse() # reverses the order of the list

# in operator checks if an item exists in the list
if "apple" in fruits:
    print("Apple is in the list.")

print("banana" in fruits)


#iterating over a list

#one approach is
fruits = ["apple", "banana", "mango"]

print(fruits[0])
print(fruits[1])
print(fruits[2])

#using a loop instead
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)

#iterating over numbers and calculating a total
marks = [80, 90, 75, 85, 95]
total = 0

for mark in marks:
    total = total + mark

print("Total marks:", total)
print("Average:", total / len(marks))

#lists and conditions

#find all marks greater than or equal to 80.
marks = [65, 82, 91, 74, 88, 56]

for mark in marks:
    if mark >= 80:
        print(mark)


#check how many students passed assuming the passing mark is 50.
marks = [35, 67, 42, 29, 80, 55]
passed = 0

for mark in marks:
    if mark >= 40:
        passed = passed + 1

print("Students who passed:", passed)

#slicing a list
#slicing allows us to extract a portion of a list by specifying a start and end index
fruits = ["apple", "banana", "mango", "kiwi", "grape"]
print(fruits[1:4]) # prints items from index 1 to 3

numbers = [10, 20, 30, 40, 50, 60]

print(numbers[:3])   # [10, 20, 30]
print(numbers[3:])   # [40, 50, 60]
print(numbers[::2])  # [10, 30, 50]
print(numbers[::-1]) # [60, 50, 40, 30, 20, 10]


# List exercises
# 1. Create a list of five favourite movies and print each one.
# 2. Create a list of ten numbers and print its length.
# 3. Find the largest number in a list without using max().
# 4. Calculate the sum and average of a list of marks.
# 5. Ask the user to enter five fruits and store them in a list.
# 6. Check whether a particular name exists in a list.
# 7. Count how many numbers in a list are greater than 50.
# 8. Create a list of numbers and make a second list containing only the even numbers.
# 9. Find how many times a particular value appears in a list.
# 10. Remove duplicate values from a list while preserving the original order.