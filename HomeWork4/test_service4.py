import requests
import pytest

def test_check_status_code(url,status_code):
    response = requests.get(url)
    if str(status_code) == str(response.status_code):
        assert True
    else:
        assert False
