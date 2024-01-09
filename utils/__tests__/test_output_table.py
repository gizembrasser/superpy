import os
import sys
import csv
import tempfile

grandparent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(grandparent_dir)

from output_table import output_table


def create_test_csv(test_data):
    # Create a temporary CSV file with test data.
    with tempfile.NamedTemporaryFile(mode="w", newline="", delete=False) as temp_csv:
       writer = csv.writer(temp_csv)
       writer.writerows(test_data)
       return temp_csv.name


def test_output_table(capsys):
    # Define test data for the CSV file.
    test_data = [
        ["period", "revenue"],
        ["2024-01-05", 79.2],
        ["2024-01-06", 22.5],
        ["2024-01-07", 75.0]
    ]

    # Create a temporary CSV file with the test data, and the other arguments needed for output_table()
    test_data_file = create_test_csv(test_data)
    test_headers = ["period", "revenue"]
    test_content_type = "revenue"

    output_table(test_headers, test_data_file, test_content_type)

    # Capture the output.
    captured = capsys.readouterr()
    actual_output = captured.out.strip() # Remove leading/trailing whitespaces.

    expected_output = 'Revenue table:     \n┌────────────┬─────────┐\n│   period   │ revenue │\n├────────────┼─────────┤\n│ 2024-01-05 │  79.2   │\n│ 2024-01-06 │  22.5   │\n│ 2024-01-07 │  75.0   │\n└────────────┴─────────┘'
    
    assert expected_output == actual_output
    assert "error" not in captured.err # Ensure no error messages are printed