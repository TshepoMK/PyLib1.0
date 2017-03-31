# -*- coding: utf-8 -*-
"""
Created on Sun Jun 01 04:12:35 2015

@author: TshepoMK
If you dont wanna loose your dice or you just love programming
Here are you digital dice
"""

import random as rand
min = 1
max = 6
print "Type 'yes' or 'y' to roll again"
roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print "Rolling the dice.."
    print "The results are.."
    
    print rand.randint(min, max)
    print rand.randint(min, max)

    roll_again = raw_input("Roll the dice again? ")