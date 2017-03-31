# -*- coding: utf-8 -*-
"""
Created on Sun Jun 07 04:05:44 2015

@author: TshepoMK
Topic - Guess the number
Again I challenge you to make this script more interesting by throwing in words
"""

import random
number = random.randint(1, 99)
guesses = 0

while guesses < 5:
    guess = int(raw_input("Enter an integer from 1 to 99: "))
    guesses +=1
    print "this is your %d guess" %guesses
	
    if guess < number:
        print "guess is low"
    elif guess > number:
        print "guess is high"
    elif guess == number:
        break
		
if guess == number:
    guesses = str(guesses)
    print "You guess it in : ", guesses + " guesses"

if guess != number:
    number = str(number)
    print "The secret number was",  number
