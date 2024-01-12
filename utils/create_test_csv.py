import csv
import tempfile

def create_test_csv(test_data):
    # Create a temporary CSV file with test data.
    with tempfile.NamedTemporaryFile(mode="w", newline="", delete=False) as temp_csv:
       writer = csv.writer(temp_csv)
       writer.writerows(test_data)
       return temp_csv.name