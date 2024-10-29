#importing module from another file 

import mymodule
print(mymodule.generate_name('Ridam','Jain'))


#During import we can rename the modules also 
'''
from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g

'''

#we can have many functions imported 
'''
from mymodule import generate_full_name, sum_two_nums, person, gravity

'''


'''
Import Built-in Modules
Some of the common built-in modules: math, datetime, os,sys, random, statistics, collections, json,re

'''

'''
OS Module

Using python os module it is possible to automatically perform many operating system tasks. 
The OS module in Python provides functions for creating, changing current working directory,
and removing a directory (folder), fetching its contents, changing and identifying the current directory.

'''

'''
import os

#Creating a directory 
os.mkdir('practice')
#Changing the current path 
os.chdir('path')
#getting current working directory 
os.getcwd()
#Removing directory 
os.rmdir()

'''


'''

Sys Module

The sys module provides functions and variables used to manipulate different parts of the Python runtime environment. 
Function sys.argv returns a list of command line arguments passed to a Python script.
The item at index 0 in this list is always the name of the script, at index 1 is the argument passed from the command line.

import sys
#print(sys.argv[0], argv[1],sys.argv[2])  # this line would print out: filename argument1 argument2
print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))


python script.py Asabeneh 30DaysOfPython
'''



'''
Statistics Module
    The statistics module provides functions for mathematical statistics of numeric data.
    The popular statistical functions which are defined in this module: mean, median, mode, stdev etc.



'''

from statistics import * #importing all the modules 
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(median(ages))
print(mean(ages))
print(mode(ages))
print(variance(ages))
print(stdev(ages))
    


'''
Math Module
    Module containing many mathematical operations and constants.


'''

from math import sqrt,pi,pow,floor,ceil,log10

print(pi)
print(sqrt(10))
print(pow(2,3))
print(floor(9.81))
print(ceil(5.6))
print(log10(100))


'''

String Module
     string module is a useful module for many purposes. The example below shows some use of the string module


'''

import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~


'''
Random Module
    Random module which gives us a random number between 0 and 0.9999....

'''

from random import random ,randint

from random import random, randint
print(random())   # it doesn't take any arguments; it returns a value between 0 and 0.9999
print(randint(5, 20)) # it returns a random integer number between [5, 20] inclusive