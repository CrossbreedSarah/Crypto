import string
from helpers import alphabet_position, rotate_character

def encrypt(message, encryptionkey):
    newtext = ''
    inxkey = 0

    for char in message:
        if char.isalpha():
            if inxkey > len(encryptionkey) - 1:
                inxkey = 0
            rotation_amount = alphabet_position(encryptionkey[inxkey])
            encrypted_letter = rotate_character(char, rotation_amount)
            newtext = newtext + encrypted_letter 
            inxkey += 1
            
        else:
           newtext += char
    return newtext
def main():
    message = input("Type a message:")
    key = input("Encryption key:")
    print(encrypt(message, key))
if __name__ == '__main__':
    main()
