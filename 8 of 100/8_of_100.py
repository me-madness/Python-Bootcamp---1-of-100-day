# Day 8 Function with Inputs

def greet():
    print("Hello")
    print("how do you do?")
    print("Isn't the wather nice today?")

greet()


# Positional vs. Keyword Arguments
## Function that allows for input

def greet_with_name(name):
    print(f"Hello {name}")
    print("How do ypu do {name?")
    
greet_with_name("Angela")    


def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")
    
        
greet_with("Rangel", "Burgas")    


def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")
    
        
greet_with(name = "Rangel", locatiion = "Burgas")    


# Exercise - Pain Area Calculator

import math

def paint_calc(height, width, cover):
    test_h = int(input("Height of wall: "))
    test_w = int(input("Width of wall: "))
    coverage = 5
    num_of_cans = (test_h * test_w) / coverage
    print(f"You'll need {round(num_of_cans)} cans of paint")
    
paint_calc(height=test_h, width=test_w, cover=coverage)
  


# Exercise - Prime Number Checker

def prime():
    print("prime")
    
    
prime()    


# Caesar Cipher Part 1 - Encryption

def caesar_two():
    print("caesar two")
    print("Caesar_one")
    
caesar_two()



# Caesar Cipher Part 2 - Decryption

def caesar_three():
    print("caesar3")
    
    
caesar_three()


# Caesar Cipher Part 3 - Reorganising our Code


def caesar_four():
    print("caesar")
    
    
caesar_four()    

# Caesar Cipher Part 4 - User Experience Improvements _ Final Touches
def caesar_final(name):
    print(f"{name}")
    
    
caesar_final(name = "final")


