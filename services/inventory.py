import csv
import os
import sys

grandparent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(grandparent_dir)

from core.constants import EXPIRED_FILE, EXPIRED_HEADER, INVENTORY_FILE, INVENTORY_HEADER
from services.dates import get_today
from utils.convert_to_date import convert_to_date
"""from services.buy import buy_product"""


# Checks the expiration dates in the INVENTORY_FILE, adds them to EXPIRED_FILE if expired.
def update_inventory():
    print("Updating inventory...")
    today_date = get_today()
    expired = []
    inventory = []

    with open(INVENTORY_FILE, mode="r") as f:
        # Return each row of the CSV file as a dict, with the keys taken from the header row.
        reader = csv.DictReader(f)

        # Loop through the list of dictionaries.
        for row in reader:
            # Use .get() to retrieve the value of the 'expiration_date' key.
            expiration_date_str = row.get("expiration_date")
            # Convert expiration_date values to datetime object, to compare them with today_date.
            expiration_date = convert_to_date(expiration_date_str)

            if expiration_date < today_date:
                expired.append(row)
            else: 
                inventory.append(row)
    
    # Write the non-expired products (stored in inventory list) back to the INVENTORY_FILE.
    with open(INVENTORY_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(INVENTORY_HEADER)

        for product in inventory:
            writer.writerow(product.values())

    # Write the expired products to the expired.csv file.
    with open(EXPIRED_FILE, "w", newline="") as f:
        print(f"Found {len(expired)} expired products in the inventory and moved them to the expired.csv file.")
        writer = csv.writer(f)
        writer.writerow(EXPIRED_HEADER)

        for product in expired:
            writer.writerow(product.values())        


"""bought_product = buy_product("orange", 0.8, 200, "2024-01-06")"""


# Takes a purchased product (a dict from the BOUGHT_FILE) as argument, adds it to the inventory.
def add_to_inventory(bought_product):
    inventory = []

    # Check if there's already a product in stock with the same product_name, buy_price and expiration_date. 
    with open(INVENTORY_FILE, mode="r") as f:
        reader = csv.DictReader(f)
        inventory = list(reader)

        filtered_inventory = [
            item
            for item in inventory
            if (
                item["product_name"] == bought_product["product_name"]
                and float(item["buy_price"]) == bought_product["buy_price"]
                and item["expiration_date"] == bought_product["expiration_date"]
            )
        ]

    # If product is already in stock, it should've ended up in filtered_inventory list.
    if len(filtered_inventory) > 0:
        print(f"Product already in stock, added {bought_product["count"]} to existing stock.")
        inventory.remove(filtered_inventory[0])
        
        # Instead of adding the product as a new row in INVENTORY_FILE, append the existing product's count.
        filtered_inventory[0]["count"] = int(filtered_inventory[0]["count"]) + bought_product["count"]
        inventory.extend(filtered_inventory)

        # Overwrite the INVENTORY_FILE, but only change the 'count' column of the matching bought_product.
        with open(INVENTORY_FILE, mode="w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=INVENTORY_HEADER)
            writer.writeheader()
            writer.writerows(inventory)
    # If product isn't in stock, just add it as a new row in INVENTORY_FILE.
    else: 
        with open(INVENTORY_FILE, mode="a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(bought_product.values())
        

"""add_to_inventory(bought_product)"""