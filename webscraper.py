from bs4 import BeautifulSoup
import requests

# url = 'https://ethans_fake_twitter_site.surge.sh/?ref=hackernoon.com'
# url = 'https://classic.battle.net/diablo2exp/'
url = 'https://vancouver.craigslist.org/search/mca?query=wide%20glide#search=1~gallery~0~0'

response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")

# print(content)
# print(response)

# test = content.findAll('p', attrs = {"class":"content"}).text

paragraphs = content.findAll('div', class_='title')



for paragraph in paragraphs:
    print(paragraph.text)

