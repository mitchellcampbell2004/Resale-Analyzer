#main.py
#Mitchell Campbell
'''This file talks to the user'''

#What I've learned:
#-how to import variables/functions from other files
#-how to create separate python files for separate coding purposes

#import sales tax dictionary from calculations.py (need to remove .py)
from calculations import sales_tax_dict

#######Main Code

#Introduction
print('''
Hello!
Welcome to the Resale Analyzer!
This application is meant to allow you to input and calculate cost of potential items, then calculate what you could potentially resell them for.
This application will also keep track of purchases you have made in the past, their profitability, and many other things.''')

#print(sales_tax_dict)