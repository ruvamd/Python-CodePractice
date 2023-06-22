import pytest
from typing import Tuple, List
from asmt5 import RodLengthCalculator

@pytest.fixture
def rod_length():
    return 8

@pytest.fixture
def price_array():
    return [0, 1, 6, 2, 4, 3, 3, 2, 8]

def test_find_max_value_top_down_memoization(rod_length, price_array):
    r = RodLengthCalculator(rod_length, price_array)
    max_value, sizes = r.find_max_value_top_down_memoization()
    print("Actual max value:", max_value)
    print("Actual sizes:", sizes)
    assert max_value == 22
    assert sizes == [2, 6]

def test_find_max_value_bottom_up(rod_length, price_array):
    r = RodLengthCalculator(rod_length, price_array)
    max_value, sizes = r.find_max_value_bottom_up()
    assert max_value == 22
    assert sizes == [2, 6]
