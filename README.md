# Cryptography Research Journal

This is research is being conducted out of personal interest during  Fridays while working for Selkirk's Applied Research and innovation Centre. The goal is that this research can be potentially conducted and written in a way to provide instruction on the Advanced Computing Wiki.

Cryptography is a method of protecting information and communications through the use of codes, so that only those for whom the information is intended can read and process it. For modern computing cryptography is used for communication over the internet as well as file storage.

## Symmetric Encryption
- Same key is used for both encryption and decryption
- Enigma
- Caesar Cipher

### Advanced Encryption Standard (AES)
  - National Institute of Standards and Technology (NIST) in 2001.
  - Works with 128 Bit blocks
  - 4x4 grid of bytes
  
  
  |0   |1    |2    |3   |
  |:---|:---:|:---:|---:|
  |4   |5    |6    |7   |
  |8   |9    |10   |11  |
  |12  |13   |14   |15  |
  

  - required use of 128, 192, or 256 bit keys 
  - Prevented brute force decryption as would take too long
  - Balanced encryption security with minimal encryption and decryption time for intended publishers/receivers
  - Steps within each round (mix columns not in last round)
    - 1. Plaintext XOR with key
    - 2. Sub Bytes
    - 3. Shift Rows
    - 4. Mix Columns
    - 5. Add Normal Key
  - 128 bit key -> 10 rounds, 192 bit key -> 12 rounds, 256 bit key -> 14 rounds
  
  ![](https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/AES_%28Rijndael%29_Round_Function.png/375px-AES_%28Rijndael%29_Round_Function.png)
#### Round Function Visulization

  - Easily reversible with knowledge of key
  - [Video](https://www.youtube.com/watch?v=O4xNJsjtN6E)
  - Quantum Resistant because no public key
  - Most Websites use 128 bit but stuff to stay encrypted for sure for 30+years uses 256 bit AES


### 3DES Encryption

3DES (Triple Data Encryption Standard) is a symmetric encryption algorithm that is derived from the original Data Encryption Standard (DES) algorithm. It is a block cipher that operates on blocks of data and uses a combination of symmetric key operations to provide encryption and decryption.

3DES applies the DES algorithm three times to each data block, using a different key for each iteration. The algorithm is structured as follows:

1. Key Generation: Three independent keys, typically of 56 bits each, are generated or derived.

2. Encryption: The data block is divided into smaller blocks, typically 64 bits in size. Each block undergoes the following process:
   a. The block is encrypted using the first key using the DES algorithm.
   b. The resulting ciphertext is then decrypted using the second key using the DES algorithm.
   c. The intermediate result is then encrypted again using the third key using the DES algorithm.
   d. The final ciphertext is the output of the third encryption.

3. Decryption: The decryption process is the reverse of the encryption process. The ciphertext is decrypted using the third key, then encrypted using the second key, and finally decrypted using the first key.

By applying DES three times in this manner, 3DES provides increased security compared to the original DES algorithm. It effectively uses a key length of 168 bits (56 bits x 3) while retaining compatibility with the existing DES infrastructure.

However, it's important to note that 3DES is now considered relatively weak for modern cryptographic standards due to its key size and computational limitations. It has been largely replaced by more secure and efficient symmetric encryption algorithms such as AES (Advanced Encryption Standard).

## Asymmetric Encryption
- Has a public key known to all as well as a private key, ie. different key decrypts than encrypts.
![](https://www.usna.edu/Users/cs/wcbrown/courses/si110AY13S/lec/l26/asymmetricencryption.png)
### RSA Algorithm (Rivest, Shamir, Adleman)
  - Currently used with private and public keys were public keys are the product of 2 large prime private keys 
  - Knowing a public key cannot tell you the private key, numbers are too large and there are too many other factors, would take millions of years with the best methods of factoring.
  - used by HTTPS and SSH
  - When data is sent it is encrypted with their public key so only they can decrypt it  

### Diffie-Hellman Key Exchange
  - Works using Mathmatical one way functions
  - B^x Mod(M) = R
  - x is kept as some secret key for each user
  - B and M are constant between them
  - The R values calculated by each user is sent to the other
  - Raising this received value to the power of their own x creates the same shared key as (B^y mod(M))^x = (B^x mod(M))^y = **B^xy mod(M)** <- shared key
  - Secret shared key used for Symmetric Encryption
  ![](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Public_key_shared_secret.svg/375px-Public_key_shared_secret.svg.png)


## SSL/TLS Protocols

Transport Layer Security (TLS) is based on the Secure Socket Layer (SSL) protocol that was developed in the 1990s by the Netscape Corporation. SSL/TLS uses both asymmetric and symmetric encryption to protect the confidentiality and integrity of data-in-transit. Asymmetric encryption is used to establish a secure session between a client and a server, and symmetric encryption is used to exchange data within the secured session. 

TLS is most commonly used with HTTP to make it secure (HTTPS)

A website must have an SSL/TLS certificate for their web server/domain name to use SSL/TLS encryption. Once installed, the certificate enables the client and server to securely negotiate the level of encryption in the following steps:

1. The client contacts the server using a secure URL (HTTPS…).
2. The server sends the client its certificate and public key.
3. The client verifies this with a Trusted Root Certification Authority to ensure the certificate is legitimate.
4. The client and server negotiate the strongest type of encryption that each can support.
5. The client encrypts a session (secret) key with the server’s public key, and sends it back to the server.
6. The server decrypts the client communication with its private key, and the session is established.
7. The session key (symmetric encryption) is now used to encrypt and decrypt data transmitted between the client and server.

Both the client and server are now using HTTPS (SSL/TLS + HTTP) for their communication. Web browsers validate this with a lock icon in the browser address bar. HTTPS functions over Port 443.

![](https://thumbs.dreamstime.com/b/internet-security-concept-ssl-https-lock-symbol-computer-browser-laptop-screen-151635340.jpg)

Once you leave the website, those keys are discarded. On your next visit, a new handshake is negotiated, and a new set of keys are generated.

Depending on the version of TLS/SSL different symmetric and asymmetric algorithms can be used. Some TLS versions can use RSA for its key exchange and handshake while other versions use Diffie-Hellman. Versions of TLS also use AES or 3DES for its symmetric encryption bulk data transfers.

