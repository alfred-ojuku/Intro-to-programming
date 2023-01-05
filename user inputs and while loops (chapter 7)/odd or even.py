# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 15:28:16 2022

@author: LENOVO
"""
message = "Enter a number and I'll tell you if" 
message += "the number is even or odd:"

number = input(message)

number = int(number)

if number % 2 == 0:
     print(f"\n{number} is even")
else:
     print(f"\n{number} is odd")