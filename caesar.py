import string
from helpers import alphabet_position, rotate_character

def encrypt(text, rot):

    encrypted = ""

    for aletter in text:
        encrypted += rotate_character (aletter, rot)

    return encrypted

def main():
    text = input("Enter a message: ")
    rot = input("Enter a number: ")
    rot = int(rot)

    print(encrypt(text, rot))

if __name__ == "__main__":
    main()

