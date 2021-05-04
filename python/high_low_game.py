#!/usr/bin/env python3
#creating a high and low numbers game
import random


#generate a random number between 1 and 10
number = random.randint(1, 10)
print(number)

#user guesses a number between 1 and 10
guess = int(input("Guess a number between 1 and 10: "))

while guess != number:
#if the number is too high we tell them and ask to guess again
    if guess > number:
        guess = int(input("Too high! Try again: "))
#if the number is too low we tell them and ask to guess again
    elif guess < number:
        guess = int(input("Too low Try again: "))
#if the user guesses the number we congratulate them
print("Well done! You got it!")
