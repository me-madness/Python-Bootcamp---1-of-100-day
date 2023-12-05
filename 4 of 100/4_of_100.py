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

state_of_america[1] = "Pencilvania"

state_of_america.extend(["Angelaland", "Jack Bauer Land"])

print(state_of_america[1])

# Interactive Coding Exercise - Banker Roulette - Who will pay the bill

import random 

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

namesAsCSV = input("Give me everybody's names, seperated by a comma. ")

# Who will pay the bill

import random

name_string = input("Give me everybody's names, seperated by a comma. ")
names = name_string.split(", ")


num_items = len(names)

random_choice = random.randint(0, num_items - 1)

person_who_will_pay = names[random_choice]

print(f"{person_who_will_pay} is going to buy the meal today!")

# Working with nested lists

state_of_america = ["Delaware", "Pensilvania", "New Jersey", "Georgia"]  

num_of_state =len(state_of_america)
print(state_of_america[num_of_state])

# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Celery"]
vegetables= ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

# Interactive Coding Exercise - Treasure Map

row1 = [" "," "," "]
row2 = [" "," "," "]
row3 = [" "," "," "]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

horizontal = int(position[0])
vertical = int(position[1])

selected_row = map[vertical - 1]
selected_row[horizontal- 1] = "X"