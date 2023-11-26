from bs4 import BeautifulSoup
import requests, xlsxwriter

jsonDest = 'C:/Users/jpark/Desktop/testFILE.json'
textDest=lts = 'C:/Users/jpark/Desktop/results.txt'

searchTerm = "wide%20glide"
url = f'https://vancouver.craigslist.org/search/mca?query={searchTerm}#search=1~gallery~0~0'





response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")

# print(content)
# print(response)

# test = content.findAll('p', attrs = {"class":"content"}).text

# paragraphs = content.findAll('div', class_='title')
listing_items = content.findAll('li', class_='cl-static-search-result')



# for paragraph in paragraphs:
#     print(paragraph.text)

with open(textDest,'w') as text_file:

# Iterate through each <li> tag and extract relevant information
    counter = 1
    for listing_item in listing_items:
        text_file.write(f'# {counter}\n')
        


        # Extract title
        title = listing_item.find('div', class_='title').text.strip()

        # Extract price
        price = listing_item.find('div', class_='price')
        price = price.text.strip() if price else 'N/A'

        # Extract location
        location = listing_item.find('div', class_='location')
        location = location.text.strip() if location else 'N/A'

        # Extract link
        # link = listing_item.find('a tabindex','href').text.strip()
        # link_tag = listing_item.find('a', attrs={'tabindex': '0'})
        # link = link_tag.get('href') if link_tag else 'N/A'


        link_tag = listing_item.find('a', href=True)
        # link_tag = listing_item.find('a')
        # link = link_tag.text.strip() if link_tag else 'N/A'\

        # link=print(link_tag)
        link = link_tag.get('href') if link_tag else 'N/A'





        # Print the extracted information
        text_file.write(f"Title: {title}\nPrice: {price}\nLocation: {location}\nLink: {link}\n{'-' * 30}\n")

        counter +=1

# with open(jsonDest, 'w') as file:
#     json.dump('blahhh', file)

