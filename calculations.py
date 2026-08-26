#resale.py
#Mitchell Campbell
'''Purpose: to create the calculations for the resale analyzer application'''

#What I've learned:
#-how to import CSV
#-how to use Rainbow CSV to make better use of csv data
#-how to open and parse csv files and make dictionaries with that data using "with open" and "as file"
#-how to create dictionaries within dictionaries


def total_cost(price_per_unit, total_units, tax, shipping):
    '''Calculate total cost of a potential purchase'''
    product_cost = price_per_unit * total_units
    return product_cost + shipping + tax

#print(f"Total_cost: ${total_cost(12.00, 30.00, 125.00)}")

#dictionaries containing things like sales tax by state
import csv


#sales tax dict; info. via https://taxfoundation.org/data/all/state/sales-tax-rates/
sales_tax_dict = {}

#open sales tax file and build dictionary with state dictionaries inside it
with open("2026_sales_tax_by_state.csv", "r") as file: #means to open and read ("r") csv file, work "with" it and then close when done
    sales_tax_reader = csv.DictReader(file)

    for row in sales_tax_reader:
        sales_tax_state = row["State"].lower()
        statewide_sales_tax = (float(row["State Sales Tax Rate"].replace("%", "")) / 100)
        avg_local_sales_tax = (float(row["Avg. Local Sales Tax Rate"].replace("%", "")) / 100)
        total_sales_tax = statewide_sales_tax + avg_local_sales_tax

        sales_tax_dict[sales_tax_state] = {
            "statewide": statewide_sales_tax,
            "local": avg_local_sales_tax,
            "total": total_sales_tax
        }

        #print(sales_tax_dict)

#select state + calculate sales tax
#while True:
    #sales_tax_state_selection = input("What state would you be making this purchase in? ").strip().lower()

def calculate_sales_tax(item_cost, sales_tax_state, sales_tax_dict): #call the item cost, the user-inputted state, and grab the dictionary
    sales_tax_rate = sales_tax_dict[sales_tax_state]["total"] #need to call it in this order so that pyth doesn't get confused and think you're trying to index a str
    return item_cost * sales_tax_rate

def calculate_base_cost(cost_of_item, number_of_items):
    return cost_of_item * number_of_items

def calculate_additional_fees():
    while True:
        additional_fees_answer = input("Are there any additional fees besides tax that you had to pay/could foresee being associated with this investment? ").strip().lower()
        if additional_fees_answer in ("yes", "y"):
            number_list=[]
            print("Ok. You will now be prompted to enter any additional costs, including shipping, rent for a storage space, etc.")
            print("Enter each fee one at a time.")
            print("If a fee is more abstract, such as renting a storage space, enter your best guess at how much it will cost you for this purchase specifically.")
            while True:
                try:
                    list_number = input('Type each number individually and press enter. Type "done" when you are done. ').strip().lower()
                    if list_number in ('d', 'done'):
                        break
                    else:
                        list_number = float(list_number)
                        if list_number <= 0:
                            print("Sorry, that is not a valid input.")
                            print("Please enter a number greater than 0.")
                        else:
                            number_list.append(list_number)
                except ValueError:
                    print("Sorry, that is not a valid number.")
                    print('Please try again.')
            total = sum(number_list)
            print(f"Your additional fee total is ${total:.2f}.")
            return total
        elif additional_fees_answer in ("no", "n"):
            print('Great, your additonal fees total is $0.')
            total = 0
            return total
        else:
            print("Sorry, that is not a valid input.")
            print('Please enter either "yes" or "no".')

def calculate_total_cost(base_cost, tax, additional_fees):
    return (base_cost + tax + additional_fees)

def calculate_roi(total_cost, returns):
    net_profit = returns - total_cost

    
   
