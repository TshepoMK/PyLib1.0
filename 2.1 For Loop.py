#This Python scrip will loop 20 times calculating the final velocity and
#displacemet for each i value

#Example 1

X_i = 829.8
V_i = 0
g = -9.81
times = range(0, 20, 1)
                    
for i in times:   #i = 20 numbers ranging from 0 to 19
    V_f = V_i + g * t
    X_f = X_i   + V_i * t + 0.5 * g * t**2
                    
    Result_1 = ("After " + str(i) + " seconds, the object's position "
            + "is " + str(X_f) + "m above the ground with a velocity "
            + "of " + str(V_f) + "m/s")
                    
    print Result_1
                            
#==============================================================================#
#This scrip will loop in the numbers ranging from 2 to 99 adding them up to 0
    
#Example 2
                        
Sum = 0
numbers = range(2, 101, 2)
for j in numbers:
    Sum = Sum + j

print Sum

#==============================================================================#
#This scrip operates in a similar manner as Example 2

#Example 3

Product = 1
numbers = range(1, 11, 1)
for k in numbers:
    Product = Product * k

print Product

#==============================================================================#
#This is an example of a script that estimates a term of all odd numbers
#Between 1 and Term value

#Example 4

import math

Terms = 19
Sum = 0

for l in range(1, Terms + 1, 1):
    sign = (-1) ** (l - 1)
    Term = 1.0 / l
    Sum  = Sum  + sign * term

error = abs(math.log(2) - Sum )
print Sum 
print math.log(2)
print error
