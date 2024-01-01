import os
import sys
import datetime

# Add grandparent directory to sys.path to be able to import from 'core' folder.
grandparent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(grandparent_dir)

from core.constants import TODAY_FILE

# Grabs the current day from the today.txt file.
def get_today():
    if not os.path.exists(TODAY_FILE):
        return datetime.date.today()
    
    with open(TODAY_FILE, "r") as f:
        today_str = f.read().strip()
        today_date = datetime.datetime.strptime(today_str, "%Y-%m-%d").date()
    return today_date