#Web Scraper Project
#100daysofcode (day 3)
#Wisdom Alawode

#Importing necessary libaries
import requests
from bs4 import BeautifulSoup

#defining the url to be scraped
url = "http://quotes.toscrape.com"
response = requests.get(url)

if response.status_code == 200:
    print("Successfully fetched page")
    
    soup = BeautifulSoup(response.text, 'html.parser')

    print(f"Page title: {soup.title.text}")
    
    # Finding all quotes
    quotes = soup.find_all('div', class_='quote')
    
    print(f"Found {len(quotes)} quotes")
    
    #printing found quotes
    if quotes:
        for quote in quotes:
            text = quote.find('span', class_='text').text
            author = quote.find('small', class_='author').text
            print(f'"{text}" - {author}')
            print()
    else:
        print("No quotes found! Let me show you what the page looks like:")
        print(soup.prettify()[:1000])  # Printing first 1000 characters of the HTML
else:
    print(f"Failed to fetch page. Status code: {response.status_code}")



    