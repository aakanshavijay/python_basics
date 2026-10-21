#sometimes one condition is not enough 

#and operator: both conditions must be true for the whole condition to be true
age = 15
registered = True

if age >= 13 and registered:
    print("You can enter.")

#or operator: at least one condition must be true for the whole condition to be true
age = 15
registered = False 

if age >= 13 or registered:
    print("You can enter.")

#eg
# if is_student or is_senior:
#     print("Discount available")

#not operator: reverses the result of the condition
is_student = True
print(not is_student) #False

#real world example
is_raining = True
if not is_raining:
    print("You can go outside.")

#combining multiple operators
age = 15
registered = True
if (age >= 13 and registered) or (age >= 18):
    print("You can enter.")

#NESTED CONDITIONS
# a nested condition is a condition inside another condition

age = 15
has_ticket = True

if age >= 13:
    if has_ticket:
        print("You can enter.")
    else:
        print("You need a ticket.")
else:
    print("You are too young.")

#another example of nested conditions
age = 15
if age >= 13:
    print("You can create a social media account.")
    if age < 18:
        print("You need parental consent.")
    else:
        print("You do not need parental consent.")
else:
    print("You cannot create a social media account.")

# no need to overuse nested conditions, try to keep your code simple and readable
if age >= 13 and has_ticket:
    print("You can enter.")


#project to give as homework. Need to make a decision tree for it first and then implement it in python.
#rock paper scissors game 
# player1 = input("Player 1: ")
# player2 = input("Player 2: ")

# if player1 == player2:
#     print("Draw")
# elif player1 == "rock" and player2 == "scissors":
#     print("Player 1 wins")
# ...