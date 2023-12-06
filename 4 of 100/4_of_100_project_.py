# Project Rock Paper Scissors

import random
game_images = [rock, paper, scissors]

user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
print(game_images[user_choise])


computer_choice = random.randint(0, 2)
print(f"Computer chose:")

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")    
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("you lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's draw!")