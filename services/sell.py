import csv
import os
import sys
from datetime import datetime

# Add grandparent directory to sys.path to be able to import from 'core' folder.
grandparent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(grandparent_dir)

from core.constants import INVENTORY_FILE, INVENTORY_HEADER, SOLD_FILE
from services.dates import get_today
from utils.numbers import is_positive_number


# Function that removes sold products from the inventory and writes them to the SOLD_FILE.
def sell_product(product_name, sell_price, count):
    if not is_positive_number(sell_price, count):
        print("Please enter a positive number for --sell_price and --count.")
        return None
    
    sell_date = get_today()

    # Check the inventory if there's a matching product and if there's enough in stock.
    with open(INVENTORY_FILE, mode="r") as f:
        reader = csv.DictReader(f)
        # Convert the content of INVENTORY_FILE into a list of dictionaries.
        inventory = list(reader)

        # List comprehension to filter the inventory based on the product_name.
        filtered_inventory = [item for item in inventory if (item["product_name"] == product_name)]

    # The filtered_inventory list should contain a dictionary of the found product(s) if in stock.
    if len(filtered_inventory) == 0:
        print(f"No {product_name} found in stock.")
        return None
    elif int(filtered_inventory[0]["count"]) < count:
        print(f"Not enough {product_name} in stock. Maximum quantity: {filtered_inventory[0]["count"]}")
        return None
    
    # Remove the sold product dictionary from the inventory list.
    inventory.remove(filtered_inventory[0])
        
    if int(filtered_inventory[0]["count"]) == count:
        # Overwrite the INVENTORY_FILE to contain the new inventory, without the sold product(s).
        with open(INVENTORY_FILE, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=INVENTORY_HEADER)
            writer.writeheader()
            writer.writerows(inventory)
    else:
        # If the amount to be sold is less than the amount in stock, subtract them.
        filtered_inventory[0]["count"] = int(filtered_inventory[0]["count"]) - count
        # Extend the inventory with the updated count.
        inventory.extend(filtered_inventory)
        with open(INVENTORY_FILE, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=INVENTORY_HEADER)
            writer.writeheader()
            writer.writerows(inventory)
                 
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
    
                   
"""sell_product("orange", 0.8, 10)"""



