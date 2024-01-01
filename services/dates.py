import os
import sys
from datetime import datetime, date, timedelta

# Add grandparent directory to sys.path to be able to import from 'core' folder.
grandparent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(grandparent_dir)

from core.constants import DATE_FORMAT, TODAY_FILE

# Grabs the current day from the today.txt file.
def get_today():
    try: 
        with open(TODAY_FILE, "r") as f:
            today_str = f.read().strip()
            today_date = datetime.strptime(today_str, DATE_FORMAT).date()
        return today_date 
    
    except FileNotFoundError:
        return date.today()
    
# Manually set a date for today.
def set_today(date):
    date_object = datetime.strptime(date, DATE_FORMAT)
    
    with open(TODAY_FILE, "w") as f:
        f.write(date_object.strftime(DATE_FORMAT))

def advance_time(days):
    today = get_today()
    new_date = today + timedelta(days=days)

    set_today(new_date.strftime(DATE_FORMAT))
