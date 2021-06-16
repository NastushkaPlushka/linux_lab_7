#!/usr/bin/python
# -*- coding: utf-8 -*-
def encrypt(m, key):
    s1=[]
    s2=[]
    for i in m:
        s1.append((ord(i)+key)%65536) 
    for i in range(len(s1)):
        s2.append(chr(s1[i]))
    cipher = ''.join(s2)
    return cipher

def decrypt(cipher, key):
    s1=[]
    s2=[]
    for i in cipher:
        s1.append((ord(i)-key)%65536) 
    for i in range(len(s1)):
        s2.append(chr(s1[i]))
    m = ''.join(s2)
    return m

def hack(cipher):
    number =[]
    for i in range(len(cipher)):
        number.append([cipher.count(cipher[i]),cipher[i]])
        max=0
        for j in range(len(number)):
            if number[j][0] > max:
                max=number[j][0]
                elmax=number[j][1]
    key=ord(elmax)-ord(' ')%256
    s1=[]
    s2=[]
    for i in cipher:
        s1.append((ord(i)-key)%256) 
    for i in range(len(s1)):
        s2.append(chr(s1[i]))
    str=''.join(s2)   
    return str

msg = "хочу кушать"
key = "password"
ciphers = encrypt(key,msg)
ancipers = decrypt(key,ciphers)
ancipers_with_hack = hack(ciphers)
print("Исходное",msg)
print("Зашифрованное",ciphers)
print("Расшифрованное",ancipers)
print("Расшифрованые без помощи ключа",ancipers_with_hack)