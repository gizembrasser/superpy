# Superpy: Supermarket inventory management

Superpy is a command-line interface (CLI) built for supermarkets to help manage their purchases, sales and inventory. It provides features to buy and sell products, check the inventory for expired products, produce reports on costs, revenue and profit for certain periods and more. It uses an internal date system that can be manually adjusted by the user.

# Features
- Date management: set and advance the internal date to simulate daily operations.
- Inventory control: add/remove products from the inventory by buying and selling.
- Reports: uses the rich module to generate reports within the CLI that show purchased/sold items, inventory and expired products.
- Calculations: the system is able to calculate the costs, revenue and profit for specified time periods.
- Data storage: all transactions are stored in CSV format for easy reference.

# Installation
- Make sure you have Python 3 installed.
- Clone or download this repository to your local machine.
- Navigate to the directory in the CLI.
- The first command you run will generate all necessary CSV files. 

# Commands
1. Set current date: $ python super.py set_today YYYY-MM-DD
- Use the --today argument to set the current date to today. 

2. Get current date: $ python super.py get_today
- Fetches the current date set by the user.

3. Advance date: $ python super.py advance_time < number_of_days >
- This can also be a negative number of days to go back in time.

4. Buy product: $ python super.py buy --product_name "Name" --buy_price < price > --count 100 --expiration_date YYYY-MM-DD
- The system will purchase a product and add it to the inventory.
- The < count > option will default to 1 if you omit the argument. 

5. Sell product: $ python super.py sell --product_name "Name" --sell_price < price > --count 100
- The system will search for the product in the inventory, and sell if it's in stock.
- The < count > option will default to 1 if you omit the argument. 

6. Generate report: $ python super.py report "file_name"
- Will show a table in the CLI of a CSV file. Choose between: "bought", "sold", "inventory", "expired".

7. Calculate costs: $ python super.py costs YYYY-MM-DD
- Will display the costs for a specified time period.
- Can be used with the optional --today or --yesterday arguments.

8. Calculate revenue: $ python super.py revenue YYYY-MM-DD
- Will display the revenue for a specified time period.
- Can be used with the optional --today or --yesterday arguments.

9. Calculate profit: $ python super.py profit YYYY-MM-DD
- Will display the profit for a specified time period.
- Can be used with the optional --today or --yesterday arguments.

10. Clear all CSV files: $ python super.py clear_history
- Deletes all CSV files. Run any command to generate new ones.