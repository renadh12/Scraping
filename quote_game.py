from random import choice
from bs4 import BeautifulSoup
import requests
from csv import DictReader

# Caps variable name because it's a constant
BASE_URL = "http://quotes.toscrape.com/"


def read_quotes(filename):
    with open(filename, "r") as file:
        csv_reader = DictReader(file)
        return list(csv_reader)


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


quotes = read_quotes('quotes.csv')
start_game(quotes)
