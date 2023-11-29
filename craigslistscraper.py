from bs4 import BeautifulSoup
import requests
import xlsxwriter


searchResults = {}

# locations=["vancouver","abbotsford", "edmonton"]
# searchTerm="wide%20glide"

def cl_search(locations, searchTerm):
    searchNumber = 1
    for each in locations:
        url = f'https://{each}.craigslist.org/search/mca?query={searchTerm}#search=1~gallery~0~0'
        # print(url)
        response = requests.get(url, timeout=5)
        content = BeautifulSoup(response.content, "html.parser")

        listing_items = content.findAll('li', class_='cl-static-search-result')

        for listing_item in listing_items:
            
            # Extract title
            title = listing_item.find('div', class_='title').text.strip()

            # Extract price
            price = listing_item.find('div', class_='price')
            # price = price.text.strip() if price else 'N/A'

            # price = float(price.text.strip().replace('$', '').replace(',', '')) if price else 0.0 <-- this is equivalent to below
            # Check if 'price' element exists
            if price:
                # Extract text content, strip whitespaces, remove '$' and commas, convert to float
                cleaned_price_text = price.text.strip().replace('$', '').replace(',', '')
                price = float(cleaned_price_text)
            else:
                # If 'price' element doesn't exist, default to 0.0
                price = 0.0


            # Extract location
            location = listing_item.find('div', class_='location')
            location = location.text.strip() if location else 'N/A'

            link_tag = listing_item.find('a', href=True)
            link = link_tag.get('href') if link_tag else 'N/A'


            searchResults[searchNumber] = [price, title, location, link]

            searchNumber+=1

    # print(searchResults)
    return searchResults

# cl_search(locations,searchTerm)
# print(searchResults)