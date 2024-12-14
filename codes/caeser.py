def caeser(plaintext,key):
    chiphertext=""
    for i in plaintext:
        if i.isalpha():
            cipher=chr((ord(i)-ord("A" if i.isupper() else"a" )+key)
            %26+ord("A" if i.isupper() else "a"))
            chiphertext += cipher
    return chiphertext