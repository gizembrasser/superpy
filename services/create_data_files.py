import os
import sys
import csv
import datetime

# Add grandparent directory to sys.path to be able to import from 'core' folder.
grandparent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(grandparent_dir)

from core.constants import DATA_DIR
from core.constants import TODAY_FILE, BOUGHT_FILE, SOLD_FILE, EXPIRED_FILE, INVENTORY_FILE, COSTS_FILE, REVENUE_FILE, PROFIT_FILE
from core.constants import BOUGHT_HEADER, SOLD_HEADER, EXPIRED_HEADER, INVENTORY_HEADER, COSTS_HEADER, REVENUE_HEADER, PROFIT_HEADER

# Create data files if they don't exist.
def create_data_files():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    # Create today.txt if it doesn't exist.
    if not os.path.exists(TODAY_FILE):
        with open(TODAY_FILE, "w") as f:
            today = datetime.date.today().strftime("%Y-%m-%d")
            f.write(today)
    
    # Create initial CSV files with headers if they don't exist.
    if not os.path.exists(BOUGHT_FILE):
        with open(BOUGHT_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(BOUGHT_HEADER)
    
    if not os.path.exists(SOLD_FILE):
        with open(SOLD_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(SOLD_HEADER)
    
    if not os.path.exists(EXPIRED_FILE):
        with open(EXPIRED_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(EXPIRED_HEADER)
    
    if not os.path.exists(INVENTORY_FILE):
        with open(INVENTORY_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(INVENTORY_HEADER)

    if not os.path.exists(REVENUE_FILE):
        with open(REVENUE_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(REVENUE_HEADER)

    if not os.path.exists(PROFIT_FILE):
        with open(PROFIT_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(PROFIT_HEADER)

    


