import pytest
from datetime import datetime

def get_time():
    time_string = datetime.now().strftime("%A %d %B %Y %H %M %S")
    return time_string.split()

def test_get_time_length():
    result = get_time()
    assert len(result) == 7

def test_get_time_contents():
    result = get_time()
    for element in result:
        assert isinstance(element, str)
        pytest.success("It worked")

