import csv
import os
import sys
from datetime import datetime


# Add grandparent directory to sys.path to be able to import from 'core' folder.
grandparent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(grandparent_dir)

from core.constants import DATE_FORMAT, BOUGHT_FILE, EXPIRED_FILE, EXPIRED_HEADER, INVENTORY_FILE, INVENTORY_HEADER
from dates import get_today

# The inventory is updated after each action performed in the CLI.
def update_inventory():
    print("Updating inventory...")
    today_date = get_today()
    expired = []
    inventory = []

    with open(BOUGHT_FILE, "r") as f:
        reader = csv.DictReader(f)
        
        # Checks each product's expiration date, adds to the 'expired' list if date has passed.
        # If the product is not expired it gets added to the 'inventory' list.
        for row in reader:
            expiration_date_str = row.get("expiration_date")
            expiration_date = datetime.strptime(expiration_date_str, DATE_FORMAT).date()

            if expiration_date < today_date:
                expired.append(row)
            else: 
                inventory.append(row)
    
    # Write the non-expired products to the inventory.csv file.
    with open(INVENTORY_FILE, "w", newline="") as f:
        print(f"Found {len(inventory)} products that are not expired and wrote them to the inventory.csv file")
        writer = csv.writer(f)
        writer.writerow(INVENTORY_HEADER)

        for product in inventory:
            writer.writerow(product.values())


    # Write the expired products to the expired.csv file.
    with open(EXPIRED_FILE, "w", newline="") as f:
        print(f"Found {len(expired)} products that are expired and moved them to the expired.csv file")
        writer = csv.writer(f)
        writer.writerow(EXPIRED_HEADER)

        for product in expired:
            writer.writerow(product.values())

update_inventory()
