import csv
import os
import sys
from datetime import datetime

# Add grandparent directory to sys.path to be able to import from 'core' folder.
grandparent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(grandparent_dir)

from core.constants import DATE_FORMAT, INVENTORY_FILE, SOLD_FILE
from services.dates import get_today

# Function that removes sold products from the inventory and writes them to the SOLD_FILE.
def sell_product(product_name, sell_price, count):
    sell_date = get_today()

    # Check the inventory if there's a matching product and if there's enough in stock.
    with open(INVENTORY_FILE, mode="r") as f:
        reader = csv.DictReader(f)
        # Convert the content of INVENTORY_FILE into a list of dictionaries.
        inventory = list(reader)

        # List comprehension to filter the inventory based on the product_name and expiration_date.   
        filtered_inventory = [
            item
            for item in inventory 
            if (
                item["product_name"] == product_name
                and datetime.strptime(item["expiration_date"], DATE_FORMAT). date() >= sell_date
            )
        ]

    # The filtered_inventory list should contain the found product(s) if it is in stock.
    if len(filtered_inventory) == 0:
        return f"No {product_name} found in stock."
    elif int(filtered_inventory[0]["count"]) < count:
        answer = input(f"Not enough {product_name} in stock. Do you want to sell the remaining {filtered_inventory[0]["count"]} items? (y/n): ")
        if answer.lower() == "y":
            count = int(filtered_inventory[0]["count"])
            sell_product(product_name, sell_price, count)
        else:
            return "Sale cancelled."
        
    # Assign the data to the right keys so it can be written to the correct headers in the CSV file.   
    for item in filtered_inventory:
        sold_data = {
            "sold_id": item["bought_id"],
            "product_name": item["product_name"],
            "buy_date": item["buy_date"],
            "buy_price": item["buy_price"],
            "count": count,
            "sell_date": sell_date,
            "sell_price": sell_price
        }

    # Append the SOLD_FILE with the sold product.
    with open(SOLD_FILE, mode="a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(sold_data.values())
    
                   
sell_product("orange", 0.9, 300)



