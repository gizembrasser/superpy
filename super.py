import datetime

from core.constants import DATE_FORMAT, BOUGHT_FILE, EXPIRED_FILE, INVENTORY_FILE
from core.parser import create_parser
from services.files import create_data_files, clear_csv_files
from services.dates import get_today, set_today, advance_time
from services.inventory import update_inventory, add_to_inventory
from services.buy import buy_product
from services.sell import sell_product
from utils.output_table import output_table

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"

# Your code below this line.
def main():
    create_data_files()

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
            date_object = datetime.datetime.today()
            
            set_today(date_object.strftime(DATE_FORMAT))
            print(f"Today's date has been automatically set to the current day.")
        update_inventory()

    # get_today function is called when this command is given.
    elif args.command == "get_today":
        date = get_today()
        print(f"Today's date is {date}.")

    elif args.command == "advance_time":
        print(f"Advancing time with {args.days} days...")
        advance_time(args.days)
        update_inventory()
    
    elif args.command == "buy":
        bought_product = buy_product(args.product_name, args.buy_price, args.count, args.expiration_date)
        if bought_product:
            add_to_inventory(bought_product)
        update_inventory()

    elif args.command == "sell":
        # Update inventory before function call, to prevent selling expired products.
        update_inventory()
        sell_product(args.product_name, args.sell_price, args.count)
        
    elif args.command == "report":
        output_table(args.content_type)

    elif args.command == "clear_history":
        clear_csv_files()
        print("Cleared all CSV files. Run any command to generate new ones.")


if __name__ == "__main__":
    main()