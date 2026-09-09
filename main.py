#main.py
#Mitchell Campbell
'''This file talks to the user'''

#What I've learned:
#-how to import variables/functions from other files
#-how to create separate python files for separate coding purposes

#import sales tax dictionary from calculations.py (need to remove .py)
from calculations import sales_tax_dict
#import categories.py functions
import categories 

#trying to make func to confirm item category so don't have to repeat 13 times -- success!

item_sub_cat = str()
item_dictionary = {}
item_count = 0
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
    print('''Here, you will have the chance to input information, including your budget, the item(s) you are wishing to purchase, and what amount of money you could potentially sell these items for. The program will then do some calculations and spit information back out to you, including how much of your buddget would be used, your ROI, and other pertinent info.''')

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
        multiple_types_of_items_choice = input('For one type, enter "one", "1", or "single". For multiple types, enter "multiple". ').strip().lower()
        if multiple_types_of_items_choice in ("1", "one", "single"):
            print("Great!")
            numb_diff_items = "1"
            break
        elif multiple_types_of_items_choice in ("multiple"):
            print("Great")
            numb_diff_items = "multiple"
            break
        else:
            print("Sorry, that's not a valid option.")
            print("Please choose either one or multiple.")

    #ask 
    if numb_diff_items == "1":
        print("So, what kind of item is this?")
    elif numb_diff_items == "multiple":
        print("So, what kind of item is this?")
        if item_count >= 1:
            print('If you are done adding items, enter "quit" or "exit."')

    #choose item category
    item_category = categories.category_choice()

    #select item subcategory
    if item_category == "Electronics":
        item_subcat = categories.elect_subcat()
    elif item_category == "Automotive":
        item_subcat = categories.auto_subcat()
    elif item_category == "Clothing/Apparel":
        item_subcat = categories.clothing_subcat()
    elif item_category == "Home/Furniture":
        item_subcat = categories.home_subcat()
    elif item_category == "Collectibles":
        item_subcat = categories.collect_subcat()
    elif item_category == "Toys/Games":
        item_subcat = categories.toy_subcat()
    elif item_category == "Books/Media":
        item_subcat = categories.books_subcat
    elif item_category == "Sports/Outdoors":
        item_subcat = categories.sports_subcat()
    elif item_category == "Jewelry/Accessories":
        item_subcat = categories.jewelry_subcat()
    elif item_category == "Beauty/Personal Care":
        item_subcat = categories.beauty_subcat()
    elif item_category == "Hobbies/Crafts":
        item_subcat = categories.hobb_subcat()
    elif item_category == "Industrial/Business Equipment":
        item_subcat = categories.ind_subcat()
    elif item_category == "Miscellaneous":
        item_subcat = categories.misc_subcat()


    #move on to the item specifics

    #ask for the name of the item and confirm
    print(f"Alright, this item is in the {item_category} category, specifically under {item_subcat}.")
    while True:
        item_name = input("What is the name of this item? Be relatively detailed and check your spelling! ")
        item_name = str(item_name)
        while True:
            print(f"Are you sure you want to name this item {item_name}?")
            item_name_confirmation = input("You will not be able to change this in the future... ")
            if item_name_confirmation in ("yes", "y"):
                print(f'Ok, your item is officially named: "{item_name}".')
                break
            elif item_name_confirmation in ("no", "n"):
                print("Ok, please enter the correct name for this item.")
                break
        if item_name_confirmation in ("yes", "y"):
            break
        elif item_name_confirmation in ("no", "n"):
            continue


    #move on to price and quantity; ask one or multiple of the same item
    print("Ok, moving on to price and quantity.")
    item_quantity_loop = True
    while item_quantity_loop == True:
        while True:
            one_or_more = input(f"Are you looking to buy one {item_name} or multiple? ")
            if one_or_more in ("1", "one", "single", "individual"):
                break
            elif one_or_more in ("multiple", "mult", "more", "more than one"):
                break
            else:
                print("Sorry, that is not a valid option.")
                print('Please enter either "one" or "multiple".')

        if one_or_more in ("1", "one", "single", "individual"):
            while True:
                item_quantity_confirmation = input(f"You are looking to purchase 1 {item_name}, correct? ")
                if item_quantity_confirmation in ("yes", "y"):
                    item_quantity = 1
                    item_quantity_loop = False
                    break
                elif item_quantity_confirmation in ("no", "n"):
                    break
        elif one_or_more in ("multiple", "mult", "more", "more than one"):
            while True:
                while True:
                    try:
                        item_quantity = int(input("Enter how many of these items you are looking to purchase. "))
                        if item_quantity >= 1:
                            break
                    except ValueError:
                        print("Sorry, that is not a valid quantity.")
                        print("Please enter a whole number that is greater than or equal to 1.")
                while True:
                    item_quantity_confirmation = input(f"You are looking to purchase {item_quantity} of the item {item_name}, correct? ")
                    if item_quantity_confirmation in ("yes", "y"):
                        print(f"Great! The quantity of {item_name} is now {item_quantity}!")
                        item_quantity_loop = False
                        break
                    elif item_quantity_confirmation in ("no", "n"):
                        print("Ok, please enter the correct quantity.")
                        break
                    else:
                        print("That is not a valid input.")
                        print('Please enter either "yes" or "no".')

                if item_quantity_confirmation in ("yes", "y"):
                    break
                elif item_quantity_confirmation in ("no", "n"):
                    continue


    #multiple items choice loop
    '''elif item_type_choice == "multiple":
        while True:
            multiple_items_number = input("How many different items are you looking to buy? ").strip().lower()
            try:
                multiple_items_number = int(multiple_items_number)
                if multiple_items_number <= 0:
                    print("sorry, ")'''




    




#print(sales_tax_dict)