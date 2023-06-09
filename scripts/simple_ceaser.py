import random

def toNum(char):
    return ord(char) - 97

def toAlph(int):
    return chr(int + 97)

def encrypt_ceaser(input, offset):
    #input.casefold()
    encrypted = ""
    for i in range(0,len(input)):
        # if input[i] == ' ':
        #     newVal = ord(' ')
        # elif toNum(input[i]) + offset >= 26:
        #     newVal = toNum(input[i]) + offset - 26
        #else:
        newVal = toNum(input[i]) + offset
        
        encrypted += toAlph(newVal)

    return encrypted

def decrypt_ceaser(input, offset):
    decrypted = ""
    for i in range(0,len(input)):
        # if input[i] == ' ':
        #     newVal = ord(' ')
        # elif toNum(input[i]) - offset < 0:
        #     newVal = toNum(input[i]) - offset + 26
        #else:
        newVal = toNum(input[i]) - offset
        
        decrypted += toAlph(newVal)

    return decrypted


if __name__ == '__main__':

    string = "Beef is my Favorite food"
    key = random.randint(0,25)

    print("Key: " + str(key))
    print("Input: " + string)
    encrypted = encrypt_ceaser(string, key)
    print("encrypted: " + encrypted)
    decrypted = decrypt_ceaser(encrypted, key)
    print("decrypted: " + decrypted)
    print(toNum('F'))