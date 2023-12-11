from bs4 import BeautifulSoup
import requests
import scrapeutils 
import time

delayValue = 1

searchResults = {}

# def kj_search(locations: str, categoryCode: str , searchTerm: str, locationCode: str) -> dict:
def kj_search(url: str) -> dict:
    """
    Extract listing from Kijiji

    User inputs URL of the first page of their search
    
    """
    # url = f'https://www.kijiji.ca/{categoryCode}/{locations}/{searchTerm}/{locationCode}'
    # print(url)

    homeURL = scrapeutils.getHomeURL(url)


    searchNumber = 1
    while url != 'N/A':
        response = requests.get(url, timeout=10)
        content = BeautifulSoup(response.content, "html.parser")

        listing_items = content.findAll('section', {'data-testid': 'listing-card'})

        # linkTarget = content.findAll('li', {'data-testid': 'pagination-next-link'})
        # print(linkTarget)
        # print(listing_items)


        
        for listing_item in listing_items:
            
            # price = listing_item.find('p', {'data-testid': 'listing-price'}).text.strip()
            price = listing_item.find('p', {'data-testid': 'listing-price'})
            cleaned_price_text = price.text.strip().replace('$', '').replace(',', '') if price else '0'
            # this is for when the price is Please/Contact or Swap/Trade
            try:
                price = float(cleaned_price_text)
            except ValueError:
                price = cleaned_price_text

            title = listing_item.find('a', {'data-testid': 'listing-link'}).text.strip()

            location = listing_item.find('a', {'data-testid': 'listing-location'})
            location = location.text.strip() if location else 'N/A'

            link_tag = listing_item.find('a', href=True)
            link = link_tag.get('href') if link_tag else 'N/A'
            link = homeURL + link

            # print(f"Title: {title}\nPrice: {price}\n")
            # print(f"Title: {title}\nPrice: {price}\nLocation: {location}\nLink: {link}\n{'-' * 30}\n")


            searchResults[searchNumber] = [price, title, location, link]

            searchNumber+=1

        nextLink = scrapeutils.getNextPageLinkKijiji(url)

        url = nextLink
        time.sleep(delayValue)

    return searchResults

