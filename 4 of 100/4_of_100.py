# Randomisation
import random


random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random() * 5
print(random_float)

love_score = random.randint(1, 10)
print(f"Your love score is {love_score}")

# Random
import random
 
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

random_side = random.randint(0, 1)
if random_side == 1:
    print("Heads")
else:
    print("Tails")    
    
# Python List

state_of_america = ["Delaware", "Pensilvania", "New Jersey", "Georgia"]  

print(state_of_america[1])

# Interactive Coding Exercise - Banker Roulette - Who will pay the bill

import random 

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

namesAsCSV = input("Give me everybody's names separet by a comma. ")