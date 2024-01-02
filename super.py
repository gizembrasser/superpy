import datetime

from core.constants import DATE_FORMAT
from core.parser import create_parser
from services.create_data_files import create_data_files
from services.dates import get_today, set_today, advance_time
from services.update_inventory import update_inventory

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"

# Your code below this line.
def main():
    create_data_files()

    args = create_parser()

    # Check which command was given.
    # Call the corresponding function with the given arguments.

    # Set_today function is added to the parser.
    if args.command == "set_today":
        if args.date:
            set_today(args.date)
        if args.today:
            date_object = datetime.datetime.today()
            
            set_today(date_object.strftime(DATE_FORMAT))
            print(f"Today's date has been automatically set to the current day.")
            # After every command the inventory gets updated.
            update_inventory()

    # Get_today function is added to the parser.
    elif args.command == "get_today":
        date = get_today()
        print(f"Today's date is {date}.")
        update_inventory()

    # Advance_time function is added to the parser.
    elif args.command == "advance_time":
        print(f"Advancing time with {args.days} days...")
        advance_time(args.days)
        update_inventory()

if __name__ == "__main__":
    main()