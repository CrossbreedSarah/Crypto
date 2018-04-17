import string 
def alphabet_position(letter):
    if letter in string.ascii_uppercase:
        position = string.ascii_uppercase.find(letter)
    
    elif letter in string.ascii_lowercase:
        position = string.ascii_lowercase.find(letter)
        
    return position
    
def rotate_character(char, rot):
    import string
    if char in string.digits or char in string.punctuation or char in string.whitespace:
        return char
    index = alphabet_position(char) + rot
    if index > 25:
        index = index % 26
    if char in string.ascii_lowercase:
        lcl = string.ascii_lowercase
        newchar = lcl[index]
        return newchar
    if char in string.ascii_uppercase:
        ucl = string.ascii_uppercase
        newchar = ucl[index]
        return newchar