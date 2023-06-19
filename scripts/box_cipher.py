
def box_encrypt(input):
    x = 1
    while x ** 2 < len(input):
        x += 1 
    

    box = [[' ' for i in range(x)] for j in range(x)]
    output = ""

    for i in range(0,x):
        for j in range(0,x):
            if x*i + j < len(input):
                
                box[i][j] = input[x*i + j]
                
            else:
                box[i][j] = ' '

    for i in range(x):
        for j in range(i):
            temp = box[i][j]
            box [i][j] = box[j][i]
            box[j][i] = temp

    for i in range(x):
        for j in range(x):
            output += box[i][j]

    
    return output



if __name__ == '__main__':

    string = "This technique doesn't use a key so it is kinda bad, oh well"
    print("Input: " + string)
    encrypted = box_encrypt(string)
    print("encrypted: " + encrypted)
    decrypted = box_encrypt(encrypted)
    print("decrypted: " + decrypted)
    