import csv
import os
import sys

grandparent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(grandparent_dir)

from core.constants import INVENTORY_FILE, INVENTORY_HEADER, SOLD_FILE
from services.dates import get_today
from utils.is_positive_number import is_positive_number


# Function that checks if a product is in stock, and how much.
def check_stock(product_name, count):
    if not is_positive_number(count):
        print("Please enter a positive number for --count.")
        return None
    
    # Check the inventory.
    with open(INVENTORY_FILE, mode="r") as f:
        reader = csv.DictReader(f)
        # Convert the content of INVENTORY_FILE into a list of dictionaries.
        inventory = list(reader)

        filtered_inventory = [item for item in inventory if (item["product_name"] == product_name)]

    # The filtered_inventory list should contain a dictionary of the found product if in stock.
    if len(filtered_inventory) == 0:
        print(f"No {product_name} found in stock.")
        return None
    elif int(filtered_inventory[0]["count"]) < count:
        print(f"Not enough {product_name} in stock. Maximum quantity: {filtered_inventory[0]["count"]}")
        return None
    else:
        return inventory, filtered_inventory


"""inventory, inventory_product = check_stock("orange", 1)"""


# Function that removes sold products from the inventory and writes them to the SOLD_FILE.
def sell_product(inventory, inventory_product, sell_price, count):
    inventory.remove(inventory_product[0])

    # If amount to be sold is equal to amount in stock, remove sold product from the INVENTORY_FILE.  
    if int(inventory_product[0]["count"]) == count:
        # Overwrite the INVENTORY_FILE to contain the new inventory, without the sold product.
        with open(INVENTORY_FILE, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=INVENTORY_HEADER)
            writer.writeheader()
            writer.writerows(inventory)
    else:
        # If the amount to be sold is less than the amount in stock, subtract them.
        inventory_product[0]["count"] = int(inventory_product[0]["count"]) - count
        # Extend the inventory with the updated count.
        inventory.extend(inventory_product)
        with open(INVENTORY_FILE, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=INVENTORY_HEADER)
            writer.writeheader()
            writer.writerows(inventory)
                 
    # Assign the data to the right keys so it can be written to the correct headers in the SOLD_FILE.  
    for item in inventory_product:
        sold_data = {
            "sold_id": item["bought_id"],
            "product_name": item["product_name"],
            "buy_date": item["buy_date"],
            "buy_price": item["buy_price"],
            "count": count,
            "sell_date": get_today(),
            "sell_price": sell_price
        }

    with open(SOLD_FILE, mode="a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(sold_data.values())


"""sell_product(inventory, inventory_product, 0.8, 1)"""