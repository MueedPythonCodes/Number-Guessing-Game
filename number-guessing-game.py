import random
import os

logo='''
        _   ____  ____  _______  __________     ________  __________________ _____   ________   _________    __  _________
        / | / / / / /  |/  / __ )/ ____/ __ \   / ____/ / / / ____/ ___/ ___//  _/ | / / ____/  / ____/   |  /  |/  / ____/
       /  |/ / / / / /|_/ / __  / __/ / /_/ /  / / __/ / / / __/  \__ \\__ \ / //  |/ / / __   / / __/ /| | / /|_/ / __/   
      / /|  / /_/ / /  / / /_/ / /___/ _, _/  / /_/ / /_/ / /___ ___/ /__/ // // /|  / /_/ /  / /_/ / ___ |/ /  / / /___   
     /_/ |_/\____/_/  /_/_____/_____/_/ |_|   \____/\____/_____//____/____/___/_/ |_/\____/   \____/_/  |_/_/  /_/_____/   
                                                                                                                        
'''


RANDOM_NUM = random.randint(1,101)
# print(RANDOM_NUM)

print(logo)
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100")
level = input("Choose a difficulty.Type 'easy' or 'hard': ").lower()
attempts = 0
if level == "easy":
    attempts = 10
elif level == "hard":
    attempts = 5

flag = True


while flag:
    print(f"You have {attempts} attempts remaining for guess.")
    user_guess = int(input("Make a Guess: "))
    if user_guess == RANDOM_NUM:
        print("Congrats you have guessed the right number.You won.")
        flag = False
    elif user_guess > RANDOM_NUM:
        attempts -= 1
        print("Too high")
    elif user_guess < RANDOM_NUM:
        attempts -= 1
        print("Too low")
    
    if attempts == 0:
        print("You lose")
        flag = False
    

