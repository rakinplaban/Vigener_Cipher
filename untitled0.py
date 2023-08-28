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
            text = chr((ord(plainText[i]) - ord('A')) + ord(key[i % len(key)])) 
            encrypt += text
        else:
            encrypt += plainText[i]
    return encrypt


plaintext = "HELLO"
keyword = "KEY"

encrypted_text = encrypt(plaintext, keyword)
print("Encrypted:", encrypted_text)