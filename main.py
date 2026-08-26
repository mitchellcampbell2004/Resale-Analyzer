#main.py
#Mitchell Campbell
'''This file talks to the user'''

#What I've learned:
#-how to import variables/functions from other files
#-how to create separate python files for separate coding purposes

#import sales tax dictionary from calculations.py (need to remove .py)
from calculations import sales_tax_dict

#trying to make func to confirm item category so don't have to repeat 13 times
def item_category_confirmation(item_category_choice, item_category_title):
    while True: 
        electronic_confirmation = input('You have chosen "electronics", is this correct? ').strip().lower()
        if electronic_confirmation in ("yes", "y"):
            print("Great!")
            break
        elif electronic_confirmation in ("no", "n"):
            print("Ok. Please choose the correct category for the item.")
            break
        else:
            print("Sorry, that is not a valid input.")
            print('Please enter either "yes" or "no".')



#######Main Code

#Introduction
print('''
Hello!
Welcome to the Resale Analyzer!
This application is meant to allow you to input and calculate cost of potential items, then calculate what you could potentially resell them for.
This application will also keep track of purchases you have made in the past, their profitability, and many other things.''')

print("Home Page: ")
print("This is your home page.")
print("Here, you can calculate the costs of potential purchases, view your past purchases, and ...")

#home_page_choice
while True:
    home_page_choice = input('''What would you like to do? 
    -Make a new "potential" calculation (type "new", "potential")
    -View past purchases/results? (type "past", "results") ''').lower().strip()

    if home_page_choice in ("new", "potential"):
        menu_choice = "calculations"
        print("Great! You will be redirected to the calculations menu.")
        break
    elif home_page_choice in ("past", "results"):
        menu_choice = "past"
        print("Great! You will be redirected to the past results menu.")
        break
    else:
        print("Sorry, that is not a valid option.")
        print("Please select an option from the menu. Make sure to check your spelling.")

#calculations menu
if menu_choice == "calculations":
    print("Welcome to the calculations menu!")
    print('''Here, you will have the chance to input information, including your budget, the item(s) you are wishing to purchase, and what amount of money you could potentially sell these items for.
    The program will then do some calculations and spit information back out to you, including how much of your buddget would be used, your ROI, and other pertinent info.''')

    #have user input current budget for purchases
    print("So, to start...")
    while True:
        try:
            budget_amount_input = input("What is your current budget to purchase items, storage space, etc.? ")
            budget_amount = round(float(budget_amount_input), 2)
            if budget_amount <= 0:
                print("Please enter a positive number that is greater than 0.")
            else:
                print(f'Great! You currently have ${budget_amount:.2f} to work with.')
                break
        except ValueError:
            print("Sorry, that is not a valid number. Please enter any positive number to two deciminal places.")

    #have user input whether or not they are looking to buy multiple types of items
    print('Now, are you looking to purchase one type of item or multiple types of items?' )
    while True:
        multiple_types_of_items_choice = input('For one type, enter "one", "1", or "single". For multiple types, enter "multiple".' ).strip().lower()
        if multiple_types_of_items_choice in ("1", "one", "single"):
            print("Great! That's much easier than multiple.")
            item_type_choice = "1"
            break
        elif multiple_types_of_items_choice in ("multiple"):
            print("No worries, we'll make sure to figure out all the calculations for each type of item!")
            item_type_choice = "multiple"
            break
        else:
            print("Sorry, that's not a valid option.")
            print("Please choose either one or multiple.")

    #single item type calculation
    if item_type_choice == "1":
        print("So, what kind of item is this? Which category does it best-fit below?")
        #choose item_category
        while True:
            item_category = input("-Electronics(1) -Automotive(2) -Clothing/Apparel(3) -Home/Furniture(4) -Collectibles(5) -Toys/Games(6) -Books/Media(7) -Sports/Outdoors(8) -Jewelry/Accessories(9) -Beauty/Personal Care(10) -Hobbies/Crafts(11) -Industrial/Business Equipment(12) -Miscellaneous(13) ").strip().lower()
            if item_category in ("electronics", "electronic", "1"):
                item_category_name = "electronics"
                while True: 
                    electronic_confirmation = input('You have chosen "electronics", is this correct? ').strip().lower()
                    if electronic_confirmation in ("yes", "y"):
                        print("Great!")
                        break
                    elif electronic_confirmation in ("no", "n"):
                        print("Ok. Please choose the correct category for the item.")
                        break
                    else:
                        print("Sorry, that is not a valid input.")
                        print('Please enter either "yes" or "no".')
            if electronic_confirmation in no:
                continue
            elif electronic_confirmation in yes:
                break       





    #multiple items choice loop
    elif item_type_choice == "multiple":
        while True:
            multiple_items_number = input("How many different items are you looking to buy? ").strip().lower()
            try:
                multiple_items_number = int(multiple_items_number)
                if multiple_items_number <= 0:
                    print("sorry, ")




    




#print(sales_tax_dict)