from bs4 import BeautifulSoup
from random import choice
import requests

BASE_URL = "http://quotes.toscrape.com/"  # Caps variable name because it's a constant


def scrape_quote():
    all_quotes = []  # We are going to append all the required data into this list - quote, author and author bio.
    url = "/page/1"  # There are multiple pages on this site, we start at Page 1

    while url:
        res = requests.get(f"{BASE_URL}{url}")  # Sending a request to the web page download the HTML
        soup = BeautifulSoup(res.text,
                             'html.parser')  # Grabbing and parsing the HTML data using BeautifulSoup so we can
        # navigate via the tags and CSS selectors
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


def start_game(all_quotes):
    quote = choice(all_quotes)
    print("Here's the quote: ")
    print(quote['text'])
    guess = ''
    remaining_guesses = 4

    while guess.lower() != quote['author'].lower() and remaining_guesses > 0:
        guess = input(f"Who said this quote? Remaining Guesses: {remaining_guesses} \n")
        remaining_guesses -= 1
        # print(quote['author'])  # Remove later

        if guess.lower() == quote['author'].lower():
            print("CORRECT ANSWER")

        if remaining_guesses == 3:
            print("Here's a hint: ")
            res = requests.get(f"{BASE_URL}{quote['bio-link']}")
            soup = BeautifulSoup(res.text, "html.parser")
            birth_date = soup.find(class_="author-born-date").get_text()
            birth_place = soup.find(class_="author-born-location").get_text()
            print(f"The author was born on {birth_date} {birth_place}")

        elif remaining_guesses == 2:
            print("Here's a hint: ")
            print(f"The first letter of author's first name is {quote['author'][0]}")

        elif remaining_guesses == 1:
            last_initial = quote['author'].split(" ")[1][0]
            print(f"The first letter of author's last name is {last_initial}")

        else:
            print(f"You have used up all your remaining guesses. The name of the author is {quote['author']}")

    again = ''
    while again.lower() not in ('y', 'yes', 'n', 'no'):
        again = input("Would you like to play the game again (y, yes/ n, no)")
    if again.lower() in ('y', 'yes'):
        return start_game(all_quotes)
    else:
        print("Have a wonderful day! Goodbye.")


quotes = scrape_quote()
start_game(quotes)
