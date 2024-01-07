import csv
import os
import sys

grandparent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(grandparent_dir)

from core.constants import SOLD_FILE, REVENUE_FILE
from utils.convert_to_date import convert_to_date


# Function that filters rows of the SOLD_FILE based on a time period.
# For each of the filtered rows, read the 'count' and' sell_price' column and multiply them to get the revenue.
def calculate_revenue(period_str):
    if convert_to_date(period_str):
        period = convert_to_date(period_str)
    else:
        return None
    
    revenue = []

    with open(SOLD_FILE, mode="r") as f:
        reader = csv.DictReader(f)
        sold = list(reader)

        filtered_sold = [
            item 
            for item in sold
            if (
            convert_to_date(item["sell_date"]) == period
            )
        ]
    
    if len(filtered_sold) == 0:
        print(f"No sales made during this period: {period_str} ")
        return None
    else: 
        for sold_product in filtered_sold:
            count = sold_product.get("count")
            sell_price = sold_product.get("sell_price")
            revenue_per_product = int(count) * float(sell_price)

            revenue.append(revenue_per_product)
        
        total_revenue = {
            "period": period_str,
            "revenue": str(sum(revenue))
        }

    return total_revenue


"""total_revenue = calculate_revenue("2024-01-05")"""


# Add new row to REVENUE_FILE if data for that period hasn't been recorded yet.
def add_to_revenue(revenue_data):
    total_revenue = []

    with open(REVENUE_FILE, mode="r", newline="") as f:
        reader = csv.DictReader(f)
        total_revenue = list(reader)
    
    try:
        print(f"Total revenue for {revenue_data['period']}: ${revenue_data['revenue']}")

        if revenue_data not in total_revenue:
            total_revenue.append(revenue_data)

            with open(REVENUE_FILE, mode="a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(revenue_data.values())         
    except TypeError:
        return None


"""add_to_revenue(total_revenue)"""
