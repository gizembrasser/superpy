import csv
import os
import sys
from datetime import datetime

# Add grandparent directory to sys.path to be able to import from 'core' folder.
grandparent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(grandparent_dir)

from services.dates import set_today
from services.inventory import update_inventory
from utils.output_table import output_table
from core.constants import REVENUE_FILE, SOLD_FILE, PROFIT_FILE
from core.constants import REVENUE_HEADER, PROFIT_HEADER