from bs4 import BeautifulSoup
import requests
import xlsxwriter


def dl_search(targetURL):

    searchResults = {}
    searchNumber = 1

    # Isolate homeURL to combine with partial link later to make full link 
    partsURL = targetURL.split('/')
    homeURL = '/'.join(partsURL[:3])

    # To set up for format below
    newURL = targetURL + "&pg={}"

    
    # Initial page
    current_page = 1

    # Applying recursion to scrape each page automatically
    while True:
        url = newURL.format(current_page)
        response = requests.get(url, timeout=10)
        content = BeautifulSoup(response.content, "html.parser")

        pageInfo = content.find("span", class_="v7list-pagination__page").text.strip()
        totalPages = int(pageInfo.split()[-1])

        listing_items = content.findAll('li', class_='v7list-results__item')

        for listing_item in listing_items:
            year = listing_item.find('span', class_='vehicle-heading__year').text.strip()
            model = listing_item.find('span', class_='vehicle-heading__model').text.strip()
            title = year + " " + model

            price = listing_item.find('span', class_="vehicle-price vehicle-price--current")
            price = price.find('span', class_='vehicle-price__price') if price else None

            cleaned_price_text = price.text.strip().replace('$', '').replace(',', '') if price else '0'
            price = float(cleaned_price_text)

            location = listing_item.find('div', class_='location')
            location = location.text.strip() if location else 'N/A'

            link_tag = listing_item.find('a', href=True)
            link = link_tag.get('href') if link_tag else 'N/A'
            link = homeURL + link

            # print(f"Title: {year, model}\nPrice: {price}\nLocation: {location}\nLink: {link}\n{'-' * 30}\n")

            # searchResults[searchNumber] = [price, year, model, location, link]
            searchResults[searchNumber] = [price, title, location, link]
            searchNumber += 1

        current_page += 1

        if current_page > totalPages:
            break

    return searchResults

