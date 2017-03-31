#An exmaple of usage of "if statements", basically you give a script
#conditions to run until they are met.This is a simple code, for a more
#Accurate directive code look at example 2

# Example 1

Grade = 71

if grade < 50:
    print "Fail"
    
elif grade < 75:
    print "Pass"
    
else:
    print "Distinction"
#==============================================================================#
    
#Example 2
    
Grade = 71

if Grade > 1 and Grade < 50:
    print "Fail"
    
if Grade >= 50 and Grade < 75:
    print "Pass"
    
if Grade >= 75 and Grade <= 100:
    print "Distinction" 
    
if Grade < 1 and Grade > 100:
    print "Grade not availabe"
    
    
#==============================================================================#
#This script calculates how many times a dice landed on 1 and 2 and add up the
#total
    
#Example 3
    
import random


count_1 = 0
count_2 = 0
sum_of_dice = 0
while sum_of_dice < 50:
    dice = random.randint(1, 6)
    sum_of_dice = sum_dice + dice

    if dice == 2:
        count_1 = count_1 + 1

    if dice == 2:
        count_2 = count_2 + 1

print "Landed on 1 " + str(count_1) + " times."
print "Landed on 2 " + str(count_2) + " times."


#==============================================================================#
#This script checks for odd and even numbers and positive and negative numbers
#Example 4

int_val = -21

if (int_val % 2) == 1 and (int_val > 0):
    print "Odd Number"
    print "Greater than 0"

if (int_val % 2) == 1 and (int_val < 0):
    print "Odd Number"
    print "Greater than 0"

if (int_val % 2) != 1 and (int_val > 0):
    print "Even Number"
    print "Greater than 0"

if (int_val % 2) != 1 and (int_val < 0):
    print "Even Number"
    print "Less than 0"




