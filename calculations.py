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
        sales_tax_state = row["State"]
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
while True:
    sales_tax_state_selection = input("What state would you be making this purchase in? ").strip().lower()
    
