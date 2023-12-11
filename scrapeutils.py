from bs4 import BeautifulSoup
import requests


def getHomeURL(fullURL: str) -> str:
    partsURL = fullURL.split('/')
    homeURL = '/'.join(partsURL[:3])

    return homeURL

def getNextPageLinkKijiji(url: str):

    response = requests.get(url, timeout=5)
    content = BeautifulSoup(response.content, "html.parser")

    linkTarget = content.findAll('li', {'data-testid': 'pagination-next-link'})
    # print(f'linkTarget:{linkTarget}')

    # Check if there are no links on the page
    if not linkTarget:
        nextLink = 'N/A'
        return nextLink
    else:
        # Extract the link if it exists
        for eachLink in linkTarget:
            nextLinkGroup = eachLink.find('a', href=True)
            nextLink = nextLinkGroup.get('href') if nextLinkGroup else 'N/A'
            return nextLink

