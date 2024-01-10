import csv
import os
import sys

grandparent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(grandparent_dir)

from core.constants import BOUGHT_FILE
from utils.convert_to_date import convert_to_date


# Function that filters rows of the BOUGHT_FILE based on a time period.
# For each of the filtered rows, read the 'count' and' buy_price' column and multiply them to get the cost.
def calculate_costs(period_str):
    if convert_to_date(period_str):
       period = convert_to_date(period_str)
    else: 
        return None
    
    costs = []

    with open(BOUGHT_FILE, mode="r") as f:
        reader = csv.DictReader(f)
        bought = list(reader)

        # List comprehension to filter the 'bought' list based on the time period passed as argument.
        filtered_bought = [
            item 
            for item in bought
            if (
            convert_to_date(item["buy_date"]) == period
            )
        ]
    
    if len(filtered_bought) == 0:
        print(f"No purchases made during this period: {period_str} ")
        return None
    else: 
        # Loop through filtered_bought list and get the values for 'count' and 'buy_price'.
        for bought_product in filtered_bought:
            count = bought_product.get("count")
            buy_price = bought_product.get("buy_price")
            # Multiply the count and buy_price for each product.
            cost_per_product = int(count) * float(buy_price)

            # Add the cost for each product to the 'costs' list.   
            costs.append(cost_per_product)
        
        total_cost = {
            "period": period_str,
            "costs": str(sum(costs))
        }

    print(f"Total costs for {total_cost['period']}: ${total_cost['costs']}")   
    return total_cost
        
    
"""calculate_costs("2024-01-07")"""

