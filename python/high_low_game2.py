#!/usr/bin/env python3
#creating a high and low numbers game
import random

#generate a random number between 1 and 10
number = random.randint(1, 10)
print(number) #this is used for debugging

#user guesses a number between 1 and 10
guess = int(input("You have 3 chances to guess a number between 1 and 10: "))

#the player gets 3 attempts
chance = 3

#as long as the player has chances they can play
while (chance > 1):
#if the number is too high we tell them and ask to guess again
    if guess > number:
        chance -= 1
        guess = int(input("Too high! You have {0} chance(s) left. Try again: ".format(chance)))
#if the number is too low we tell them and ask to guess again
    elif guess < number:
        chance -= 1
        guess = int(input("Too low! You have {0} chance(s) left. Try again: ".format(chance)))
#if the player guesses the number we congratulate them
    else:
        print("Well done! You got it!")
        exit()

#if the player runs out of chances but also need to consider if the answer is correct.
if guess != number:
    print("Sorry, no more chances. The numer was {0}.".format(number))
else:
    print("Well done! You got it!")

    





