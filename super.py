from datetime import datetime, timedelta

from core.constants import DATE_FORMAT
from core.parser import create_parser
from services.files import create_data_files, clear_csv_files
from services.dates import get_today, set_today, advance_time
from services.inventory import update_inventory, add_to_inventory
from services.buy import buy_product
from services.sell import check_stock, sell_product
from services.costs import calculate_costs, add_to_costs
from services.revenue import calculate_revenue, add_to_revenue
from utils.output_table import output_table

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"

# Your code below this line.
def main():
    create_data_files()
    today = get_today()
    yesterday = today - timedelta(days=1)

    # create_parser() returns an object containing parsed command-line arguments.
    args = create_parser()

    # Check which command was given using the 'command' attribute of args.
    if args.command == "set_today":
        # Check if any optional arguments ('date' or 'today') were provided alongside the command.
        if args.date:
            # If a valid date was provided set_today is called to change the date.
            if set_today(args.date):
                print(f"Today's date is now set to {args.date}.")
        if args.today:
            date_object = datetime.today()
            
            set_today(date_object.strftime(DATE_FORMAT))
            print(f"Today's date has been automatically set to the current day.")
        update_inventory()

    elif args.command == "get_today":
        print(f"Today's date is {today}.")

    elif args.command == "advance_time":
        print(f"Advancing time with {args.days} days...")
        advance_time(args.days)
        update_inventory()
    
    elif args.command == "buy":
        bought_product = buy_product(args.product_name, args.buy_price, args.count, args.expiration_date)
        # If buy_product() returned a valid product dictionary, add it to inventory.
        if bought_product:
            add_to_inventory(bought_product)
        update_inventory()

    elif args.command == "sell":
        # Update inventory before function call, to prevent selling expired products.
        update_inventory()
        # Check if product is in stock before calling sell_product().
        if check_stock(args.product_name, args.count):
            inventory, inventory_product = check_stock(args.product_name, args.count)
            sell_product(inventory, inventory_product, args.sell_price, args.count)
        
    elif args.command == "report":
        output_table(args.content_type)
    
    elif args.command == "costs":
        if args.date:
            add_to_costs(calculate_costs(args.date))
        if args.today:
            add_to_costs(calculate_costs(today.strftime(DATE_FORMAT)))
        if args.yesterday:
            add_to_costs(calculate_costs(yesterday.strftime(DATE_FORMAT)))

    elif args.command == "revenue":
        if args.date:
            add_to_revenue(calculate_revenue(args.date))
        if args.today:
            add_to_revenue(calculate_revenue(today.strftime(DATE_FORMAT)))
        if args.yesterday:
            add_to_revenue(calculate_revenue(yesterday.strftime(DATE_FORMAT)))
            
    elif args.command == "clear_history":
        clear_csv_files()
        print("Cleared all CSV files. Run any command to generate new ones.")


if __name__ == "__main__":
    main()