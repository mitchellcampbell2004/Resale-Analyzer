#research.py
#Mitchell Campbell
'''The purpose of this program is to collect information to build a database of the best-selling types of items for resale.'''

#things I've learned:
#Using "r" before the string in a regex search tells python to give the string to regex as is and not let things like \n or \t in python mess it up



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
book_category_list = []
for category in book_categories:
    category_name = category.get_text(strip=True) #get the text from a tags and strip them
    if len(category_name) >=1 and category_name not in ("Books to Scrape", "Home", "Books"): #forego other a tags and get to product categories (need to *****need to figure out how to apply it to different sites w/ different a tags)
        if category_count != 50: #print only the category names and not other a tags hanging around (*****need to figure out how to apply it to other sites that don't have exactly 50 categories)
            #print(category_name)
            book_category_list.append(category_name)
            category_count += 1
#print(book_category_list)

with open("books.csv", "a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    for book_category in book_category_list:
        writer.writerow(["Category"])






#######Main Code