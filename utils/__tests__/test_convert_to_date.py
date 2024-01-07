import os
import sys
from datetime import date

grandparent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(grandparent_dir)

from convert_to_date import convert_to_date

def test_convert_to_date_success():
    assert convert_to_date("2024-01-04") == date(2024, 1, 4)

def test_convert_to_date_failure():
    assert convert_to_date("abc") == None

