# SETS
# A set stores unique elements. Duplicate values are not retained.
# suppose we have a list of numbers with duplicates, we can convert it to a set to get only the unique values.

#Imagine collecting the names of every student who participated in a school competition. 
# Some students might participate in multiple rounds, 
# but we want each student's name to appear only once in the final collection.

participants = {
    "Riya",
    "Aman",
    "Riya",
    "Kabir",
    "Aman"
}

print(participants)


colours = {"red", "green", "blue"}
colours.add("yellow")
colours.add("red") # adding red again will not change the set since it already exists
print(colours)

colours.remove("green")

#Suppose two students have different collections of favourite games.
riya_games = {"chess", "Minecraft", "football"}
aman_games = {"football", "Minecraft", "cricket"}

print(riya_games & aman_games) #intersection of two sets

print(riya_games | aman_games) #union of two sets

print(riya_games - aman_games) #difference of two sets, returns elements in riya_games that are not in aman_games


empty_dictionary = {}
empty_set = set()
#The expression {} creates an empty dictionary, not an empty set. Python uses set() for an empty set.

#sets are unordered, meaning the order of elements is not guaranteed.
#use lists or tuples if you need to maintain the order of elements.



# all four collections:
# a school is organizing a sports day.

# A list of events in the order they will happen
events = ["Race", "Chess", "Football"]

# A tuple representing a fixed event time
event_time = (10, 30)

# A dictionary storing a student's details
student = {
    "name": "Riya",
    "house": "Blue",
    "points": 20
}

# A set of students who participated
participants = {"Riya", "Aman", "Kabir"}


# Tuple and set exercises
# 1. Create a tuple containing three favourite foods and print the second item.
# 2. Create a tuple containing the coordinates of a point.
# 3. Try changing an element in a tuple and observe the error.
# 4. Create a set containing repeated numbers and inspect the result.
# 5. Given two sets of favourite sports, find the sports they have in common.
# 6. Combine two sets of participants without duplicates.
# 7. Given a list of names, identify the unique names.
# 8. Check whether a particular item exists in a set.