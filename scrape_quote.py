from bs4 import BeautifulSoup
from random import choice
import requests
from csv import DictWriter

BASE_URL = "http://quotes.toscrape.com/"  # Caps variable name because it's a constant


def scrape_quote():
    all_quotes = []  # We are going to append all the required data into this list - quote, author and author bio.
    url = "/page/1"  # There are multiple pages on this site, we start at Page 1

    while url:
        # Sending a request to the web page to download the HTML
        res = requests.get(f"{BASE_URL}{url}")

        '''Grabbing and parsing the HTML data using BeautifulSoup so we can 
           navigate via the tags and CSS selectors'''

        soup = BeautifulSoup(res.text, 'html.parser')
        quotes = soup.find_all(
            class_='quote')  # Retrieve all the quotes from each page from the quote class from the parsed HTML data

        # Iterate over each quote to grab the text, author_name and the href tag for bio info
        for quote in quotes:
            all_quotes.append({
                "text": quote.find(class_='text').get_text(),
                # Retrieve the inner text from the text class inside the quote class
                "author": quote.find(class_='author').get_text(),
                # Retrieve author name from the author class inside the quote class
                "bio-link": quote.find("a")["href"]
                # Retrieve the href for our hints, we can use brackets to find single attribute
            })
        next_btn = soup.find(class_='next')
        url = next_btn.find('a')['href'] if next_btn else None

    return all_quotes


def write_quotes(quotes):
    with open("quotes.csv", "w") as file:
        # Write column names into a list first
        headers = ["text", "author", "bio-link"]
        # Going to use a DictWriter because we are dealing with a dictionary (quote is a dictionary that contains the
        # scraped data) to store all the scraped data(values) - we have to import DictWriter from csv module
        csv_writer = DictWriter(file, fieldnames=headers)
        # Write down the column names on the csv file
        csv_writer.writeheader()
        # Write all the rows (scraped data) on to the csv file
        for quote in quotes:
            csv_writer.writerow(quote)


quote_data = scrape_quote()
write_quotes(quote_data)
