# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 20:39:47 2023

@author: Rakin Shahriar
"""

def encrypt(plainText, key):
    encrypt = ''
    key = key.upper()
    plainText = plainText.upper()
    
    for i in range(len(plainText)):
        if plainText[i].isalpha():
            text = chr((((ord(plainText[i]) - ord('A')) + (ord(key[i % len(key)])-ord('A')))%26) + ord('A'))
            encrypt += text
        else:
            encrypt += plainText[i]
    return encrypt

def decrypt(cipher, key):
    plain_text = ''
    key = key.upper()
    plainText = cipher.upper()
    
    for i in range(len(plainText)):
        if plainText[i].isalpha():
            idx = (ord(plainText[i]) - ord('A')) - (ord(key[i % len(key)])-ord('A'))
            text = chr((idx+26)%26 + ord('A'))
            plain_text += text
        else:
            plain_text += plainText[i]
    
    return plain_text


plaintext = input("Please enter your message: ")
keyword = input("Now enter key: ")

encrypted_text = encrypt(plaintext, keyword)
print("Encrypted:", encrypted_text)
decrypted_text = decrypt(encrypted_text, keyword)
print("Decrypted:", decrypted_text)