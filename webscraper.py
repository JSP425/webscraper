from bs4 import BeautifulSoup
import requests, xlsxwriter

jsonDest = 'C:/Users/jpark/Desktop/testFILE.json'
textDest=lts = 'C:/Users/jpark/Desktop/results.txt'

searchTerm = "wide%20glide"
# searchTerm = "fxdl"
url = f'https://vancouver.craigslist.org/search/mca?query={searchTerm}#search=1~gallery~0~0'





response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")

# print(content)
# print(response)

listing_items = content.findAll('li', class_='cl-static-search-result')


workbook = xlsxwriter.Workbook('C:/Users/jpark/Desktop/test.xlsx')
worksheet = workbook.add_worksheet(searchTerm)

bold = workbook.add_format({'bold': True})

# Widen
worksheet.set_column('D:D', 60)

# Text with formatting.
worksheet.write('B1', 'Price', bold)
worksheet.write('D1', 'Name', bold)
worksheet.write('F1', 'Location', bold)
worksheet.write('I1', 'Link', bold)

# Iterate through each <li> tag and extract relevant information
# counter = 1
# xlLineCounter = 0
cellRow = 2
for listing_item in listing_items:
    
    # Extract title
    title = listing_item.find('div', class_='title').text.strip()

    # Extract price
    price = listing_item.find('div', class_='price')
    price = price.text.strip() if price else 'N/A'

    # Extract location
    location = listing_item.find('div', class_='location')
    location = location.text.strip() if location else 'N/A'

    link_tag = listing_item.find('a', href=True)
    link = link_tag.get('href') if link_tag else 'N/A'

    # Print the extracted information
    # text_file.write(f"Title: {title}\nPrice: {price}\nLocation: {location}\nLink: {link}\n{'-' * 30}\n")

    # write into excel original format
    # worksheet.write(xlLineCounter, 0, title)
    # worksheet.write(xlLineCounter+1, 0, price)
    # worksheet.write(xlLineCounter+2, 0, location)
    # worksheet.write(xlLineCounter+3, 0, link)
    # worksheet.write(xlLineCounter+4, 0, "")

    # write into excel new format
    worksheet.write(f"B{cellRow}", price)
    worksheet.write(f"D{cellRow}", title)
    worksheet.write(f"F{cellRow}", location)
    worksheet.write(f"I{cellRow}", link)

    # counter +=1
    # xlLineCounter += 5
    cellRow += 1

worksheet.autofilter('B1:I1')



workbook.close()
# with open(jsonDest, 'w') as file:
#     json.dump('blahhh', file)

