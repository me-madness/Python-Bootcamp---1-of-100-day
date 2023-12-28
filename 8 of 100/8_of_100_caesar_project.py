# Project Caesar 

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