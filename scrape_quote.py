from bs4 import BeautifulSoup
from random import choice
import requests


def scrape_quote():
    BASE_URL = "http://quotes.toscrape.com/"
    url = "/page/1"

    while url:
        res = requests.get(f"{BASE_URL}{url}")  # Sending a request to the web page download the HTML
        soup = BeautifulSoup(res.text,
                             'html.parser')  # Grabbing and parsing the HTML data using BeautifulSoup so we can
        # navigate via the tags and CSS selectors
        quotes = soup.find_all(
            class_='quote')  # Retrieve all the quotes from each page from the quote class from the parsed HTML data

        all_quotes = []  # We are going to append all the required data into this list - quote, author and author bio.

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

        quote = choice(all_quotes)
        print("Here's the quote: ")
        print(quote['text'])
        auth = quote['author']
        guess = ''
        remaining_guesses = 4

        while guess.lower() != auth.lower():
            guess = input(f"Who said this quote? Remaining Guesses: {remaining_guesses}")
            remaining_guesses -= 1

            if remaining_guesses == 3:
                print("Here's a hint: ")
                res = requests.get(f"{BASE_URL}{quote['bio-link']}")
                soup = BeautifulSoup(res.text, "html.parser")
                birth_date = soup.find(class_="author-born-date").get_text()
                birth_place = soup.find(class_="author-born-location").get_text()
                print(f"The author was born on {birth_date} {birth_place}")

            elif remaining_guesses ==2:
                print("Here's a hint: ")
                print(f"The first letter of author's first name is {auth[0]}")

            elif remaining_guesses ==1:
                last_initial = auth.split(" ")[1][0]
                print(f"The first letter of author's last name is {last_initial}")




scrape_quote()
