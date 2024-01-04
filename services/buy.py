import csv
import os
import sys
from datetime import datetime
import uuid

# Add grandparent directory to sys.path to be able to import from 'core' folder.
grandparent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(grandparent_dir)

from core.constants import DATE_FORMAT, BOUGHT_FILE, BOUGHT_HEADER
from services.dates import get_today
from utils.numbers import is_positive_number


# Function that takes attributes of a product as arguments, adds the product to BOUGHT_FILE.
def buy_product(product_name, buy_price, count, expiration_date_str):
    if not is_positive_number(buy_price, count):
        print("Please enter a positive number for --buy_price and --count.")
        return None
    
    buy_date = get_today()
    # Convert expiration_date_str into datetime object.
    expiration_date = datetime.strptime(expiration_date_str, DATE_FORMAT)

    # Generate the data to insert into the CSV file.
    bought_data = {
        # Random id number generated by uuid.
        "id": uuid.uuid4(),
        "product_name": product_name,
        "buy_date": buy_date,
        "buy_price": buy_price,
        "count": count,
        "expiration_date": expiration_date.strftime(DATE_FORMAT)
    }

    # Appends the BOUGHT_FILE with the new bought product.
    with open(BOUGHT_FILE, mode="a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(bought_data.values())
        
    return bought_data
        

"""print(buy_product("pee", 1.4, 75, "2024-01-04"))"""