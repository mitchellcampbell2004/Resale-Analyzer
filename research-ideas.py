#research-ideas.py
#Mitchell Campbell
'''The purpose of this file is for me to brainstorm workarounds for problems in my research.py file.'''

import urllib.request, urllib.parse, urllib.error 
from bs4 import BeautifulSoup 
import ssl #defaults to certificate verification and most secure protocol (now TLS)
import re #import regex
import csv #import csv

#ignore SSL/TLS certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#get url and open it
url = input('Enter URL: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

#find all the anchor tags + then isolate the categories
book_categories = soup.find_all("a")
category_count = 0
category_link_count = 0
book_list = []
first_book_dict = {}
book_category_list = []
book_soup_count = 0

print(book_categories)

for category in book_categories:
    category_link = category.get('href', None)
    if category_link.startswith("catalogue/category/books/") and category_count == 1: #isolate just the book categories, which in this case is a subcategory of book category, but is isolated with "...books/"

        new_category_link = "https://books.toscrape.com/" + category_link #for whatever reason, need to add the main page to the url; inspected the site, maybe b/c it comes from a different script?
        category_page = urllib.request.urlopen(new_category_link, context=ctx).read()
        category_soup = BeautifulSoup(category_page, 'html.parser')
        print(category_soup)
        category_count += 1



'''for category in book_categories:
    category_link = category.get('href', None)
    if category_link.startswith("catalogue/category/books/") and category_count == 1: #isolate just the book categories, which in this case is a subcategory of book category, but is isolated with "...books/"

        new_category_link = "https://books.toscrape.com/" + category_link #for whatever reason, need to add the main page to the url; inspected the site, maybe b/c it comes from a different script?
        category_page = urllib.request.urlopen(new_category_link, context=ctx).read()
        category_soup = BeautifulSoup(category_page, 'html.parser')

        #print(category_soup)
        category_count += 1'''