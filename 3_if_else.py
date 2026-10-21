#decisions and logic

# eg. if it is raining, then take an umbrella
# eg. if it is sunny, then wear sunglasses
# eg. if it is snowing, then wear a coat
# eg. if my salary is greater than 1000, then I will buy a new phone

#similar conditions in python

#comparison operators
'''
>
<
>=
<=
==
!=
'''

#eg. if my age is greater than or equal to 13, then I can create a social media account
age = 15
print(age >= 13)

#thus, python can make decisions based on conditions using if statements
if age >= 13:
    print("You can create a social media account")
else:
    print("You cannot create a social media account")

# also notice indentation in python


#if the condition is not met, then we can use else statement to execute a different block of code
age = 10
if age >= 13:
    print("You can create a social media account")
else:
    print("You cannot create a social media account")

#we can also use elif statement to check for multiple conditions
#real world decisions often have multiple conditions
age = 15
if age < 13:
    print("You cannot create a social media account")
elif age >= 13 and age < 18:
    print("You can create a social media account with parental consent")
else:
    print("You can create a social media account without parental consent")

#eg
score = 82

if score >= 90:
    print("Excellent")
elif score >= 75:
    print("Good")
elif score >= 50:
    print("Pass")
else:
    print("Fail")

#the order of conditions matters as python checks conditions from top to bottom
#see by changing the sequence of conditions and see how the output changes

#mini project 
# design a grade calculator that takes marks as input and gives the grade as output
# based on average marks

