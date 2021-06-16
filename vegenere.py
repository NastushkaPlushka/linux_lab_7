#!/usr/bin/python
# -*- coding: utf-8 -*-
def incript(s, key):
    n1 = [i for i in s]
    n2 = [key[i % len(key)] for i in range(len(n1))]
    n3 = [chr((ord(n1[i]) + ord(n2[i]))) for i in range(len(n1))]
    return ''.join(n3)


def decript(s, key):
    n1 = [i for i in s]
    n2 = [key[i % len(key)] for i in range(len(n1))]
    n3 = [chr((ord(n1[i]) - ord(n2[i]))) for i in range(len(n1))]
    return ''.join(n3)


msg = "хочу кушать"
key = 'password'
ciphers = incript(msg, key)
ancipers = decript(ciphers, key)
print("Зашифрованное",ciphers)
print("Расшифрованное",ancipers)

