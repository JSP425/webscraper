from bs4 import BeautifulSoup
import requests
import xlsxwriter
import subprocess # this is for opening the file automatically after


jsonDest = 'C:/Users/jpark/Desktop/testFILE.json'
fileDest ="C:/Users/jpark/Desktop/test.xlsx"

# searchTerm = "wide%20glide"
searchTerm = "harley"
url = f'https://vancouver.craigslist.org/search/mca?query={searchTerm}#search=1~gallery~0~0'


response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")

# print(content)
# print(response)

listing_items = content.findAll('li', class_='cl-static-search-result')


workbook = xlsxwriter.Workbook(fileDest)
worksheet = workbook.add_worksheet(searchTerm)

bold = workbook.add_format({'bold': True})
currency_format = workbook.add_format({'num_format': '$#,##0.00'})
worksheet.set_column('B:B', None, currency_format)

# Widen
# changing column width changes formatting from currency to custom
# worksheet.set_column('B:B', 10)

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


subprocess.Popen(['start', 'excel', fileDest], shell=True)

# with open(jsonDest, 'w') as file:
#     json.dump('blahhh', file)

