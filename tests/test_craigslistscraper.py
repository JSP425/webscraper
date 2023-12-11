from craigslistscraper import cl_search
import random
import pytest

testLocations=["vancouver", "abbotsford", "nanaimo"]
testLocation = testLocations[0]
print(testLocation)
testCategory = "cta"
testSearchTerm = "Toyota%20Prius"


def test_one_location():
    
    results = cl_search([testLocation], testCategory, testSearchTerm)

    assert isinstance(results, dict)
    assert len(results) > 0

    for key, value in results.items():
        assert isinstance(value, list), f"Value for key '{key}' is not a list: {value}"
        assert len(value) == 4, f"List for key '{key}' does not have exactly four elements: {value}"

def test_multiple_locations():
    
    results = cl_search(testLocations, testCategory, testSearchTerm)

    assert isinstance(results, dict)
    assert len(results) > 0

    for key, value in results.items():
        assert isinstance(value, list), f"Value for key '{key}' is not a list: {value}"
        assert len(value) == 4, f"List for key '{key}' does not have exactly four elements: {value}"

def test_cl_search_no_results():
    pass

    

