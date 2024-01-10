# Superpy: Supermarket inventory management

Superpy is a command-line interface (CLI) built for supermarkets to help manage their purchases, sales and inventory. It provides features to buy and sell products, check the inventory for expired products, produce reports on costs, revenue and profit for certain periods and more. It uses an internal date system that can be manually adjusted by the user.

## Features
- **Date management:** set and advance the internal date to simulate daily operations.
- **Inventory control:** add/remove products from the inventory by buying and selling.
- **Reports:** uses the rich module to generate reports within the CLI that show purchased/sold items, inventory and expired products.
- **Calculations:** the system is able to calculate the costs, revenue and profit for specified time periods.
- **Data storage:** all transactions are stored in CSV format for easy reference.

## Installation
- Make sure you have Python 3 installed.
- Clone or download this repository to your local machine.
- Navigate to the directory in the CLI and open the terminal.
- The first command you run will generate all necessary CSV files. 

## Commands
1. **Set current date:** $ python super.py set_today `YYYY-MM-DD`
> _Use the --today argument to set the current date to today._

2. **Get current date:** $ python super.py get_today
> _Fetches the current date set by the user._

3. **Advance date:** $ python super.py advance_time `days`
> _The `days` argument can also be a negative number to go back in time._

4. **Buy product:** $ python super.py buy --product_name `"name"` --buy_price `price` --count `100` --expiration_date `YYYY-MM-DD`
> _The system will purchase a product and add it to the inventory._
> _The --count option will default to 1 if you omit the argument._

5. **Sell product:** $ python super.py sell --product_name `"name"` --sell_price `price` --count `100`
> _The system will search for the product in the inventory, and sell if it's in stock._
> _The --count option will default to 1 if you omit the argument._

6. **Generate report:** $ python super.py report `"file_name"`
> _Will show a table in the CLI of a CSV file. Choose between: `"bought"`, `"sold"`, `"inventory"`, `"expired"`._

7. **Calculate costs:** $ python super.py costs `YYYY-MM-DD`
> _Will display the costs for a specified time period._
> _Can be used with the optional --today or --yesterday arguments._

8. **Calculate revenue:** $ python super.py revenue `YYYY-MM-DD`
> _Will display the revenue for a specified time period._
> _Can be used with the optional --today or --yesterday arguments._

9. **Calculate profit:** $ python super.py profit `YYYY-MM-DD`
> _Will display the profit for a specified time period._
> _Can be used with the optional --today or --yesterday arguments._

10. **Clear all CSV files:** $ python super.py clear_history
> _Deletes all CSV files. Run any command to generate new ones._

## Data storage
All transaction data is stored in CSV files located in the `data` directory. 

- `bought.csv`: contains details about bought products including id, name, buy date, buy price, count and expiration date.
- `sold.csv`: contains details about sold products including id, name, buy date, buy price, count, sell date and sell price.
- `inventory.csv`: contains details about the non-expired products.
- `expired.csv`: contains details about the expired products.

The program reads the details from these files to calculate costs, revenue and profit. 

## Author
Gizem Brasser