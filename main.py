#main.py
#Mitchell Campbell
'''This file talks to the user'''

#What I've learned:
#-how to import variables/functions from other files
#-how to create separate python files for separate coding purposes

#import sales tax dictionary from calculations.py (need to remove .py)
from calculations import sales_tax_dict

#trying to make func to confirm item category so don't have to repeat 13 times
def item_category_confirmation(item_category_title):
    while True: 
        confirmation_answer = input(f'You have chosen "{item_category_title}", is this correct? ').strip().lower()
        if confirmation_answer in ("yes", "y"):
            print("Great!")
            return "y"
        elif confirmation_answer in ("no", "n"):
            print("Ok. Please choose the correct category for the item.")
            return "n"
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
        multiple_types_of_items_choice = input('For one type, enter "one", "1", or "single". For multiple types, enter "multiple". ').strip().lower()
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
        print("So, what kind of item is this?")
        #choose item_category
        while True:
            item_category = input("-Electronics(1) -Automotive(2) -Clothing/Apparel(3) -Home/Furniture(4) -Collectibles(5) -Toys/Games(6) -Books/Media(7) -Sports/Outdoors(8) -Jewelry/Accessories(9) -Beauty/Personal Care(10) -Hobbies/Crafts(11) -Industrial/Business Equipment(12) -Miscellaneous(13) ").strip().lower()
            if item_category in ("electronics", "electronic", "1"):
                item_category_name = "Electronics"
            elif item_category in ("auto", "automotive", "car", "2"):
                item_category_name = "Automotive"
            elif item_category in ("clothing", "apparel", "clothes", "shoes", "3"):
                item_category_name = "Clothing/Accessories"
            elif item_category in ("home", "furniture", "house", "home/furniture", "4"):
                item_category_name = "Home/Furniture"
            elif item_category in ("collectibles", "5"):
                item_category_name = "Collectibles"
            elif item_category in ("toys", "games", "toys/games", "6"):
                item_category_name = "Toys/Games"
            elif item_category in ("books", "media", "books/media", "7"):
                item_category_name = "Books/Media"
            elif item_category in ("sports", "outdoors", "sports/outdoors", "8"):
                item_category_name = "Sports/Outdoors"
            elif item_category in ("jewelry", "accessories", "jewelry/accessories", "9"):
                item_category_name = "Jewelry/Accessories"
            elif item_category in ("beauty", "personal", "personal care", "beauty/personal care", "10"):
                item_category_name = "Beauty/Personal Care"
            elif item_category in ("hobbies", "hobby", "crafts", "hobbies/crafts", "11"):
                item_category_name = "Hobbies/Crafts"
            elif item_category in ("industrial", "business", "equipment", "industrial equipment", "business equipment", "industrial/business equipment", "12"):
                item_category_name = "Industrial/Business Equipment"
            elif item_category in ("misc", "misc.", "miscellaneous", "13"):
                item_category_name = "Miscellaneous"
            else:
                print("Sorry, that's not a valid option.")
                print("Please choose an option from the menu below.")
                print("Type either the name of the menu or its corresponding number.")
                continue

            #either move on to next step or restart if user chose wrong category
            item_cat_conf_answer = item_category_confirmation(item_category_name)
            if item_cat_conf_answer == "y":
                item_classification = item_category
                break
            elif item_cat_conf_answer == "n":
                continue
             
        #######for the category of item, create subcategories and have user choose which one to access
        #choose electronics subcategory
        if item_classification == "Electronics":
            while True:
                print("What electronics subcategory does this item fit under?")
                elect_sub_cat = input("-Smartphones(1) -Tablets(2) -Laptops(3) -Desktop Computers(4) -Computer Components(5) -Monitors(6) -TVs(7) -Cameras/Lenses(8) -Audio Equipment(9) -Gaming Consoles(10) -Gaming Accessories(11) -Smart Home Devices(12) -Wearables/Smartwatches(13) -Networking Equipment(14) -Cables/Adaptors(15) -Other(16) ").strip().lower()
                if elect_sub_cat in ("smartphones", "phones", "1"):
                    elect_sub_cat_name = "Smartphones"
                elif elect_sub_cat in ("tablets", "2"):
                    elect_sub_cat_name = "Tablets"
                elif elect_sub_cat in ("laptop", "laptops", "3"):
                    elect_sub_cat_name = "Laptops"
                elif elect_sub_cat in ("desktop", "computers", "desktop computers", "4"):
                    elect_sub_cat_name = "Desktop Computers"
                elif elect_sub_cat in ("computer components", "components", "5"):
                    elect_sub_cat_name = "Computer Components"
                elif elect_sub_cat in ("monitors", "monitor", "6"):
                    elect_sub_cat_name = "Monitors"
                elif elect_sub_cat in ("tv", "tvs", "7"):
                    elect_sub_cat_name = "TVs"
                elif elect_sub_cat in ("cameras", "lenses", "cameras/lenses", "8"):
                    elect_sub_cat_name = "Cameras/Lenses"
                elif elect_sub_cat in ("audio", "audio equipment", "9"):
                    elect_sub_cat_name = "Audio Equipment"
                elif elect_sub_cat in ("consoles", "gaming consoles", "10"):
                    elect_sub_cat_name = "Gaming Consoles"
                elif elect_sub_cat in ("accessories", "gaming accessories", "11"):
                    elect_sub_cat_name = "Gaming Accessories"
                elif elect_sub_cat in ("smart home devices", "smart devices", "home", "home devices", "12"):
                    elect_sub_cat_name = "Smart Home Devices"
                elif elect_sub_cat in ("wearables", "smartwatches", "wearables/smartwatches", "13"):
                    elect_sub_cat_name = "Wearables/Smartwatches"
                elif elect_sub_cat in ("networking", "networking equipment", "14"):
                    elect_sub_cat_name = "Networking Equipment"
                elif elect_sub_cat in ("cables", "adaptors", "cables/adaptors", "15"):
                    elect_sub_cat_name = "Cables/Adaptors"
                elif elect_sub_cat in ("other", "16"):
                    elect_sub_cat_name = "Other"
                else:
                    print("Sorry, that's not a valid option.")
                    print("Please select a valid option or its corresponding number.")
                    continue

                #confirm electronic subcategory selection or restart
                elect_sub_cat_name_answer = item_category_confirmation(elect_sub_cat_name)
                if elect_sub_cat_name_answer == "y":
                    elect_classification = elect_sub_cat_name
                    break
                elif elect_sub_cat_name_answer == "n":
                    continue

        #choose automotive subcategory
        elif item_classification == "Automotive":
            while True:
                print("What automotive subcategory does this item fit under?")
                auto_sub_cat = input("-Vehicles(1) -Car/Truck Parts(2) -Wheels/Tires(3) -Tools/Equipment(4) -Electronics/Audio(5) -Interior Accessories(6) -Exterior Accessories(7) -Performance Parts(8) -Maintenance Parts(9) -Accessories(10) -Other(11) ").strip().lower()
                if auto_sub_cat in ("vehicles", "1"):
                    auto_sub_cat_name = "Vehicles"
                elif auto_sub_cat in ("car parts", "truck parts", "car/truck parts", "2"):
                    auto_sub_cat_name = "Car/Truck Parts"
                elif auto_sub_cat in ("wheels", "tires", "wheels/tires", "3"):
                    auto_sub_cat_name = "Wheels/Tires"
                elif auto_sub_cat in ("tools", "equipment", "tools/equipment", "4"):
                    auto_sub_cat_name = "Tools/Equipment"
                elif auto_sub_cat in ("electronics", "audio", "electronics/audio", "5"):
                    auto_sub_cat_name = "Electronics/Audio"
                elif auto_sub_cat in ("interior", "interior accessories", "6"):
                    auto_sub_cat_name = "Interior Accessories"
                elif auto_sub_cat in ("exterior", "exterior accessories", "7"):
                    auto_sub_cat_name = "Exterior Accessories"
                elif auto_sub_cat in ("performance", "performance parts", "8"):
                    auto_sub_cat_name = "Performance Parts"
                elif auto_sub_cat in ("maintenance", "maintenance parts", "9"):
                    auto_sub_cat_name = "Maintenance Parts"
                elif auto_sub_cat in ("accessories", "10"):
                    auto_sub_cat_name = "Accessories"
                elif auto_sub_cat in ("other", "11"):
                    auto_sub_cat_name = "Other"
                else:
                    print("Sorry, that's not a valid option.")
                    print("Please select a valid option or enter its corresponding number.")
                    continue

                #confirm auto subcategory selection or restart
                auto_sub_cat_name_answer = item_category_confirmation(auto_sub_cat_name)
                if auto_sub_cat_name_answer == "y":
                    auto_classification = auto_sub_cat_name
                    break
                elif auto_sub_cat_name_answer =="n":
                    continue

        #choose clothing subcategory
        elif item_classification == "Clothing/Apparel":
            while True:
                print("What clothing/apparel subcategory does this item best fit?")
                clothing_sub_cat = input("-Men's Clothing(1), -Women's Clothing(2) -Children's clothing(3) -Shoes(4) -Boots(5) -Jackets/Coats(6) -Dresses(7) -Suits/Formalwear(8) -Vintage Clothing(9) -Athletic Wear(10) -Workwear(11) -Accessories(12) -Designer/Luxury(13) -Other(14) ").strip().lower()
                if clothing_sub_cat in ("men", "men's", "men's clothing", "1"):
                    clothing_sub_cat_name = "Men's Clothing"
                elif clothing_sub_cat in ("women", "women's", "women's clothing", "2"):
                    clothing_sub_cat_name = "Women's Clothing"
                elif clothing_sub_cat in ("children's", "children", "children's clothing", "3"):
                    clothing_sub_cat_name = "Children's Clothing"
                elif clothing_sub_cat in ("shoes", "shoe", "4"):
                    clothing_sub_cat_name = "Shoes"
                elif clothing_sub_cat in ("boots", "boot", "5"):
                    clothing_sub_cat_name = "Boots"
                elif clothing_sub_cat in ("jackets", "coats", "jackets/coats", "6"):
                    clothing_sub_cat_name = "Jackets/Coats"
                elif clothing_sub_cat in ("dresses", "dress", "7"):
                    clothing_sub_cat_name = "Dresses"
                elif clothing_sub_cat in ("suits", "formal", "formalwear", "suits/formalwear", "8"):
                    clothing_sub_cat_name = "Suits/Formalwear"
                elif clothing_sub_cat in ("vintage", "vintage clothing", "9"):
                    clothing_sub_cat_name = "Vintage Clothing"
                elif clothing_sub_cat in ("athletic", "athletic wear", "10"):
                    clothing_sub_cat_name = "Athletic Wear"
                elif clothing_sub_cat in ("work", "workwear", "11"):
                    clothing_sub_cat_name = "Workwear"
                elif clothing_sub_cat in ("accessories", "12"):
                    clothing_sub_cat_name = "Accessories"
                elif clothing_sub_cat in ("designer", "luxury", "designer/luxury", "13"):
                    clothing_sub_cat_name = "Designer/Luxury"
                elif clothing_sub_cat in ("other", "14"):
                    clothing_sub_cat_name = "Other"
                else:
                    print("Sorry, that's not a valid option.")
                    print("Please select a valid option or enter its corresponding number.")
                    continue

                #confirm clothing subcategory selection or restart
                clothing_sub_cat_name_answer = item_category_confirmation(clothing_sub_cat_name)
                if clothing_sub_cat_name_answer == "y":
                    clothing_classification = clothing_sub_cat_name
                    break
                elif clothing_sub_cat_name_answer == "n":
                    continue

        #choose home/furniture subcategory
        elif item_classification == "Home/Furniture":
            while True:
                print("What home/furniture subcategory does this item best fit under?")
                home_sub_cat = input("-Furniture(1) -Kitchen(2) -Appliances(3) -Home Decor(4) -Lighting(5) -Bedding(6) -Bathroom(7) -Storage/Organization(8) -Tools/Hardware(9) -Garden/Yard(10) -Office Furniture(11) -Home Improvement(12) -Other(13) ").strip().lower()
                if home_sub_cat in ("furniture", "1"):
                    home_sub_cat_name = "Furniture"
                elif home_sub_cat in ("kitchen", "2"):
                    home_sub_cat_name = "Kitchen"
                elif home_sub_cat in ("appliance", "appliances", "3"):
                    home_sub_cat_name = "Appliances"
                elif home_sub_cat in ("home decor", "decor", "4"):
                    home_sub_cat_name = "Home Decor"
                elif home_sub_cat in ("lightning", "5"):
                    home_sub_cat_name = "Lighting"
                elif home_sub_cat in ("bed", "bedding", "6"):
                    home_sub_cat_name = "Bedding"
                elif home_sub_cat in ("bathroom", "bath", "7"):
                    home_sub_cat_name = "Bathroom"
                elif home_sub_cat in ("storage", "organization", "storage/organization", "8"):
                    home_sub_cat_name = "Storage/Organization"
                elif home_sub_cat in ("tools", "hardware", "tools/hardware", "9"):
                    home_sub_cat_name = "Tools/Hardware"
                elif home_sub_cat in ("garden", "yard", "garden/yard", "10"):
                    home_sub_cat_name = "Garden/Yard"
                elif home_sub_cat in ("office", "office furniture", "11"):
                    home_sub_cat_name = "Office Furniture"
                elif home_sub_cat in ("home improvement", "improvement", "12"):
                    home_sub_cat_name = "Home Improvement"
                elif home_sub_cat in ("other", "13"):
                    home_sub_cat_name = "Other"
                else:
                    print("Sorry, that's not a valid option.")
                    print("Please select a valid option or enter its corresponding number.")
                    continue
                
                home_sub_cat_name_answer = item_category_confirmation(home_sub_cat_name)
                if home_sub_cat_name_answer == "y":
                    break
                elif home_sub_cat_name_answer == "n":
                    continue
                
        #choose collectible subcategory
        elif item_classification == "Collectibles":
            while True:
                print("What collectibles subcategory does this item best fit under?")
                collect_sub_cat = input("-Trading Cards(1) -Coins/Currency(2) -Stamps(3) -Sports Memorabilia(4) -Autographs(5) -Action Figures(6) -Statues/Figurines(7) -Comics(8) -Vintage Collectibles(9) -Avertising Memorobilia(10) -Antiques(11) -Rare/Valuable Items(12) -Other(13) ").strip().lower()
                if collect_sub_cat in ("trading", "cards", "trading cards", "1"):
                    collect_sub_cat_name = "Trading Cards"
                elif collect_sub_cat in ("coins", "currency", "coins/currency", "2"):
                    collect_sub_cat_name = "Coins/Currency"
                elif collect_sub_cat in ("stamp", "stamps", "3"):
                    collect_sub_cat_name = "Stamps"
                elif collect_sub_cat in ("sports", "sports memorobilia", "4"):
                    collect_sub_cat_name  = "Sports Memorobilia"
                elif collect_sub_cat in ("autographs", "autos", "5"):
                    collect_sub_cat_name = "Autographs"
                elif collect_sub_cat in ("action", "action figures", "6"):
                    collect_sub_cat_name = "Action Figures"
                elif collect_sub_cat in ("statue", "statues", "figurines", "statues/figurines", "7"):
                    collect_sub_cat_name = "Statues/Figurines"
                elif collect_sub_cat in ("comic", "comics", "8"):
                    collect_sub_cat_name = "Comics"
                elif collect_sub_cat in ("vintage", "vintage collectibles", "9"):
                    collect_sub_cat_name = "Vintage Collectibles"
                elif collect_sub_cat in ("adverts", "advertising", "advertising memorobilia", "10"):
                    collect_sub_cat_name = "Advertising Memorobilia"
                elif collect_sub_cat in ("antique", "antiques", "11"):
                    collect_sub_cat_name = "Antiques"
                elif collect_sub_cat in ("rare", "valuable", "rare/valuable", "rare/valuable items", "12"):
                    collect_sub_cat_name = "Rare/Valuable Items"
                elif collect_sub_cat in ("other", "13"):
                    collect_sub_cat_name = "Other"                   
                else:
                    print("Sorry, that's not a valid option.")
                    print("Please select a valid option or enter its corresponding number.")
                    continue

                collect_sub_cat_name_answer = item_category_confirmation(collect_sub_cat_name)
                if collect_sub_cat_name_answer == "y":
                    break
                elif collect_sub_cat_name_answer == "n":
                    continue

        #choose toy/game subcategory
        elif item_classification == "Toys/Games":
            while True:
                print("What toys/games subcategory does this item best fit under?")
                toy_sub_cat = input("-Board Games(1) -Card Games(2) -Video Games(3) -Gaming Consoles(4) -Puzzles(5) -LEGO/Building Sets(6) -Action Figures(7) -Dolls(8) -RC Vehicles(9) -Outdoor Toys(10) -Educational Toys(11) -Plush(12) -Vintage Toys(13) -Other(14) ").strip().lower()
                if toy_sub_cat in ("board", "board game", "board games", "1"):
                    toy_sub_cat_name = "Board Games"
                elif toy_sub_cat in ("card", "card games", "2"):
                    toy_sub_cat_name = "Card Games"
                elif toy_sub_cat in ("video", "video games", "3"):
                    toy_sub_cat_name = "Video Games"
                elif toy_sub_cat in ("gaming consoles", "gaming", "4"):
                    toy_sub_cat_name = "Gaming Consoles"
                elif toy_sub_cat in ("puzzle", "puzzles", "puzzling, is it not?", "5"):
                    toy_sub_cat_name = "Puzzles"
                elif toy_sub_cat in ("lego", "building", "building sets", "lego/building sets", "6"):
                    toy_sub_cat_name = "LEGO/Building Sets"
                elif toy_sub_cat in ("action", "action figures", "7"):
                    toy_sub_cat_name = "Action Figures"
                elif toy_sub_cat in ("doll", "dolls", "8"):
                    toy_sub_cat_name = "Dolls"
                elif toy_sub_cat in ("rc", "vehicles", "rc vehivles", "9"):
                    toy_sub_cat_name = "RC Vehicles"
                elif toy_sub_cat in ("outdoor", "outdoor toys", "10"):
                    toy_sub_cat_name = "Outdoor Toys"
                elif toy_sub_cat in ("education", "educational toys", "education toys", "ejimucation", "11"):
                    toy_sub_cat_name = "Educational Toys"
                elif toy_sub_cat in ("plush", "plushies", "12"):
                    toy_sub_cat_name = "Plush"
                elif toy_sub_cat in ("vintage", "vintage toys", "13"):
                    toy_sub-cat_name = "Vintage Toys"
                elif toy_sub_cat in ("other", "14"):
                    toy_sub_cat_name = "Other"
                else:
                    print("Sorry, that's not a valid option.")
                    print("Please select a valid option or enter its corresponding number.")
                    continue

                toy_sub_cat_name_answer = item_category_confirmation(toy_sub_cat_name)
                if toy_sub_cat_name_answer == "y":
                    break
                elif toy_sub_cat_name_answer == "n":
                    continue

        #choose books/media subcategory
        elif item_classification == "Books/Media":
            while True:
                print("What books/media subcategory does this item best fit under?")
                books_sub_cat = input("-Fiction(1) -Nonfiction(2) -Textbooks(3) -Academic/Professeional(4) -Children's Books(5) -Comics/Manga(6) -Rare/Collectible Books(7) -DVDs/Blu-Ray(8) -CDs(9) -Vinyl Records(10) -Video Games(11) -Magazines(12) -Other(13) ").strip().lower()
                if books_sub_cat in ("fiction", "1"):
                    books_sub_cat_name = "Fiction"
                elif books_sub_cat in ("nonfiction", "2"):
                    books_sub_cat_name = "Nonfiction"
                elif books_sub_cat in ("textbooks", "3"):
                    books_sub_cat_name = "Textbooks"
                elif books_sub_cat in ("academic", "professional", "academic/professional", "4"):
                    books_sub_cat_name = "Academic/Professional"
                elif books_sub_cat in ("children", "children's", "children's books", "5"):
                    books_sub_cat_name = "Children's Books"
                elif books_sub_cat in ("comic", "comics", "manga", "comics/manga", "6"):
                    books_sub_cat_name = "Comics/Manga"   
                elif books_sub_cat in ("rare", "collectible", "rare books", "collectible books", "rare/collectible books", "7"):
                    books_sub_cat_name = "Rare/Collectible Books"
                elif books_sub_cat in ("dvd", "dvds", "blu", "blu-ray", "dvds/blu-ray", "8"):
                    books_sub_cat_name = "DVDs/Blu-Ray"
                elif books_sub_cat in ("cd", "cds", "9"):
                    books_sub_cat_name = "CDs"
                elif books_sub_cat in ("vinyl", "records", "vinyl records", "10"):
                    books_sub_cat_name = "Vinyl Records"
                elif books_sub_cat in ("video games", "11"):
                    books_sub_cat_name = "Video Games"
                elif books_sub_cat in ("magazine", "mag", "magazines", "12"):
                    books_sub_cat_name = "Magazines"
                elif books_sub_cat in ("other", "13"):
                    books_sub_cat_name = "Other"
                else:
                    print("Sorry, that's not a valid option.")
                    print("Please select a valid option or enter its corresponding number.")
                    continue

                books_sub_cat_name_answer = item_category_confirmation(books_sub_cat_name)
                if books_sub_cat_name_answer == "y":
                    break
                elif books_sub_cat_name_answer == "n":
                    continue

        #choose sports/outdoors subcategory
        elif item_classification == "Sports/Outdoors":
            while True:
                print("What sports/outdoors subcategory does this item best fit under?")
                sports_sub_cat = input("-Camping(1) -Hiking(2) -Fishing(3) -Hunting(4) -Cycling(5) -Golf(6) -Fitness/Gym Equipmnet(7) -Running(8) -Water Sports(9) -Winter Sports(10) -Team Sports(11) -Sporting Goods(12) -Outdoor Recreation(13) -Other(14) ").strip().lower()
                if sports_sub_cat in ("camp", "camping", "glamping", "1"):
                    sports_sub_cat_name = "Camping"
                elif sports_sub_cat in ("hike", "take a hike!", "hiking", "2"):
                    sports_sub_cat_name = "Hiking"
                elif sports_sub_cat in ("fish", "fishing", "3"):
                    sports_sub_cat_name = "Fishing"
                elif sports_sub_cat in ("hunt", "hunting", "4"):
                    sports_sub_cat_name = "Hunting"
                elif sports_sub_cat in ("cycle", "bike", "biking", "cycling", "5"):
                    sports_sub_cat_name = "Cycling"
                elif sports_sub_cat in ("golf", "golfing", "6"):
                    sports_sub_cat_name = "Golfing"
                elif sports_sub_cat in ("fitness", "gym", "fitness equipment", "gym equipment", "fitnes//gym equipment", "7"):
                    sports_sub_cat_name = "Fitness/Gym Equipment"
                elif sports_sub_cat in ("run", "running", "8"):
                    sports_sub_cat_name = "Running"
                elif sports_sub_cat in ("water", "water sports", "9"):
                    sports_sub_cat_name = "Water Sports"
                elif sports_sub_cat in ("winter", "winter sports", "10"):
                    sports_sub_cat_name = "Winter Sports"
                elif sports_sub_cat in ("team", "team sports" "11"):
                    sports_sub_cat_name = "Team Sports"
                elif sports_sub_cat in ("sporting", "sporting goods", "12"):
                    sports_sub_cat_name = "Sporting Goods"
                elif sports_sub_cat in ("outdoor", "outdoor rec", "outdoor recreation", "13"):
                    sports_sub_cat_name = "Outdoor Recreation"
                elif sports_sub_cat in ("other", "14"):
                    sports_sub_cat_name = "Other"
                else:
                    print("Sorry, that's not a valid option.")
                    print("Please select a valid option or enter its corresponding number.")
                    continue

                sports_sub_cat_name_answer = item_category_confirmation(sports_sub_cat_name)
                if sports_sub_cat_name_answer == "y":
                    break
                elif sports_sub_cat_name_answer == "n":
                    continue

        #choose jewelry/accessories subcategory
        elif item_classification == "Jewelry/Accessories":
            while True:
                print("What jewelry/accessories subcategory does this item best fit under?")
                jewelry_sub_cat = input("-Rings(1) -Necklaces(2) -Bracelets(3) -Earrings(4) -Watches(5) -Sunglasses(6) -Handbags/Purses(7) -Wallets(8) -Belts(9) -Hats(10) -Designer Accessories(11) -Fine Jewelry(12) -Costume Jewelry(13) -Other(14) ").strip().lower()
                if jewelry_sub_cat in ("ring", "rings", "1"):
                    jewelry_sub_cat_name = "Rings"
                elif jewelry_sub_cat in ("neck", "necklace", "necklaces", "2"):
                    jewelry_sub_cat_name = "Necklaces"
                elif jewelry_sub_cat in ("bracelet", "bracelets", "3"):
                    jewelry_sub_cat_name = "Bracelets"
                elif jewelry_sub_cat in ("earrings", "ear", "earring", "4"):
                    jewelry_sub_cat_name = "Earrings"
                elif jewelry_sub_cat in ("watch", "watches", "5"):
                    jewelry_sub_cat_name = "Watches"
                elif jewelry_sub_cat in ("sunglasses", "sunnies", "6"):
                    jewelry_sub_cat_name = "Sunglasses"
                elif jewelry_sub_cat in ("handbag", "handbags", "purse", "purses", "handbags/purses", "7"):
                    jewelry_sub_cat_name = "Handbags/Purses"
                elif jewelry_sub_cat in ("wallet", "wallets", "coin purse", "8"):
                    jewelry_sub_cat_name = "Wallets"
                elif jewelry_sub_cat in ("belt", "belts", "9"):
                    jewelry_sub_cat_name = "Belts"
                elif jewelry_sub_cat in ("hat", "hats", "10"):
                    jewelry_sub_cat_name = "Hats"
                elif jewelry_sub_cat in ("designer", "designer accessories", "11"):
                    jewelry_sub_cat_name = "Designer Accessories"
                elif jewelry_sub_cat in ("fine", "fine jewelry", "12"):
                    jewelry_sub_cat_name = "Fine Jewelry"
                elif jewelry_sub_cat in ("costume", "costume jewelry", "13"):
                    jewelry_sub_cat_name = "Costume Jewelry"
                elif jewelry_sub_cat in ("other", "14"):
                    jewelry_sub_cat_name = "Other"
                else:
                    print("Sorry, that's not a valid option.")
                    print("Please select a valid option or enter its corresponding number.")
                    continue

                jewelry_sub_cat_name_answer = item_category_confirmation(jewelry_sub_cat_name)
                if jewelry_sub_cat_name_answer == "y":
                    break
                elif jewelry_sub_cat_name_answer == "n":
                    continue

        #choose beauty/personal care subcategory
        elif item_classification =="Beauty/Personal Care":
            while True:
                print("What beauty/personal care subcategory does this item best fit under?")
                beauty_sub_cat = input("-Skincare(1) -Haircare(2) -Makeup(3) -Fragrances(4) -Grooming(5) -Hair Tools(6) -Personal Care Appliances(7) -Bath/Body(8) -Beauty Accessories(9) -Professional/Spa Equipment(10) -Other(11) ").strip().lower()
                if beauty_sub_cat in ("skin", "skincare", "1"):
                    beauty_sub_cat_name = "Skincare"
                elif beauty_sub_cat in ("haircare", "2"):
                    baeuty_sub_cat_name = "Haircare"
                elif beauty_sub_cat in ("makeup", "3"):
                    baeuty_sub_cat_name = "Makeup"
                elif beauty_sub_cat in ("fragrances", "frog races", "4"):
                    beauty_sub_cat_name = "Fragrances"
                elif beauty_sub_cat in ("grooming", "5"):
                    beauty_sub_cat_name = "Grooming"
                elif beauty_sub_cat in ("hair tools", "6"):
                    beauty_sub_cat_name = "Hair Tools"
                elif beauty_sub_cat in ("personal care", "personal care appliances", "appliances" "7"):
                    beauty_sub_cat_name = "Personal Care Appliances"
                elif beauty_sub_cat in ("bath", "body", "bath/body", "8"):
                    beauty_sub_cat_name = "Bath/Body"
                elif beauty_sub_cat in ("beauty accessories", "accessories", "9"):
                    beauty_sub_cat_name = "Beauty Accessories"
                elif beauty_sub_cat in ("professional", "spa", "professional equipment", "spa equipment", "professional/spa equipment", "10"):
                    beauty_sub_cat_name = "Professional/Spa Equipment"
                elif beauty_sub_cat in ("other", "11"):
                    beauty_sub_cat_name = "Other"                    
                else:
                    print("Sorry, that's not a valid option.")
                    print("Please select a valid option or enter its corresponding number.")
                    continue

                beauty_sub_cat_name_answer = item_category_confirmation(beauty_sub_cat_name)
                if beauty_sub_cat_name_answer == "y":
                    break
                elif beauty_sub_cat_name_answer == "n":
                    continue

        #choose hobbies/crafts subcategory
        elif item_classification == "Hobbies/Crafts":
            while True:
                print("What hobbies/crafts subcategory does this item best fit under?")
                hobb_sub_cat = input("-Sewing(1) -Knitting/Crochet(2) -Painting(3) -Drawing(4) -Scrapbooking(5) -Model Kits(6) -3D Printing(7) -Woodworking(8) -Musical Instruments(9) -Photography(10) -RC/Hobby Vehicles(11) -Craft Supplies(12) -Art Supplies(13) -Other(14) ").strip().lower()
                if hobb_sub_cat in ("sew", "sewing", "1"):
                    hobb_sub_cat_name = "Sewing"
                elif hobb_sub_cat in ("snit", "knitting", "crochet", "chochett", "knitting/crochet", "2"):
                    hobb_sub_cat_name = "Knitting/Crochet"
                elif hobb_sub_cat in ("pain", "painting", "3"):
                    hobb_sub_cat_name = "Painting"
                elif hobb_sub_cat in ("draw", "drawing", "4"):
                    hobb_sub_cat_name = "Drawing"
                elif hobb_sub_cat in ("scrap", "scrappy doo", "scrapbooking", "5"):
                    hobb_sub_cat_name = "Scrapbooking"
                elif hobb_sub_cat in ("model", "model kits", "6"):
                    hobb_sub_cat_name = "Model Kits"
                elif hobb_sub_cat in ("3d", "3d printing", "7"):
                    hobb_sub_cat_name = "3D Printing"
                elif hobb_sub_cat in ("wood", "woodworking", "8"):
                    hobb_sub_cat_name = "Woodworking"
                elif hobb_sub_cat in ("music", "musical", "instrument", "musical instruments", "instruments", "9"):
                    hobb_sub_cat_name = "Musical Instruments"
                elif hobb_sub_cat in ("photo", "photos", "photograph", "photography", "10"):
                    hobb_sub_cat_name = "Photography"
                elif hobb_sub_cat in ("rc", "hobby vehicles", "rc vehicles", "rc/hobby vehicles", "11"):
                    hobb_sub_cat_name = "RC/Hobby Vehicles"
                elif hobb_sub_cat in ("craft", "crafting", "craft supplies", "12"):
                    hobb_sub_cat_name = "Craft Supplies"
                elif hobb_sub_cat in ("art", "artsy", "art supplies", "13"):
                    hobb_sub_cat_name = "Art Supplies"
                elif hobb_sub_cat in ("other", "14"):
                    hobb_sub_cat_name = "Other"
                else:
                    print("Sorry, that's not a valid option.")
                    print("Please select a valid option or enter its corresponding number.")
                    continue

                hobb_sub_cat_name_answer = item_category_confirmation(hobb_sub_cat_name)
                if hobb_sub_cat_name_answer == "y":
                    break
                elif hobb_sub_cat_name_answer == "n":
                    continue

        #choose industrial/business equipment subcategory
        elif item_classification == "Industrial/Business Equiment":
            while True:
                print("What industrial/business equipment subcategory does this item best fit under?")
                ind_sub_cat = input("-Power Tools(1) -Hand Tools(2) -Construction Equipment(3) -Manufacturing Equipment(4) -Restaurant Equipment(5) -Office Equipment(6) -Medical Equipment(7) -Commercial Equipment(8) -Safety Equipment(9) -Warehouse Equipment(10) -Agricultural Equipment(11) -Automotive Shop Equipment(12) -Industrial Parts(13) -Other(14)").strip().lower()
                if ind_sub_cat in ("power", "power tool", "power tools", "1"):
                    ind_sub_cat_name = "Power Tools"
                elif ind_sub_cat in ("hand tools", "hand", "2"):
                    ind_sub_cat_name = "Hand Tools"
                else:
                    print("Sorry, that's not a valid option.")
                    print("Please select a valid option or enter its corresponding number.")
                    continue

                ind_sub_cat_name_answer = item_category_confirmation(ind_sub_cat_name)
                if ind_sub_cat_name_answer == "y":
                    break
                elif ind_sub_cat_name_answer == "n":
                    continue

        #choose miscellaneous subcategory
        elif item_classification == "Miscellaneous":
            while True:
                print("What miscellaneous subcategory does this item best fit under?")
                misc_sub_cat = input("-Pet Supplies(1) -Baby/Kids(2) -Musical Equipment(3) -Party/Event Supplies(4) -Travel/Luggage(5) -Religious Items(6) -Seasonal/Holiday(7) -Promotional Merchandise(8) -Specialty Items(9) -Other(10) ").strip().lower()



    #multiple items choice loop
    '''elif item_type_choice == "multiple":
        while True:
            multiple_items_number = input("How many different items are you looking to buy? ").strip().lower()
            try:
                multiple_items_number = int(multiple_items_number)
                if multiple_items_number <= 0:
                    print("sorry, ")'''




    




#print(sales_tax_dict)