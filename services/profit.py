import csv
import os
import sys
from datetime import datetime

grandparent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(grandparent_dir)

from core.constants import DATE_FORMAT, COSTS_FILE, REVENUE_FILE
from services.costs import calculate_costs
from services.revenue import calculate_revenue


# Calculates the profit based on the result of calculate_costs() and calculate_revenue() for a certain period.
def calculate_profit(period_str):
    try:
        period = datetime.strptime(period_str, DATE_FORMAT).date()
    except ValueError:
        print("Invalid date format. Please use the format YYYY-MM-DD.")
        return None
    
    total_costs = calculate_costs(period_str)
    total_revenue = calculate_revenue(period_str)
    
    if total_costs and not total_revenue:
        total_profit = {
            "period": period_str,
            "profit": f"-{total_costs['costs']}"
        }

        print(f"Total profit for {period}: ${total_profit['profit']}")
        return total_profit
    
    elif total_revenue and not total_costs:
        total_profit = {
            "period": period_str,
            "profit": f"{total_revenue['revenue']}"

        }
        
        print(f"Total profit for {period}: ${total_profit['profit']}")
        return total_profit
    
    elif total_costs and total_revenue:
        profit = float(total_costs['costs']) - float(total_revenue['revenue'])

        total_profit = {
            "period": period_str,
            "profit": profit
        }

        print(f"Total profit for {period}: ${profit}")
        return total_profit
    
    else:
        return None


calculate_profit("2024-01-06")