import os
import sys
import datetime

# Add grandparent directory to sys.path to be able to import from 'core' folder.
grandparent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(grandparent_dir)

from core.constants import TODAY_FILE

# Grabs the current day from the today.txt file.
def get_today():
    try: 
        with open(TODAY_FILE, "r") as f:
            today_str = f.read().strip()
            today_date = datetime.datetime.strptime(today_str, "%Y-%m-%d").date()
        return today_date
    
    except FileNotFoundError:
        return datetime.date.today()
    
# Manually set a date for today.
def set_today(date):
    date_object = datetime.datetime.strptime(date, "%Y-%m-%d")
    
    with open(TODAY_FILE, "w") as f:
        f.write(date_object.strftime("%Y-%m-%d"))
    get_today()

