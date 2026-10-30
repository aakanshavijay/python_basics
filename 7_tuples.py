# TUPLES
# A tuple is similar to a list because it can store multiple items in order. 
# The main difference is that a tuple cannot be modified in place after it has been created

rgb = (255, 100, 50)

print(rgb)  # (255, 100, 50)

# can be accessed by index
print(rgb[0])  # 255

#A tuple can also contain different types
book = ("Harry Potter", 1997, True)


days = ("Monday", "Tuesday", "Wednesday")
days[0] = "Sunday" #raises TypeError: 'tuple' object does not support item assignment

# a single value tuple must have a trailing comma, otherwise it is just a regular value
a = (5)
b = (5,)

print(type(a))  # <class 'int'>
print(type(b))  # <class 'tuple'>


#tuple methods
print(len(days))  # 3
print(days.count("Monday"))  # 1
print(days.index("Tuesday"))  # 1