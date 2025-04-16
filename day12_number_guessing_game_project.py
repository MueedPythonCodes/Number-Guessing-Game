import random
import os

logo='''
        _   ____  ____  _______  __________     ________  __________________ _____   ________   _________    __  _________
        / | / / / / /  |/  / __ )/ ____/ __ \   / ____/ / / / ____/ ___/ ___//  _/ | / / ____/  / ____/   |  /  |/  / ____/
       /  |/ / / / / /|_/ / __  / __/ / /_/ /  / / __/ / / / __/  \__ \\__ \ / //  |/ / / __   / / __/ /| | / /|_/ / __/   
      / /|  / /_/ / /  / / /_/ / /___/ _, _/  / /_/ / /_/ / /___ ___/ /__/ // // /|  / /_/ /  / /_/ / ___ |/ /  / / /___   
     /_/ |_/\____/_/  /_/_____/_____/_/ |_|   \____/\____/_____//____/____/___/_/ |_/\____/   \____/_/  |_/_/  /_/_____/   
                                                                                                                        
'''
GUESS=random.randint(1,100)

end=True

def start_playing(i):
    """Checks while you have guessed right number or not"""           # This is a docstring that tells what this function will do
    while i>0:
        print(f"You have {i} attempts to guess the write number")
        user_guess=int(input("Make a guess: "))
        i -= 1
        if user_guess==GUESS:
            print(f"You have guessed the right number.The answer is {user_guess}")
            print("Congrats you win")
            break
        elif user_guess > GUESS:
            print("Too high")
            print("Try Again")
        elif user_guess < GUESS:
            print("Too low")
            print("Try Again")

    if user_guess!=GUESS:
        print("You have lost all the lives. You lose")
        print(f"The number I have guessed is {GUESS}") 
    
    extra_fun=input("Enter yes to Play the Game again or Enter stop to Exit the Game: ").lower()
    if extra_fun=='yes':
        os.system('cls')
        number_guess()
    elif extra_fun=='stop':
        os.system('cls')
        print("GAME OVER")
        end=False


def number_guess():
    print(logo)
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    type=input("Choose a difficulty.Type 'easy' or 'hard':").lower()
    if type=='easy':
        i=10
        start_playing(i)
    elif type=='hard':
        i=5
        start_playing(i)
    else:
        print("Invalid Entry")
        


number_guess()