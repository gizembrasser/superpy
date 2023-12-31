# Goals
- Build a command-line tool called Superpy that a supermarket will use to keep track of its inventory.
- The core functionality is about keeping track and producing reports on various kinds of data.

# Data
- Which products the supermarket offers.
- How many of each type of product the supermarket holds currently.
- How much each product was bought for, and what its expiry date is.
- How much each product was sold for or if it expired, the fact that it did.

# CSV file structure
- All data must be saved in CSV files. 
- bought.csv columns: id, product_name, buy_date, buy_price, count, expiration_date
- sold.csv columns: id, bought_id, sell_date, sell_price, count

# Modules from standard library
- csv: CSV File Reading and Writing
- argparse: parser for command-line options, arguments and subcommands. Helps with writing the command-line tool.
- datetime: basic date and time types. Includes the date object, strftime and strptime functions, and datetime arithmetic using timedelta.

# Requirements
- The program should have an internal conception of what day it is, saved to a text file, so you can advance time by two days by using a command like < python super.py --advance-time 2 >.
- Well-structured and documented code: clear and effective variable/function names, use of comments, clear and effective separation of code into separate functions and possibly files.
- Use of external text files (CSV) to read and write data.
- Well-structured and user-friendly CLI with clear descriptions of each argument in the --help section.
- Text file containing a usage guide that includes plenty of examples.
- Include a 300-word report that highlights 3 notable technical elements of the app. Explain what problems they solve and why I chose to implement them this way. 

# Functionalities
- Setting and advancing the date that the app perceives as 'today'.
- Recording the buying and selling of products on certain dates.
- Reporting revenue and profit over specified time periods.
- Exporting selections of data to CSV files.
- Optional: using the Rich module, the ability to visualize some statistics using Matplotlib.
