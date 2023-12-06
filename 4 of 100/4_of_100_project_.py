# Project Rock Paper Scissors

import random

user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

computer_choice = random.randint(0, 2)
print(f"Computer chose {computer_choice}")