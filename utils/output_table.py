import os
import sys
from rich.table import Table
from rich.console import Console

grandparent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(grandparent_dir)

from core.constants import BOUGHT_HEADER, SOLD_HEADER,  EXPIRED_HEADER, INVENTORY_HEADER, COSTS_HEADER, REVENUE_HEADER, PROFIT_HEADER
from core.constants import BOUGHT_FILE, SOLD_FILE, EXPIRED_FILE, INVENTORY_FILE, COSTS_FILE, REVENUE_FILE, PROFIT_FILE


# Function that outputs a table to the CLI.
# Takes a name of a CSV file, and a time period to select data from as arguments.
def output_table(content_type, period=None):
    # Determine which CSV file to show based on content_type argument.
    if content_type == "inventory":
        headers = INVENTORY_HEADER
        data_file = INVENTORY_FILE    
    elif content_type == "bought":
        headers = BOUGHT_HEADER
        data_file = BOUGHT_FILE
    elif content_type == "sold":
        headers = SOLD_HEADER
        data_file = SOLD_FILE
    elif content_type == "costs":
        headers = COSTS_HEADER
        data_file = COSTS_FILE
    elif content_type == "expired":
        headers = EXPIRED_HEADER
        data_file = EXPIRED_FILE
    elif content_type == "revenue":
        headers = REVENUE_HEADER
        data_file = REVENUE_FILE            
    elif content_type == "profit":
        headers = PROFIT_HEADER
        data_file = PROFIT_FILE
    else:
        print("Invalid content type specified.")
        return None
    
    # Load data from CSV file.
    with open(data_file, mode="r") as f:
        next(f) # Skip the header row.
        # Create a list of the remaining rows.
        # Each row represents a nested list, with leading/trailing whitespace removed and split into a list using ',' as the delimiter.
        data = [line.strip().split(",") for line in f.readlines()]
        footer = None
        # If the 'data' list is empty, there's no content (excluding the header) in the CSV file.
        if len(data) > 1:
            # Checks if the first element of the last line of data is equal to the string 'Total'. 
            # This is a condition to identify if the last line is a footer.
            if data[-1][0] == "Total":
                # Remove the last line from the 'data' list if it's a footer.
                footer = data[-1]
                data = data[:1]

    # Create table object with a title and header_style.
    if period != None:
        title = f"\n {period.capitalize()} {content_type.capitalize()} table:"
    else:
        title = f"\n {content_type.capitalize()} table:"

    table = Table(title=title, show_header=True, header_style="bold magenta")

    for header in headers:
        table.add_column(header, justify="center")

    # Create a list of valid styles.
    colors = ["red", "blue", "green", "yellow", "magenta", "cyan", "white", "bright_red", "bright_green", "bright_yellow", "bright_blue", "bright_magenta", "bright_cyan", "bright_white"]
    # Create a dictionary to map each product to a valid style.
    color_dict = {}
    # Loop over the 'data' list.
    # Enumerate() is used to get both the index 'i' and the corresponding row from 'data'.
    for i, row in enumerate(data):
        product_id = row[0]
        # Add each product to color_dict if it's not already present.
        if product_id not in color_dict:
            # Color style is determined based on the index 'i' using the % operator.
            # This ensures that the colors repeat if there are more products than colors.
            color_dict[product_id] = colors[i % len(colors)]
        # Add new row to table. * is used to unpack the elements of the 'row' list.
        table.add_row(*row, style=color_dict[product_id])

    # If there's a footer, add an empty row and a row containing the unpacked elements of the 'footer' list.
    if footer:
        table.add_row("")
        table.add_row(*footer, style="bold magenta")  
    
    # Output table to CLI..
    console = Console()
    console.print(table)