import os
import sys
from datetime import datetime

grandparent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(grandparent_dir)

from core.constants import DATE_FORMAT

# Check if a string can be converted to a date object.
def convert_to_date(date_str):
    try:
        date = datetime.strptime(date_str, DATE_FORMAT).date()
        return date
    except ValueError:
        print("Invalid date format. Please use the format YYYY-MM-DD.")
