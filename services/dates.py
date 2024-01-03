import os
import sys
from datetime import datetime, date, timedelta

# Add grandparent directory to sys.path to be able to import from 'core' folder.
grandparent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(grandparent_dir)

from core.constants import DATE_FORMAT, TODAY_FILE


# Grabs the current day from the TODAY_FILE file.
def get_today():
    try: 
        with open(TODAY_FILE, "r") as f:
            # Read the file, strip any whitespaces so you'll end up with the date string.
            today_str = f.read().strip()
            today_date = datetime.strptime(today_str, DATE_FORMAT).date()
        # Return today's date as a datetime object.
        return today_date 
        
    except FileNotFoundError:
        return date.today()


# Manually set a date for today.
def set_today(date):
    # Try to convert argument passed into a datetime object to see if it's a valid date.
    try:
        date_object = datetime.strptime(date, DATE_FORMAT)
    
        with open(TODAY_FILE, "w") as f:
            f.write(date_object.strftime(DATE_FORMAT))
    except ValueError: 
        print("Invalid date format. Please use the format YYYY-MM-DD.")
        # Return 0 if argument passed is invalid due to ValueError.
        return 0


# Function to advance time based on the date in TODAY_FILE file.
def advance_time(days):
    today = get_today()
    # Add/subtract the amount of days passed as argument from the current date.
    new_date = today + timedelta(days=days)
    
    # Use set_today to write the new advanced date into the TODAY_FILE.
    set_today(new_date.strftime(DATE_FORMAT))
