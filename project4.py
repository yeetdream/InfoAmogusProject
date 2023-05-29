import requests
from bs4 import BeautifulSoup
from pprint import pprint

def parse_books(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    books = []
    for book in soup.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3'):
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text
        books.append((title, price[1:]))
    return books

url = 'http://books.toscrape.com/catalogue/category/books/classics_6/index.html'
pprint(parse_books(url))
