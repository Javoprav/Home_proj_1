import unittest
import calc
from func import my_func

'''def test_my_func():
    assert my_func(4, 2) == 2

def test_my_func_ex():
    assert my_func(4, 0) == "Error"'''

class Test_my_func2(unittest.TestCase):
    def test_my_func1(self):
        self.assertEqual(my_func(8, 2), 4)
        self.assertIsNone(my_func(5, 0))