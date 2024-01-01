import datetime

from core.create_parser import create_parser
from services.create_data_files import create_data_files
from services.dates import get_today, set_today

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"

# Your code below this line.
def main():
    create_data_files()

    args = create_parser()

    # Check which command was given.
    # Call the corresponding function with the given arguments.
    if args.command == "set_today":
        if args.date:
            set_today(args.date)
            print(f"Today's date is now set to {args.date}.")
        if args.today:
            date_object = datetime.datetime.today()
            
            set_today(date_object.strftime("%Y-%m-%d"))
            print(f"Today's date has been automatically set to the current day.")

    elif args.command == "get_today":
        date = get_today()
        print(f"Today's date is {date}.")

if __name__ == "__main__":
    main()