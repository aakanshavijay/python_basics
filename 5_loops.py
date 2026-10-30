# loops allows you to repeat a block of code multiple times. There are two main types of loops in Python: for loops and while loops.

# FOR LOOPS
# A for loop is used to iterate over a sequence (like a list, tuple, dictionary, set, or string) and 
# execute a block of code for each item in the sequence.

#it is useful when you know beforehand how many times you want to execute a statement or a block of statements.


#basic syntax of a for loop:
# for variable in sequence:
#     # block of code to be executed


for number in range(5):
    print(number)

# three ways to use range() function:
# 1. range(stop) - generates numbers from 0 to stop-1
# 2. range(start, stop) - generates numbers from start to stop-1
# 3. range(start, stop, step) - generates numbers from start to stop-1, incrementing by step

# can also count backwards

for i in range(5, 0, -1):
    print(i)

print("Go!")


# arithematic operations can be performed inside the loop
# printing multiplication table of a number

for i in range(1, 11):
    print(7, "x", i, "=", 7 * i)


#calculate sum of numbers from 1-5
total = 0
for number in range(1, 6):
    total = total + number

print("Total:", total)


# WHILE LOOPS
p
# example: "Keep asking the player to enter a password while the password is incorrect."

# syntax of a while loop:
# while condition:
#     # block of code to be executed

#example of a while loop:
count = 1

while count <= 5:
    print(count)
    count = count + 1 # what happens if we don't increment the count variable (infinite loop)


password = "secret"
user_input = ""
while user_input != password:
    user_input = input("Enter the password: ")
    if user_input == password:
        print("Access granted!")
    else:
        print("Incorrect password. Try again.")


# break statement can be used to exit a loop prematurely
# imagine searching for a particular name in a list. Once the name is found, there may be no reason to continue searching

names = ["Alice", "Bob", "Charlie", "David", "Eve"]

for name in names:
    if name == "Charlie":
        break
    print(name)


for number in range(1, 11):
    if number == 6:
        break

    print(number)


#continue statement can be used to skip the current iteration of a loop and move on to the next iteration
# imagine you want to print all numbers from 1 to 10, but skip the number 5

for number in range(1, 11):
    if number % 2 == 0:
        continue

    print(number)


# exercises:
# Print the numbers from 1 to 20.
# Print all even numbers between 1 and 50.
# Print the multiplication table of a number entered by the user.
# Calculate the sum of all numbers from 1 to 100.
# Count backwards from 10 to 1, then print "Blast off!".
# Keep asking the user for a number until they enter 0.
# Ask the user to enter five numbers and count how many are positive.
# Create a game that gives the player three chances to guess a secret number.
# Print all numbers between 1 and 100 that are divisible by both 3 and 5.
# Calculate the factorial of a positive integer using a loop.