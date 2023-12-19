import pytest
from kijijiscraper import kj_search  

# Sample URL for testing
valid_url_with_results = "https://www.kijiji.ca/b-motorcycles/british-columbia/yamaha/k0c30l9007"
url_with_no_results = "https://www.kijiji.ca/b-motorcycles/british-columbia/blahblah/k0c30l9007"

def test_kj_search_no_results():
    results = kj_search(url_with_no_results)
    
    assert isinstance(results, dict)
    assert len(results) == 0
    

def test_kj_search_valid_url():
    results = kj_search(valid_url_with_results)
    
    assert isinstance(results, dict)
    assert len(results) > 0
    
    for key, value in results.items():
        assert isinstance(value, list), f"Value for key '{key}' is not a list: {value}"
        assert len(value) == 4, f"List for key '{key}' does not have exactly four elements: {value}"
        assert isinstance(value[0], (float, int, str)), f"Invalid type for price in key '{key}': {type(value[0])}"
        assert isinstance(value[1], str), f"Invalid type for title in key '{key}': {type(value[1])}"
        assert isinstance(value[2], str), f"Invalid type for location in key '{key}': {type(value[2])}"
        assert isinstance(value[3], str), f"Invalid type for link in key '{key}': {type(value[3])}"







