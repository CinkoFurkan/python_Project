#from art import logo 
import random

#print(logo)

print("I'm thinking of a number between 1 and 100 ")
numbers = list(range(1, 101))  # Using list(range()) for generating numbers 1 to 100 inclusively.

chosen_number = random.choice(numbers)

difficulty = input("Choose a difficulty, type easy or hard: ").lower()

if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5
else:
    print("Invalid difficulty level. Please choose either 'easy' or 'hard'.")
    exit()

for _ in range(attempts):
    print(f"You have {attempts} attempts remaining to guess the number")
    guess = int(input("Make a guess: "))
    if guess < chosen_number:
        print("Too low")
    elif guess > chosen_number:
        print("Too high")
    else:
        print(f"Congratulations! You've guessed the number {chosen_number} correctly!")
        break  # End the game since the number is guessed correctly
    attempts -= 1  # Reduce the number of attempts

if attempts == 0:
    print(f"Sorry, you've run out of turns. The correct number was {chosen_number}.")
