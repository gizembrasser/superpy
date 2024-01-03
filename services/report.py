import csv
from rich.console import Console
from rich.table import Table

# Use the rich library to display a CSV file in the terminal as a table.
def display_report(file_path):
    # Create a table.
    table = Table(title="CSV Data")

    custom_headers = ["Product Name", "Buy Date", "Buy Price", "Count", "Expiration Date"]

    for header in custom_headers:
        table.add_column(header, style="magenta", justify="center")

    # Read data from the CSV file.
    with open(file_path, "r", newline="") as f:
        reader = csv.reader(f)
        next(reader) # Skip the header row.
        
        for row in reader:
            # Exclude the first element (id column) from each row.
            # Unpacking operator * is used to pass each element as individual argument, instead of one list.
            table.add_row(*row[1:])
    
    console = Console()
    console.print(table)