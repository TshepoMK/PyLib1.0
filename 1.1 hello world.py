# -*- coding: utf-8 -*-
"""
Created on Sun Jun 03 06:41:12 2015

@author: TshepoMK
Topic - Hello world, Name assignments, Punctuation and math symbols, modules

"""

#1- Python hello world script is more very compared to other languages

print("Hello World!") #And just like that you are done
#=============================================================================#
#2 - Breakdown of the above code

print - the interpreter will display whatever comes after print
        And you will notice that the print out doesnt have "", its because in
        python 
        and most languages whatever is in the quotattion marks is called a 
        string.
        And unlike most languages python does not require ; at the end of a 
        code
#=============================================================================#        
#3- Name assingments
#3.1
        
a = "Hello World!"

print = a #This will print Hello world too
#3.2 Math Symbols and Punctuation

If you want to add comments on your like markers and you dont want errors, in 
python we use a hash symbol "#" like I did above.
#=============================================================================#
#mathematical functions are pretty much standard
a = 2
b = 5

c = a + b 
print c #will give me 7
d = a * b
print d #will give me 10
e = b / a 
print e #will give me 2.5
f = b - a
print f  # will give me 3
g = a * a = a ** 2
print g # it will the value of a to the power 2, 4
#=============================================================================#
#4 - Modules
#Modules are python scripts that have been prewritten to do a specific task
#that will reqire you to write an extra script before starting with what you 
#want to write, so in a nutshell they make progarmming easier and less tediuos
#To use them you have to tell python to draw them from achives if you will
#You can read up online on these modules because they are very important

#Example, say I want to compute the following.
x = 0
fx = x ** 2 + e ** x
print fx    #will give me an error that e is not defined because it is just a 
            #letter but in math it has a value
import math
from math import e
#then
print fx # will give me 1
#=============================================================================#
#You can import a lot of functions from math module

import math
from math import e, factorial, cos, sin, tan, pi, radian
#Examples
x = 30
gx = cosx ** 2 + sinx * e ** x  #tell python you uisng import from math and 
                                #convert x to radians if reqiured to

gx_new = math.cos(radian(30)) ** 2 + math.sin(radian(30)) * math.e ** radian(30)
print gx_new

#=============================================================================#








        