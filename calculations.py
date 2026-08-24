#resale.py
#Mitchell Campbell
'''Purpose: to create an application utilizing Python and R in which one can enter information, calculate results, and display information related to reselling.'''

#Home Screen; possible user/pw entering
print("Welcome!")

#explain the purpose
print("The purpose of this program is to aid resellers with finding (potential) goods, calculating profitability, and to display the calculated information in an easily-digestible format.")

#Home menu

print("What would you like to do?")

while True:
    home_menu_choice = input('-See prior purchases/profits (enter "prior" or "history") \n-Calculate potential/new profits (enter "potential" or "new") \n-Other (enter "other") ').lower().strip()
    if home_menu_choice in ('prior', 'history'):
        print("Routing to history...")
    elif home_menu_choice in ('potential', 'new'):
        print("Routing to new order...")
    elif home_menu_choice in ('other'):
        print('Routing to "Other" menu...')
    else:
        print("Sorry, that is not a valid option.")
        print("Please select one of the options listed on the menu.")

if home_menu_choice in ('prior', 'history'):
    print("Welcome to the potential/current ")
#Enter information related to potential purchase
