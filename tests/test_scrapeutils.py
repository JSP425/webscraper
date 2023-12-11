import scrapeutils
from bs4 import BeautifulSoup
import requests

testURL = "https://www.kijiji.ca/b-motorcycles/british-columbia/honda/page-{}/k0c30l9007"

testFirstPageURL = testURL.format(1)
testLastPageURL = testURL.format(6)


def test_firstPage():
    result = scrapeutils.getNextPageLinkKijiji(testFirstPageURL)

    assert result != 'N/A', f"this should be the last page of search results. check webpage."

# this should fail. last page will not have a next page link
def test_lastPage():
    result = scrapeutils.getNextPageLinkKijiji(testLastPageURL)

    assert result != 'N/A', f"this should be the last page of search results. check webpage."

