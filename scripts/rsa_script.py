import math

def extendedGCD(a, b):
 
    if a == 0: 
        return b, 0, 1
            
    gcd, s1, t1 = extendedGCD(b%a, a)

    s,t = updateCoeff(a,b,s1,t1)
    
    return gcd, s, t

def updateCoeff(a,b,s,t):
    return (t - (b//a) * s, s) 


class RSA:
    
    def __init__(self,p1,p2):
        self.p1 = p1    #Prime 1
        self.p2 = p2    #prime 2
        self.max = p1*p2    #max result for cycle
        n = (p1-1)*(p2-1)   #phi value

        b = 2               #finding Public Key
        while b < n:
            if math.gcd(b,n) == 1:
                break
            else:
                b+=1
        self.public = b

        b = 2               #finding private key
        while b < n and (self.public * b) % n != 1:
                b+=1

        self.private = b

    def get_max(self):      #returns max/cycle value (required by others for encryption to you)
        b = self.max
        return int(b)
    
    def get_public(self):      #returns public key value (required by others for encryption to you)
        b = self.public
        return int(b)
    
    def encrypt_self (self, string):           #encrypt message for yourself
        str = ""
        for i in range(len(string)):
            str += self.encryptChar(string[i],self.public,self.max)
        return str
    
    def encrypt_other (self, string, key, max):           #encrypt message for yourself
        str = ""
        for i in range(len(string)):
            str += self.encryptChar(string[i],key,max)
        return str
    
    def encryptChar(self, char, key, max):
        o = ord(char)
        p = ord(char)
        #print(o)
        for i in range(key-1):
            p = (o*p)%max

            #print(p)
        #print()
        return chr(p)

    def decrypt (self, string):
        return "".join(map(self.decryptChar, string))
    
    def decryptChar(self, char):
        key = self.private
        o = ord(char)
        p = ord(char)
        for i in range(key-1):
            p = (o*p)%self.max
        #print(p)
        return chr(p)

    
if __name__ == "__main__":
    rsa = RSA(137,197)
    print(rsa.get_max())
    print(rsa.get_public())
    encrypted = rsa.encrypt_self("JAMES IS AWESOME!!!! right?")
    print(encrypted)
    decrypted = rsa.decrypt(encrypted)
    print(decrypted)