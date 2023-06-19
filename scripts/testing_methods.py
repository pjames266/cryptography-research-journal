import box_cipher
import simple_ceaser
import random

if __name__ == '__main__':

    string = "James is good at programming and didn't make mistakes"
    key = random.randint(0,56) #Can replace for a specific key

    print("Key: " + str(key))
    
    print("Input: " + string)
    print()
    encrypted = box_cipher.box_encrypt(string)
    print("encrypted box: " + encrypted)
    decrypted = box_cipher.box_encrypt(encrypted)
    print("decrypted box: " + decrypted)
    print()
    
    encrypted = simple_ceaser.encrypt_ceaser(string, key)
    print("encrypted ceaser: " + encrypted)
    decrypted = simple_ceaser.decrypt_ceaser(encrypted, key)
    print("decrypted ceaser: " + decrypted)
    print()

    encrypted = box_cipher.box_encrypt(string)
    print("encrypted box: " + encrypted)
    encrypted = simple_ceaser.encrypt_ceaser(encrypted, key)
    print("encrypted box & ceaser: " + encrypted)

    decrypted = simple_ceaser.decrypt_ceaser(encrypted, key)
    print("decrypted ceaser: " + decrypted)
    decrypted = box_cipher.box_encrypt(decrypted)
    print("decrypted ceaser & box: " + decrypted)