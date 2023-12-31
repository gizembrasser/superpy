import argparse
from services.buy_product import buy_product

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"

# Superpy command-line tool arguments.
def main():
    parser = argparse.ArgumentParser(description="Superpy: a command-line tool for tracking a supermarket's inventory.")

    subparsers = parser.add_subparsers(dest="command", help="Choose a command.")
    
    # Subparsers for the 'buy' command.
    buy_parser = subparsers.add_parser("buy", help="Buy a product")
    buy_parser.add_argument("--product_name", help="Name of the product")
    buy_parser.add_argument("--buy_price", type=float, help="Price of the product")
    buy_parser.add_argument("--count", type=int, help="Quanity of product")
    buy_parser.add_argument("--expiration_date", help="Expiration date")

    args = parser.parse_args()

    if args.command == "buy":
        buy_product(args.product_name, args.buy_price, args.count, args.expiration_date)
    else:
        print(f"Unknown command: {args.command}")

if __name__ == "__main__":
    main()
