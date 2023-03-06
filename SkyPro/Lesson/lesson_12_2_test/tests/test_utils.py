import pytest
#from lesson_12_2_test.utils import abs
from utils import count_truth

@pytest.fixture
def coll():
    return ['a', 'a', 'a', 1, 2, 3, True, [], {1: 'a'}, False, (1, 2)]

def test_count_truth_str(coll):
    assert count_truth(coll, str) == 3

def test_count_truth_int(coll):
    assert count_truth(coll, int) == 3

def test_count_truth_list(coll):
    assert count_truth(coll, list) == 1

'''def test_abs_positive():
    assert abs(2) == 2

def test_abs_negative():
    assert abs(-2) == 2

def test_abs_zero():
    assert abs(0) == 0'''