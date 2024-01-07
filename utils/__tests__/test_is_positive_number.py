import os
import sys

grandparent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(grandparent_dir)

from is_positive_number import is_positive_number

def test_is_positive_number_two_args():
    assert is_positive_number(3.5, 4) == True

def test_is_positive_number_one_arg():
    assert is_positive_number(4) == True

def test_is_positive_number_failure():
    assert is_positive_number(-4, 2) == False