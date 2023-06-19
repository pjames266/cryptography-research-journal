import random

def toNum(char):
    return ord(char) - 65

def toAlph(int):
    return chr(int + 65)

def encrypt_ceaser(input, offset):
    #input.casefold()
    encrypted = ""
    for i in range(0,len(input)):
        if input[i] == ' ':
            encrypted += ' '
        elif toNum(input[i]) + offset >= 57:
            newVal = toNum(input[i]) + offset - 57
            encrypted += toAlph(newVal)
        else:
            newVal = toNum(input[i]) + offset
            encrypted += toAlph(newVal)
        
        

    return encrypted

def decrypt_ceaser(input, offset):
    decrypted = ""
    for i in range(0,len(input)):
        if input[i] == ' ':
            decrypted += ' '
        elif toNum(input[i]) - offset <= 0:
            newVal = toNum(input[i]) - offset + 57
            decrypted += toAlph(newVal)
        else:
            newVal = toNum(input[i]) - offset
            decrypted += toAlph(newVal)
        
        

    return decrypted


    