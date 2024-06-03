from functools import reduce
from main import process_numbers
from main import process_numbers_short

def test_process_numbers():
    assert (process_numbers([1, 2, 3, 4, 5, -2, -4]) == 55)

def test_process_numbers_short():
    assert (process_numbers_short([1, 2, 3, 4, 5, -2, -4]) == 55)