#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    @author: Mr.Un1k0d3r RingZer0 Team
    @package: core/rc4.py
"""
import os
import re

class RC4:

    def __init__(self, key):
        self.key = [ord(c) for c in key]

    def KSA(self):
        keylength = len(self.key)
        S = range(256)
        j = 0
        for i in range(256):
            j = (j + S[i] + self.key[i % keylength]) % 256
            (S[i], S[j]) = (S[j], S[i])
        return S

    def PRGA(self, S):
        i = 0
        j = 0
        while True:
            i = (i + 1) % 256
            j = (j + S[i]) % 256
            (S[i], S[j]) = (S[j], S[i])
            K = S[(S[i] + S[j]) % 256]
            yield K

    def crypt(self, data):
        output = ''
        self.S = self.KSA()
        self.keystream = self.PRGA(self.S)
        for c in data:
            output = output + chr(ord(c) ^ self.keystream.next())
        return output

    @staticmethod
    def gen_rc4_key(size):
        return os.urandom(size)
        
    @staticmethod
    def format_rc4_key(key):
        return "0x" + ", 0x".join(re.findall("..", key.encode("hex")))