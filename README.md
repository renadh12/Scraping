# Web Scraping using Python

## Scraping Quote Project

### Project Description

This is a scraping project using Python's *BeautifulSoup, requests, csv and random* modules. Additionally, the script comes with a game logic. Since the legality of scraping can be sort 
of a mixed bag, I'd like to give a shoutout to ScrapingHub for coming up with this website - http://quotes.toscrape.com/ designed specifically for scraping practices. This particular
website contains 100 quotes by well-renowned people from around the globe. To sum up my Python script, each and every quote along with its author info
is scraped from the aforementioned site and written to a CSV file. Afterwards, the script grabs a random quote from the CSV file and asks the user to guess the author
of the quote. The user gets 4 attempts. For every failed guess, a hint is given until all 4 attempts have been used up.

### Getting Started

Git Instructions

SSH

1. `git clone git@github.com:renadh12/Scraping.git`

2. `git remote add origin git@github.com:renadh12/Scraping.git`

HTTPS

1. `git clone https://github.com/renadh12/Scraping.git`

2. `git remote add origin https://github.com/renadh12/Scraping.git`


### Prerequisites

#### Installation

You can perform all these installation command lines on your `terminal` or your text editor terminal like I did.

Install pip 

- `sudo easy_install pip`

Install bs4 to import BeautifulSoup to your script

- `python3 -m pip install bs4`

Install requests module

- `python3 -m pip install requests`

### Running the script

#### Step One
- Run `scrape_quote.py`
  - Scrapes all the quotes and author info from http://quotes.toscrape.com/ 
  - Writes scraped data to a csv file.

#### Step Two
- Run `quote_game.py`
  - Reads scraped data from the csv file
  - Returns scraped data in a list
  - Initiates the game
    - Grabs random quote from the list
    - Asks user to guess the the author of the quote
    - Offers a hint for every failed guess
    - User is given 4 attempts
    - Offers user the option to play again

### Built With

- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Python library for pulling data out of HTML and XML files.
- [requests](https://requests.readthedocs.io/en/master/) - Module that allows you to send HTTP requests using Python.

### Author
*Renadh Chowdhury*

### Acknowledgements
- _Udemy_
- _Colt Steele_
- _YouTube_

