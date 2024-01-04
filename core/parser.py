import argparse

def create_parser():
    # Create instance of argparse.ArgumentParser to use the module's functionalities.
    parser = argparse.ArgumentParser(prog="python super.py", 
                                     description="Superpy: Supermarket inventory management", 
                                     epilog="Thanks for using Superpy!")

    # Add subparser to handle commands. 
    # 'dest="command"' means you can access the arguments with the .command attribute.
    subparsers = parser.add_subparsers(dest="command", title="commands", help="Choose a command")

    # Get_today command.
    subparsers.add_parser("get_today", help="Get the current date")

    # Set_today command alongside optional 'date' parameter and '--today' argument.
    parser_set_today = subparsers.add_parser("set_today", help="Set the current date")
    parser_set_today.add_argument("date", nargs="?", default=None, help="The date (YYYY-MM-DD) to set as today")
    parser_set_today.add_argument("--today", nargs="?", const=True, default=False, help="Set the current day as today")

    # Advance_time command alongside the 'days' parameter.
    parser_advance_time = subparsers.add_parser("--advance_time", help="Set the date forwards or backwards x days")
    parser_advance_time.add_argument("days", type=int, help="The humber of days to advance(can also be negative)")

    # Command to buy a product based on the arguments passed.
    parser_buy = subparsers.add_parser("buy", help="Buy a product or products")
    parser_buy.add_argument("--product_name", required=True, help="Name of the product")
    parser_buy.add_argument("--buy_price", type=float, required=True, help="Price of the product")
    parser_buy.add_argument("--count", type=int, default=1, help="Quantity of the product (default is 1)")
    parser_buy.add_argument("--expiration_date", required=True, help="Expiration date of the product (YYYY-MM-DD)")

    # Command to sell a product from the inventory.
    parser_sell = subparsers.add_parser("sell", help="Sell a product or products")
    parser_sell.add_argument("--product_name", required=True, help="Name of the product")
    parser_sell.add_argument("--sell_price", type=float, required=True, help="Sell price of the product")
    parser_sell.add_argument("--count", type=int, default=1, help="Quantity of the product (default is 1)")

    # Command to display CSV date in the terminal.
    parser_report = subparsers.add_parser("report", help="Display data from a specified CSV file")
    parser_report.add_argument("content_type", choices=["bought", "sold", "expired", "inventory"], help="Specify which CSV file to show as a table")

    # Command to clear all CSV files
    subparsers.add_parser("clear_history", help="Clear all CSV files")

    # Parse the command-line arguments and stores the result in a variable.
    # You'll be able to access its attributes by using args.command for example.
    args = parser.parse_args()

    return args