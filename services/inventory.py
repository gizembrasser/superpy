import csv
import os
import sys
from datetime import datetime

# Add grandparent directory to sys.path to be able to import from 'core' folder.
grandparent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(grandparent_dir)

from core.constants import DATE_FORMAT, BOUGHT_FILE, EXPIRED_FILE, EXPIRED_HEADER, INVENTORY_FILE, INVENTORY_HEADER
from services.dates import get_today


# The inventory is updated after each action performed in the CLI.
# Check the expiration dates in the BOUGHT_FILE, add them to the EXPIRED_FILE or INVENTORY_FILE.
def update_inventory():
    print("Updating inventory...")
    today_date = get_today()
    expired = []
    inventory = []

    with open(BOUGHT_FILE, "r") as f:
        # Return each row of the CSV file as a dict, with the keys taken from the header row.
        reader = csv.DictReader(f)
        
        # Loop through the list of dictionaries.
        for row in reader:
            # Use .get() to retrieve the value of the 'expiration_date' key.
            expiration_date_str = row.get("expiration_date")
            # Convert expiration_date values to datetime object, to compare them with today_date.
            expiration_date = datetime.strptime(expiration_date_str, DATE_FORMAT).date()

            if expiration_date < today_date:
                expired.append(row)
            else: 
                inventory.append(row)
    
    # Write the non-expired products (stored in inventory list) to the inventory.csv file.
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
