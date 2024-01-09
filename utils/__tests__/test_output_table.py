import os
import sys

grandparent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(grandparent_dir)

from output_table import output_table


def test_output_table(capsys):
    output_table("revenue")

    # Capture the output.
    captured = capsys.readouterr()
    actual_output = captured.out.strip() # Remove leading/trailing whitespaces.

    expected_output = '     Revenue table:     \n┏━━━━━━━━━━━━┳━━━━━━━━━┓\n┃   period   ┃ revenue ┃\n┡━━━━━━━━━━━━╇━━━━━━━━━┩\n│ 2024-01-01 │  79.2   │\n│ 2024-01-06 │  22.5   │\n│ 2024-01-07 │  75.0   │\n└────────────┴─────────┘'
    
    assert expected_output == actual_output
    assert "error" not in captured.err # Ensure no error messages are printed




