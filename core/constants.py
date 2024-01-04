import os

# Declare the path to the data directory.
DATA_DIR = os.path.join(os.getcwd(), "data")

# Declare the date format.
DATE_FORMAT = "%Y-%m-%d"

# Declare the path to the data CSV files.
TODAY_FILE = os.path.join(DATA_DIR, "today.txt")
BOUGHT_FILE = os.path.join(DATA_DIR, "bought.csv")
SOLD_FILE = os.path.join(DATA_DIR, "sold.csv")
EXPIRED_FILE = os.path.join(DATA_DIR, "expired.csv")
INVENTORY_FILE = os.path.join(DATA_DIR, "inventory.csv")
COSTS_FILE = os.path.join(DATA_DIR, "costs.csv")
REVENUE_FILE = os.path.join(DATA_DIR, "revenue.csv")
PROFIT_FILE = os.path.join(DATA_DIR, "profit.csv")

# Declare the headers for the CSV files.
BOUGHT_HEADER = ["id", "product_name", "buy_date", "buy_price", "count", "expiration_date"]
SOLD_HEADER = ["sold_id", "product_name", "buy_date", "buy_price", "count", "sell_date", "sell_price"]
EXPIRED_HEADER = ["bought_id", "product_name", "buy_date", "buy_price", "count", "expiration_date"]
INVENTORY_HEADER = ["bought_id", "product_name", "buy_date", "buy_price", "count", "expiration_date"]
COSTS_HEADER = ["period", "total_count", "total_costs"]
REVENUE_HEADER = ["period", "revenue"]
PROFIT_HEADER = ["period", "profit"]