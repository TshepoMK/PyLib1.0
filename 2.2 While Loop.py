#This script estimates a value of ln using an error of 1E-5

#Example 1

import math


ln_approx = 0
error = 1
ind = 1
max_terms = 25

while (error > 1E-6) and (ind <= max_terms):
    sign = (-1) ** (ind-1)
    term = 1.0 / ind
    ln_approx = ln_approx + (sign * term)

    ind = ind + 1
    error = abs(ln_approx - math.log(2))

print "Num Terms: " + str(ind)
print "Error: " + str(error)
print "ln(2) Approx: " + str(ln_approx)

#==============================================================================#
#This scrip loops through number of dice throws adding them up as long as the
#sum is less than or equal to 50

#Example 2

import random


ind = 1
stats = [0]*6
my_sum = 0
while my_sum <= 50:
    dice = random.randint(1, 6)
    stats[dice-1] = stats[dice-1] + 1
    my_sum = my_sum + dice
    ind = ind + 1

print "Num Terms: " + str(ind)
print "Sum: " + str(my_sum)
print "Stats:"
print "   Dice: " + str(range(1, 7, 1))
print "  Count: " + str(stats)
