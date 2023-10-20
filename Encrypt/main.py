import random
import string

all_chars = string.ascii_letters + string.digits + string.punctuation + " "
all_chars = list(all_chars)

# print(all_chars)
key = all_chars.copy()

# Ramdom chars
random.shuffle(key)
# print(kay)
"""Encrypy prosses"""
print("----------------Encrypt-------------")
massge = input("Enter Your Massge to encypt: ")
enc_massge = ""

for letter in massge:
    """loop all letter in all_charts and 
        match to ramdom leaters in vurable key """
    index =all_chars.index(letter)
    enc_massge += key[index]
print(f"Encrytp massge is {enc_massge}")

"""Dencrypy prosses"""
print("----------------Encrypt-------------")

enc_massge = input("Enter Your Encrypt Massge: ")
massge = ""

for letter in enc_massge:
    """loop all letter in key and 
        match to ramdom leaters in vurable all_charts """
    index =key.index(letter)
    massge += all_chars[index]
print(f"Encrytp massge is {massge}")
