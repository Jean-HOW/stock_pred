# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 16:22:43 2021

@author: jean1
"""


# SIMPLE ----------------------------------------------------------------------------
import random

char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$^&*(')"

while True:
    password_len = int(input("What length would you like your password to be: "))
    password_count = int(input("How many password would you like: "))
    for x in range(0, password_count):
        password = ""
        for x in range(0, password_len):
            password_char = random.choice(char)
            password = password + password_char
        print("Here is your password: ", password)