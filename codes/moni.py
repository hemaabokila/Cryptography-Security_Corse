def moni_encryption(plaintext,key):
    cr_text=""
    for i in plaintext:
        if i.isalpha():
            i=i.lower()
            index=ord(i)-97
            chipher=key[index]
            cr_text += chipher
    return cr_text

def moni_decryption(ciphertext,key):
    plaintext=""
    for i in ciphertext:
        if i.isalpha():
            i=i.lower()
            index=key.index(i)
            plaintext+=chr(index+97)
    return plaintext
