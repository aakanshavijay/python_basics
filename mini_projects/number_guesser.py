# How the game works
# 1. The computer chooses a random number from 1 to 20.
# 2. The player enters a guess.
# 3. The program says whether the guess is too low or too high.
# 4. The loop repeats until the player guesses correctly.
# 5. The program displays the number of attempts.

import random

secret_number = random.randint(1, 20)
attempts = 0

guess = 0

while guess != secret_number:
    guess = int(input("Guess a number between 1 and 20: "))
    attempts = attempts + 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("You guessed it!")
        print("Attempts:", attempts)

#added challenges
# Challenges
# 1. Restrict the player to five attempts.
# 2. Display "Game over!" if the player runs out of attempts.
# 3. Ask the player whether they want to play again.

#new code with challenges implemented
import random

secret_number = random.randint(1, 20)
attempts = 0
max_attempts = 5

while attempts < max_attempts:
    guess = int(input("Guess a number between 1 and 20: "))
    attempts = attempts + 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("You guessed it!")
        print("Attempts:", attempts)
        break
else:
    print("Game over! You ran out of attempts.")
    print("The number was:", secret_number)

# Ask the player whether they want to play again
play_again = input("Do you want to play again? (yes/no): ")
if play_again.lower() == "yes":
    # Restart the game
    pass