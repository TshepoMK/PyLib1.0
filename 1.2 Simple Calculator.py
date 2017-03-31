# -*- coding: utf-8 -*-
"""
Created on Sun Jun 03 06:41:12 2015

@author: TshepoMK
Topic - Simple calculations

Note that I str() in print look at the print out and pick out how it works
and try to play around with it once you figure it out it will be useful 
"""
#=============================================================================#
#This is an example for calculating the final velocity and distance using Python
#Example 1

V_i = 0
g = -9.81
t = 3.5
X_i = 5.6

V_f = V_i + g * t
X_f = X_i + V_i * t + 0.5 * g * t ** 2

print "V_f: ", V_f
print "X_f: ", X_f
#=============================================================================#
#Example of scrip including strings in the printed result
#Example 2

X_i = 17
V_i = 0
g = -9.81

t_1 = 0.5
t_2 = 1.5
t_3 = 2.5

V_1 = V_i + g * t_1
X_1 = X_i+ V_i * t_1 + 0.5 * g * t_1 ** 2

V_2 = V_i + g * t_2
X_2 = X_i+ V_i * t_2 + 0.5 * g * t_2 ** 2

V_3 = V_i + g * t_3
X_3 = X_i + V_i * t_3 + 0.5 * g * t_3 ** 2

Result_1 = ("After " + str(t_1) + " seconds, the object's position "
        + "is " + str(X_1) + "m above the ground with a velocity "
        + "of " + str(V_1) + "m/s")

Result_2 = ("After " + str(t_2 ) + " seconds, the object's position "
        + "is " + str(X_2) + "m above the ground with a velocity "
        + "of " + str(V_2) + "m/s")

Result_3 = ("After " + str(t_3) + " seconds, the object's position "
        + "is " + str(X_3) + "m above the ground with a velocity "
        + "of " + str(V_3) + "m/s")

print "Result_1: " ,Result_1
print "Result_2: " ,Result_2
print "Result_3: " ,Result_3