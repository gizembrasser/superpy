import argparse

def create_parser():
    parser = argparse.ArgumentParser(prog="python super.py", 
                                     description="Superpy: Supermarket inventory management", 
                                     epilog="Thanks for using Superpy!")
    
    subparsers = parser.add_subparsers(dest="command", title="commands", help="Choose a command")

    # Get current date command
    subparsers.add_parser("get_today", help="Get the current date")

    args = parser.parse_args()

    return args