#research.py
#Mitchell Campbell
'''The purpose of this program is to collect information to build a database of the best-selling types of items for resale.'''

#things I've learned:
#Using "r" before the string in a regex search tells python to give the string to regex as is and not let things like \n or \t in python mess it up
#Practiced using regex to isolate portions of a string



import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl # defaults to certificate verification and most secure protocol (now TLS)
import re #import regex
import csv

#ignore SSL/TLS certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#get url and open it
url = input('Enter URL: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

#print(soup)
book_categories = soup.find_all("a")
category_count = 0
category_link_count = 0
book_dict = {}
book_category_list = []
for category in book_categories:
    #category_name = category.get_text(strip=True) #get the text from a tags and strip them
    #if len(category_name) >=1 and category_name not in ("Books to Scrape", "Home", "Books"): #forego other a tags and get to product categories (need to *****need to figure out how to apply it to different sites w/ different a tags)
        #if category_count != 50: #print only the category names and not other a tags hanging around (*****need to figure out how to apply it to other sites that don't have exactly 50 categories)
            #print(category_name)
            #category_count += 1
    category_link = category.get('href', None)
    if category_link.startswith("catalogue/category/books/") and category_count < 1: #isolate just the book categories, which in this case is a subcategory of book category, but is isolated with "...books/"

        new_category_link = "https://books.toscrape.com/" + category_link #for whatever reason, need to add the main page to the url; inspected the site, maybe b/c it comes from a different script?
        category_page = urllib.request.urlopen(new_category_link, context=ctx).read()
        category_soup = BeautifulSoup(category_page, 'html.parser')
        
        book_anchors = category_soup.find_all("h3") #isolate the specific products by their identifying variable; in this case, h3; can't do find a's first and then find h3s, because find as turns it into a list
        #doesn't matter:   for book_anchor in book_anchors:
            #get book page link; most of the stuff below this doesn't matter b/c the book links don't go by type, they go just in the overall catalogue
            #doesn't matter   book_anchor_string = str(book_anchor)
            #doesn't matter:   book_link = re.search("/../..(.+)/index", book_anchor_string) #[^/]+ = any character except /
            #doesn't matter:  book_link = (book_link.group(1)) #need group because it'll return a match object string; group() gives you the entire regex match, group(1) gives you just the part you asked for
            #doesn't matter:   category_link_portion = new_category_link[:-11] #subtract the last 11 char of new_cat_link so that I can get rid of index, creating first part of final book string
            #doesn't matter:   book_link_portion = book_link + "/index.html" #add index to book link to create last part of final book link
            # doesn't matter:   final_book_link = category_link_portion + book_link_portion #add links together to make final book string
            #doesn't matter:   print(final_book_link)

        #doesn't matter:  open book page (final product page) and parse data
        #doesn't matter   book_link_page = urllib.request.urlopen(final_book_link, context=ctx).read()
        #doesn't matter:   book_soup = BeautifulSoup(book_link_page, 'html.parser')
        
        
        book_soup_count = 0
        if book_soup_count < 1:
            print(book_soup)
            book_soup_count += 1

            
            
        #book_name = book_name_anchor.get_text(strip=True)
        #print(book_name)
        #for book_name in book_names:
            #print(book_name)
        category_count += 1
        #category_link_count += 1, this is not needed rn
        





#print(book_category_list)

#with open("books.csv", "a", newline="", encoding="utf-8") as file:
    #writer = csv.writer(file)

    #for book_category in book_category_list:
        #writer.writerow(["Category"])






#######Main Code