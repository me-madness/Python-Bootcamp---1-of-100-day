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
    num_of_cans = (test_h * test_w) / coverage
    print(f"You'll need {math.ceil(num_of_cans)} cans of paint.")
    
    
    
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
  


# Exercise - Prime Number Checker

def prime_checker(n):
    if n == 1:
        print(n, "it's not a prime number")
    elif n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                print(n, "it's not a prime number")
                break
        else:
            print(n, "it's a prime number")
    else:
        print(n, "it's not a prime number")
     
                    
n = int(input("Check this number: "))
prime_checker(number=n)
    


# Caesar Cipher Part 1 - Encryption

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your mesage:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        cipher_text = alphabet[new_position]
    print(f"The encoded text is {cipher_text}") 
    
       
encrypt(plain_text=text, shift_amount=shift)

        
# Caesar Cipher Part 2 - Decryption

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your mesage:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        cipher_text = alphabet[new_position]
    print(f"The encoded text is {cipher_text}") 
    
       
encrypt(plain_text=text, shift_amount=shift)

def decrypt(cipher_text, shift_amount):
    plaint_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        plaint_text += alphabet[new_position]
    print(f"The decoded text is {plaint_text}") 
    
       
decrypt(cipher_text=text, shift_amount=shift)


if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)   
elif direction == "encode":
    decrypt(cipher_text=text, shift_amount=shift)
else:
    print("The type it's not correct, please try again.")


# Caesar Cipher Part 3 - Reorganising our Code


def caesar_three():
    print("caesar")
    
    
caesar_three()    

# Caesar Cipher Part 4 - User Experience Improvements _ Final Touches
## 8_of_100_caesar_project.py


