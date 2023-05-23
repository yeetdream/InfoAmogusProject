from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# Variable to store website link as string
myurl = 'http://books.toscrape.com/catalogue/category/books/classics_6/index.html'

# Grab website and store in variable uclient
uClient = uReq(myurl)

# Read and close HTML
page_html = uClient.read()
uClient.close()

# Call BeautifulSoup for parsing
page_soup = soup(page_html, "html.parser")

# Grabs all the products under list tag
bookshelf = page_soup.findAll(
 "li", {"class": "col-xs-6 col-sm-4 col-md-3 col-lg-3"})

# Create csv file of all products
filename = ("Books.csv")
f = open(filename, "w")

headers = "Book title, Price\n"
f.write(headers)

for books in bookshelf:
 # Collect title of all books
 book_title = books.h3.a["title"]

 # Collect book price of all books
 book_price = books.findAll("p", {"class": "price_color"})
 price = book_price[0].text.strip()

 print("Title: " + book_title)
 print("Price: " + price + '\n')
 f.write(book_title + "," + price+"\n")

f.close()