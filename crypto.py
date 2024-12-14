#Cryptography & Security By Python
class Crypto:
    #Caeser cipher encryption and decryptio method
    def caeser(plaintext,key):
        chiphertext=""
        for i in plaintext:
            if i.isalpha():
                cipher=chr((ord(i)-ord("A" if i.isupper() else"a" )+key) %26+ord("A" if i.isupper() else "a"))
                chiphertext += cipher
        return chiphertext
    
    #Monoalphabetic cipher encryption method
    def moni_encryption(plaintext,key):
        cr_text=""
        for i in plaintext:
            if i.isalpha():
                i=i.lower()
                index=ord(i)-97
                chipher=key[index]
                cr_text += chipher
        return cr_text
    
    #Monoalphabetic cipher decryptio method
    def moni_decryption(ciphertext,key):
        plaintext=""
        for i in ciphertext:
            if i.isalpha():
                i=i.lower()
                index=key.index(i)
                plaintext+=chr(index+97)
        return plaintext
