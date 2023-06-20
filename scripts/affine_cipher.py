class Affine:
   DIE = 128
   def __init__(self, k1, k2):
      a = k1
      c = self.DIE
      b = 1
  
      while (a*b)%c != 1:
        b += 1
        if b > c ** 2:
           print("ERROR: Pick key not co-factor of 128")
           break

      self.KEY = (k1, k2, b)
      
   def encryptChar(self, char):
      K1, K2, kI = self.KEY
      return chr((K1 * ord(char) + K2) % self.DIE)
		
   def encrypt(self, string):
      return "".join(map(self.encryptChar, string))
   
   def decryptChar(self, char):
      K1, K2, KI = self.KEY
      return chr(KI * (ord(char) - K2) % self.DIE)
   
   def decrypt(self, string):
      return "".join(map(self.decryptChar, string))


affine = Affine(93874290875, 12)
encrypted = affine.encrypt('Affine Cipher')
print(affine.encrypt('Affine Cipher'))
print(affine.decrypt(encrypted))
