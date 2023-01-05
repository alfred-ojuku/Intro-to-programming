# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 19:23:38 2022

@author: LENOVO
"""

prompt = "If you tell us who you are, we can personalize the message you see."
prompt +="\nWhat is your first name?\n"

name = input(prompt)

print(f"Hello {name.title()}!")