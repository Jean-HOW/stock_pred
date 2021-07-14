# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 15:34:35 2021

@author: jean1
"""

# WITH RULES---------------------------------------------------------------------------

import random 
import array 
  
# maximum length of password needed 
# this can be changed to suit your password length 

def generate_pw(pw_len):
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']   
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',  
                 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 
                 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 
                 'z'] 
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',  
                 'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 
                 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 
                 'Z'] 
    symbol = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',  
              '*', '(', ')', 'u']
    # combines all the character arrays above to form one array 
    combine_list = digits + lowercase + uppercase + symbol
    random_digit = random.choice(digits) 
    random_upper = random.choice(uppercase) 
    random_lower = random.choice(lowercase) 
    random_symbol = random.choice(symbol) 
    temp_pass = random_digit + random_upper + random_lower + random_symbol 
    
    for x in range(pw_len - 4):  
        temp_pass = temp_pass + random.choice(combine_list) 
        temp_pass_list = array.array('u', temp_pass)  
        random.shuffle(temp_pass_list) # traverse the temporary password array and append the chars to form the password  
        password = ""
        for x in temp_pass_list: 
            password = password + x 
    return password

# Simple password version
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
