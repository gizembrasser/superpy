import os
import sys

grandparent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(grandparent_dir)

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

    # If there were costs but no revenue, the profit will be negative and equal the costs.   
    if total_costs and not total_revenue:
        total_profit = {
            "period": period_str,
            "profit": f"-{total_costs['costs']}"
        }
    # If there was revenue and no costs, the profit will equal the revenue.
    elif total_revenue and not total_costs:
        total_profit = {
            "period": period_str,
            "profit": f"{total_revenue['revenue']}"

        }
    # If there were costs and revenue, the profit will equal revenue - costs.
    elif total_costs and total_revenue:
        profit = float(total_revenue['revenue']) - float(total_costs['costs'])

        total_profit = {
            "period": period_str,
            "profit": round(profit, 2)
        }   
    else:
        return None
    
    print(f"Total profit for {total_profit['period']}: ${total_profit['profit']}")


"""calculate_profit("2024-01-07")"""
