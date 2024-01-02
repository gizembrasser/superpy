import argparse

def create_parser():
    # Create instance of argparse.ArgumentParser to use the module's functionalities.
    parser = argparse.ArgumentParser(prog="python super.py", 
                                     description="Superpy: Supermarket inventory management", 
                                     epilog="Thanks for using Superpy!")

    # Add subparser to handle commands. 
    # 'dest="command"' means you can access the arguments with the .command attribute.
    subparsers = parser.add_subparsers(dest="command", title="commands", help="Choose a command")

    # Get current date command.
    subparsers.add_parser("get_today", help="Get the current date")

    # Set today command alongside optional arguments.
    parser_set_today = subparsers.add_parser("set_today", help="Set the current date")
    parser_set_today.add_argument("date", nargs="?", default=None, help="The date (YYYY-MM-DD) to set as today")
    parser_set_today.add_argument("--today", nargs="?", const=True, default=False, help="Set the current day as today")

    parser_advance_time = subparsers.add_parser("advance_time", help="Set the date forwards or backwards x days")
    parser_advance_time.add_argument("days", type=int, help="The humber of days to advance(can also be negative)")

    # Parse the command-line arguments and stores the result in a variable.
    # You'll be able to access its attributes by using args.command for example.
    args = parser.parse_args()

    return args