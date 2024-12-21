def vigenere(plaintext,key):
    cipher_text=""
    if len(key)<len(plaintext):
        num=int(len(plaintext)/len(key)+1)
        key=key * num
    for i in range(len(plaintext)):
        cipher=chr((ord(plaintext[i])+ord(key[i]))%256)
        cipher_text += cipher
    return cipher_text
