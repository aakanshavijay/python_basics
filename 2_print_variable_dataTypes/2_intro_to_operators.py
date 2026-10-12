#string

print(10)
print("10")

print(type(10))
print(type("10"))

#booleans
True
False

print(type(True))
print(type(False))

print(2 > 3)
print(4 < 10)

#type conversion
age = int("15")
price = float("99.50")
age = 15
message = "I am " + str(age) + " years old"

#value vs text
print(10 + 5) #int
print("10" + "5") #str

#operators

#arithematic operators
'''
+
-
* 
/
%
'''

#comparison operators
'''
>
<
>=
<=
==
!=
'''

#input
name = input("What is your name? ")
print("Hello, " + name)

#check type of an input number to find out its a string not a number
#try adding 1 to it to see it gives error


#mini project
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

#mini project- age calculator
birth_year = int(input("What year were you born? "))
current_year = 2026

age = current_year - birth_year

print("You are approximately", age, "years old.")

#home work
# 1. tip calculator
# ask the user for the bill amount and the tip percentage. 
# Calculate the tip amount and the total bill (bill + tip). Print the results.

# 2. pocket money calculator
# ask the user for their age and how much pocket money they receive per week.
# Calculate how much pocket money they will receive in a year (52 weeks). Print the result
