from bs4 import BeautifulSoup
import requests
import xlsxwriter

def dl_search(dealername):

    searchResults = {}

    url = "https://www.calgaryharleydavidson.ca/default.asp?page=inventory&condition=pre-owned&pg=1"

    response = requests.get(url, timeout=5)
    content = BeautifulSoup(response.content, "html.parser")
    # print(f"*******************{content.prettify}")

    pageInfo = content.find("span", class_="v7list-pagination__page").text.strip()
    totalPages= int(pageInfo.split()[-1])
    # print(totalPages)

    listing_items = content.findAll('li', class_='v7list-results__item')
    # print(listing_items)


    searchNumber = 1
    for listing_item in listing_items:
                
        # Extract title
        year = listing_item.find('span', class_='vehicle-heading__year').text.strip()
        model = listing_item.find('span', class_='vehicle-heading__model').text.strip()


        # Extract price
        # price = listing_item.find('span', class_='vehicle-price__price')
        price = listing_item.find('span', class_="vehicle-price vehicle-price--current") # this addition is necessary or else the bottom may settle on the 'strike price' rather current price
        price = price.find('span', class_='vehicle-price__price') 
    
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

        print(f"Title: {year, model}\nPrice: {price}\nLocation: {location}\nLink: {link}\n{'-' * 30}\n")

        searchResults[searchNumber] = [price, year, model, location, link]

        searchNumber+=1

        return searchResults

pageInfo = content.find("span", class_="v7list-pagination__page").text.strip()
totalPages= int(pageInfo.split()[-1])
print(totalPages)

def cl_search(locations, searchTerm):
    searchNumber = 1
    for each in locations:
        url = f'https://{each}.craigslist.org/search/mca?query={searchTerm}#search=1~gallery~0~0'
        # print(url)

        response = requests.get(url, timeout=5)
        content = BeautifulSoup(response.content, "html.parser")
        # print(f"*******************{content.prettify}")

        listing_items = content.findAll('li', class_='cl-static-search-result')
        # print(listing_items)

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