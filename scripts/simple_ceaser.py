import random

def toNum(char):
    return ord(char)

def toAlph(int):
    return chr(int)

def encrypt_ceaser(input, offset):
    #input.casefold()
    encrypted = ""
    for i in range(0,len(input)):
        if input[i] == ' ':         #Doesn't replace spaces
            encrypted += ' '
        elif toNum(input[i]) + offset >= 127:       #Bounds based around ASCII Table regular Characters
            newVal = toNum(input[i]) + offset - 94
            encrypted += toAlph(newVal)
        else:
            newVal = toNum(input[i]) + offset
            encrypted += toAlph(newVal)
        
        

    return encrypted

def decrypt_ceaser(input, offset):
    decrypted = ""
    for i in range(0,len(input)):
        if input[i] == ' ':     #Doesn't replace spaces
            decrypted += ' '
        elif toNum(input[i]) - offset <= 32:        #Bounds based around ASCII Table regular Characters
            newVal = toNum(input[i]) - offset + 94
            decrypted += toAlph(newVal)
        else:
            newVal = toNum(input[i]) - offset
            decrypted += toAlph(newVal)
        
        

    return decrypted


    