#DICTIONARIES

#A dictionary stores information as key-value pairs.

contact = {
    "name": "Riya",
    "phone": "9876543210",
    "city": "Jaipur"
}

print(contact["name"])
print(contact["city"])

# why dictionaries are useful:
student_name = "Riya"
student_age = 14
student_city = "Jaipur"
student_marks = 92

#The dictionary groups information about one student under one variable
student = {
    "name": "Riya",
    "phone": "9876543210",
    }

#If the key does not exist, assigning a value creates a new entry.

#adding a new key-value pair to the dictionary
student["city"] = "Jaipur"
print(student)

#deleting a key-value pair from the dictionary
del student["phone"]
print(student)


student = {"name": "Riya", "marks": 92}
print(student["age"])
# this raises a KeyError because the key "age" does not exist in the dictionary.
# Use get() when the key may not exist:

print(student.get("age"))

#looping through a dictionary
for key in student:
    print(key)

for value in student.values():
    print(value)

# can also use the items() method to loop through both keys and values
for key, value in student.items():
    print(key, value)


marks = {
    "Riya": 92,
    "Aman": 78,
    "Kabir": 85,
    "Meera": 96
}
for name, mark in marks.items():
    print(name, "scored", mark)


#exercise: calculate the average marks of all students in the dictionary
total = 0
for mark in marks.values():
    total = total + mark

average = total / len(marks)
print("Class average:", average)


# Dictionary exercises
# 1. Create a dictionary containing a person's name, age, and city.
# 2. Print all keys and values in a dictionary.
# 3. Add a new subject and mark to a student's record.
# 4. Update the marks of a student.
# 5. Check whether a particular key exists.
# 6. Create a dictionary of five countries and their capitals.
# 7. Count how many times each character appears in a short word.
# 8. Store three students and their marks, then print the student with the highest marks.
# 9. Build a simple inventory containing product names and quantities.
# 10. Create a dictionary of favourite games and their genres.