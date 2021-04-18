#!/usr/bin/env python3
# Another comment!
# This script will gather name and age data

name = input("What is your name: ")
now = input("What year is it: ")
born = input("What year were you born: ")
age = (int(now) - int(born))
print ("Hello {0}, you are {1} years old".format(name, age))


