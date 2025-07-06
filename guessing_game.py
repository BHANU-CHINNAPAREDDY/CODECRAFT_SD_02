"""
Program that generates a random number and challenges the user to guess it. 
The program should prompt the user to input their guess, compare it to the generated number, and provide feedback if the guess is too high or too low. 
It should continue until the user correctly guesses the number and then display the number of attempts it took to win the game."""

import random

logo = r"""
 _    _      _                            _                           
| |  | |    | |                          | |                          
| |  | | ___| | ___ ___  _ __ ___   ___  | |_ ___                     
| |/\| |/ _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \                    
\  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) |                   
 \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/                    
                                                                      
                                                                      
 _____                     _               _____                      
|  __ \                   (_)             |  __ \                     
| |  \/_   _  ___  ___ ___ _ _ __   __ _  | |  \/ __ _ _ __ ___   ___ 
| | __| | | |/ _ \/ __/ __| | '_ \ / _` | | | __ / _` | '_ ` _ \ / _ \
| |_\ \ |_| |  __/\__ \__ \ | | | | (_| | | |_\ \ (_| | | | | | |  __/
 \____/\__,_|\___||___/___/_|_| |_|\__, |  \____/\__,_|_| |_| |_|\___|
                                    __/ |                             
                                   |___/                              
"""


print(logo)

def guess_the_number(random_number):

    chances_taken = 0
    game_over = False

    while not game_over:
        try:
            user_guess = int(input('Guess a number: '))
            chances_taken +=1

            if user_guess == random_number:
                game_over = True
                print(f"Congrats! You guessed the correct number {user_guess} in {chances_taken} attempts.")
            elif user_guess > random_number:
                print(f"Your guess is too high.")
            else:
                print("Your guess is too low.")
        except ValueError as err:
            print(f"Entered is not a number. {err}")


print("Let me think of a number between 1 and 100")
# Random number between 1 to 100.
random_number = random.randint(1,100)

# Calling the game function
guess_the_number(random_number)