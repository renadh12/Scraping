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


# This function is going to start the guessing game.

def start_game(all_quotes):
    # Pick out a random quote from the all_quotes list using the choice function from random module
    quote = choice(all_quotes)
    print("Here's the quote: ")
    print(quote['text'])

    # Initialize guess user is going to input to None or empty string
    guess = ''

    # User gets 4 tries so initial value of the variable below is 4 which will decrement for every wrong guess
    remaining_guesses = 4

    # While the user's guess input is not equal to the author of the random quote, the script is going to keep asking
    # the user to try again with hints
    while guess.lower() != quote['author'].lower() and remaining_guesses > 0:
        guess = input(f"Who said this quote? Remaining Guesses: {remaining_guesses} \n")
        print(quote['author'])
        # Guesses decrement by 1 for each wrong guess
        remaining_guesses -= 1
        # print(quote['author'])  # Remove later
        # If the user gets the answer right, we are going to print CORRECT ANSWER and break
        if guess.lower() == quote['author'].lower():
            print("YES! CORRECT ANSWER!")
            break
        # Like mentioned above, user is going to be given a hint for every wrong guess
        # First hint - author's bio info : birth date & birth placedv
        if remaining_guesses == 3:
            print("Wrong! Here's a hint: ")
            res = requests.get(f"{BASE_URL}{quote['bio-link']}")
            soup = BeautifulSoup(res.text, "html.parser")
            birth_date = soup.find(class_="author-born-date").get_text()
            birth_place = soup.find(class_="author-born-location").get_text()
            print(f"The author was born on {birth_date} {birth_place}")

        # Second hint - first letter of author's first name
        elif remaining_guesses == 2:
            print("Nope! This hint might help: ")
            print(f"The first letter of author's first name is {quote['author'][0]}")

        # Third and last hint - first letter of author's last name & length of first and last names
        elif remaining_guesses == 1:
            names = quote['author'].split(" ")
            if len(names) == 3:
                last_initial = names[2][0]
                first = len(names[0])
                middle = len(names[1])
                last = len(names[2])
                print(f"Incorrect! Two more hints for you : the first letter of author's last name is {last_initial}")
                print(f"Author's first name has {first} characters. Author's middle name has {middle} characters. "
                      f"Last name has {last} characters")
            elif len(names) == 2:
                last_initial = names[1][0]
                first_name_len = len(quote['author'].split(" ")[0])
                last_name_len = len(quote['author'].split(" ")[1])
                print(f"Incorrect! Two more hints for you : the first letter of author's last name is {last_initial}")
                print(f"Author's first name has {first_name_len} characters. Author's last name has {last_name_len} "
                      f"characters.")


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
