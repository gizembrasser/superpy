import os
import sys
import csv
from datetime import date

grandparent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(grandparent_dir)

from core.constants import DATA_DIR, DATE_FORMAT
from core.constants import TODAY_FILE, BOUGHT_FILE, SOLD_FILE, EXPIRED_FILE, INVENTORY_FILE
from core.constants import BOUGHT_HEADER, SOLD_HEADER, EXPIRED_HEADER, INVENTORY_HEADER


# Create directory for data files if it doesn't exist.
def create_data_files():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    # Create today.txt if it doesn't exist.
    if not os.path.exists(TODAY_FILE):
        with open(TODAY_FILE, "w") as f:
            # Write the current date into the file.
            today = date.today().strftime(DATE_FORMAT)
            f.write(today)
    
    # Create initial CSV files with headers if they don't exist in the data directory.
    if not os.path.exists(BOUGHT_FILE):      
        with open(BOUGHT_FILE, "w", newline="") as f:      
            writer = csv.writer(f)      
            writer.writerow(BOUGHT_HEADER)
    
    if not os.path.exists(SOLD_FILE):
        #'newline=""' means that no specific newline character (like \n) should be used.
        # By creating the file this way, every added row will be written on a new line automatically.
        with open(SOLD_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(SOLD_HEADER)
    
    if not os.path.exists(EXPIRED_FILE):
        with open(EXPIRED_FILE, "w", newline="") as f:
            # Create a writer object for the file 'f'.
            writer = csv.writer(f)
            writer.writerow(EXPIRED_HEADER)
    
    if not os.path.exists(INVENTORY_FILE):
        with open(INVENTORY_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            # Write the first row to the file, which contains the headers.
            writer.writerow(INVENTORY_HEADER)


# Function to delete all CSV files.
def clear_csv_files():
    if not os.path.exists(DATA_DIR):
        print(f"Directory '{DATA_DIR}' does not exist.")

    # Iterate through list of files in the directory.
    for file in os.listdir(DATA_DIR):
        file_path = os.path.join(DATA_DIR, file)

        # Check if it's a file and has a '.csv' extension.
        if os.path.isfile(file_path) and file.endswith(".csv"):
            # Delete the CSV file
            os.remove(file_path)
            
    print(f"Cleared of contents of all CSV files.")
    


