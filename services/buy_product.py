import csv
from csv import writer
from datetime import date, datetime
import uuid
import os

file_path = "data/bought.csv"

# Function used to buy a product by passing its name, price, quantity and expiration date as arguments.
# Inserts the data into the bought.csv file, which is a history of purchased products.
def buy_product(product_name, buy_price, count, expiration_date):
    buy_date = date.today()
    # Converts the expiration_date into a valid date object.
    date_object = datetime.strptime(expiration_date, "%Y-%m-%d")

    data = {
        "id": uuid.uuid4(),
        "product_name": product_name,
        "buy_date": buy_date,
        "buy_price": buy_price,
        "count": count,
        "expiration_date": date_object.strftime("%Y-%m-%d")
    }

    # Checks if the CSV file is empty.
    # If yes, write mode is used to add the fieldnames alongside the product's data.
    if os.path.getsize(file_path) == 0:
        with open(file_path, mode="w", newline="") as file:
            fieldnames = ["id", "product_name", "buy_date", "buy_price", "count", "expiration_date"]
            writer_object = csv.DictWriter(file, fieldnames=fieldnames)

            writer_object.writeheader()

            return writer_object.writerow(data)
    # If the CSV is not empty, the fieldnames don't need to be added again.
    # The product's data will get added with append mode.
    else:
        with open(file_path, mode="a", newline="") as file:
            writer_object = writer(file)

            return writer_object.writerow(data.values())

"""buy_product("milk", 2, 100, "2024-01-10")"""





        
