lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def rotate_character(char, rot):
    newidx = 0
    if char in lowercase:
        idx = alphabet_position(char)
        newidx = idx + rot
        if newidx > 25:
            newidx = newidx % 26
        return lowercase[newidx]
    elif char in uppercase:
        idx = alphabet_position(char)
        newidx = idx + rot
        if newidx > 25:
            newidx = newidx % 26
        return uppercase[newidx]
    else:
        return char

def alphabet_position(letter):
    if letter in lowercase:
        return lowercase.index(letter)
    elif letter in uppercase:
        return uppercase.index(letter)
    else:
        return letter

def encrypt(text, rot):
    encrypted_message = ""
    for l in text:
        letter = rotate_character(l, rot)
        encrypted_message = encrypted_message + letter
        print(encrypted_message)
    return encrypted_message
