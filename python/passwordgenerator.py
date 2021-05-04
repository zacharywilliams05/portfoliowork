#!/usr/bin/env python3
# By Zachary Williams
# Finally adding a description
# 5/3/2021
import random
import string

lower_char = string.ascii_lowercase 
upper_char = string.ascii_uppercase
digits = string.digits

#ask user for the desired password length, number of passwords, and which characters they want:
password_lenth = int(input("Hello! How many characters would you like: "))
password_amount = int(input("Hello! How many password do you want: "))
lower_tf = input("Would you like lowercase characteres: ")
upper_tf = input("Would you like uppercase characters: ")
dig_tf = input("Wouldy ou like digits: ")

combined_characters = ""

if lower_tf == "Yes" or lower_tf == "yes" or lower_tf == "Y" or lower_tf == "y":
    combined_characters += lower_char
if upper_tf == "Yes" or upper_tf == "yes" or upper_tf == "Y" or upper_tf == "y":
    combined_characters += upper_char
if dig_tf == "Yes" or dig_tf == "yes" or dig_tf == "Y" or dig_tf == "y":
    combined_characters += digits

for i in range (password_amount):
    my_password = "".join(random.sample(combined_characters, password_lenth))
    print(my_password)
