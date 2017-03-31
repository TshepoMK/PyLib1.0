# -*- coding: utf-8 -*-
"""
Created on Sun Jun 06 04:20:57 2015

@author: TshepoMK
Topic - Semester Mark Calculator

This program I wrote it to calculate semester based on two semester tests
weighing 35 % each, tutorials weighing 10% and practicals wieghing 20 % you can
tweek it to suite your module requirements
"""

Semester_Test1 = int(raw_input("Enter Mark for Semester Test 1: "))
T1_Total = int(raw_input("Enter Maximum Mark Possible for Semester Test 1 : "))

Semester_Test2 = int(raw_input("Enter Mark for Semester Test 2: "))
T2_Total = int(raw_input("Enter Maximum Mark Possible for Semester Test 2 : "))


Tutorial_Tests = int(raw_input("Enter Mark for Tutorial Test 2: "))
Tut_Total = int(raw_input("Enter Maximum Mark Possible for Tutorials: "))

Practical_Mark = int(raw_input("Enter Mark for Practicals: "))
Prac_Total = int(raw_input("Enter Maximum Mark Possible for Practicals: "))

Semester_Test1_Average = (Semester_Test1 / T1_Total) * 0.35
Semester_Test2_Average = (Semester_Test2 / T2_Total) * 0.35
Tutorial_Tests_Average = (Tutorial_Tests / Tut_Total)  * 0.1
Practical_Mark_Average = (Practical_Mark / Prac_Total) * 0.2
   
Semester_mark = (Semester_Test1_Average + Semester_Test2_Average 
                + Tutorial_Tests_Average + Practical_Mark_Average) / 2

if Semester_mark < 40:
	print "Sorry, you did not make the exam entrance " 
if Semester_mark >= 40 and Semester_mark < 55:
	print "You qualified for Exam, you have to work extra hard though."
if Semester_mark >= 55:
		print "Congratulations, you did well and qualified for Exam."

print "Your Semester mark is: ", Semester_mark