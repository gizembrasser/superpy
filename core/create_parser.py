import argparse

def create_parser():
    parser = argparse.ArgumentParser(prog="python super.py", 
                                     description="Superpy: Supermarket inventory management", 
                                     epilog="Thanks for using Superpy!")
    
    subparsers = parser.add_subparsers(dest="command", title="commands", help="Choose a command")

    # Get current date command.
    subparsers.add_parser("get_today", help="Get the current date")

    # Set today command. 
    parser_set_today = subparsers.add_parser("set_today", help="Set the current date")
    parser_set_today.add_argument("date", nargs="?", default=None, help="The date (YYYY-MM-DD) to set as today")
    parser_set_today.add_argument("--today", nargs="?", const=True, default=False, help="Set the current day as today")
    
    args = parser.parse_args()

    return args