import csv
import os
import sys

grandparent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(grandparent_dir)

from core.constants import PROFIT_FILE
from services.costs import calculate_costs
from services.revenue import calculate_revenue
from utils.convert_to_date import convert_to_date


# Calculates the profit based on the result of calculate_costs() and calculate_revenue() for a certain period.
def calculate_profit(period_str):
    if convert_to_date(period_str):
        total_costs = calculate_costs(period_str)
        total_revenue = calculate_revenue(period_str)
    else: 
        return None
    
    if total_costs and not total_revenue:
        total_profit = {
            "period": period_str,
            "profit": f"-{total_costs['costs']}"
        }

        return total_profit
    
    elif total_revenue and not total_costs:
        total_profit = {
            "period": period_str,
            "profit": f"{total_revenue['revenue']}"

        }
        
        return total_profit
    
    elif total_costs and total_revenue:
        profit = float(total_revenue['revenue']) - float(total_costs['costs'])

        total_profit = {
            "period": period_str,
            "profit": str(profit)
        }

        return total_profit
    
    else:
        return None


"""total_profit = calculate_profit("2024-01-05")"""


def add_to_profit(profit_data):
    total_profit = []

    with open(PROFIT_FILE, mode="r", newline="") as f:
        reader = csv.DictReader(f)
        total_profit = list(reader)
    
    try:
        print(f"Total profit for {profit_data['period']}: ${profit_data['profit']}")

        if profit_data not in total_profit:
            total_profit.append(profit_data)

            with open(PROFIT_FILE, mode="a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(profit_data.values())         
    except TypeError:
        return None


"""add_to_profit(total_profit)"""