# This file is used to schedule the charging of stand fees to the first of every month
# we didn't include it in the main program because it requires a new module to run 
# and would ony work on the first of the month anyway

# Author: Robot Group 3

# Date: 2024-Aug-01

import schedule
import time
from datetime import datetime
from UpdateStandFee import charge_stand_fees

def is_first_of_month():
    return datetime.now().day == 1

schedule.every().day.at("00:00").do(charge_stand_fees)

while True:
    schedule.run_pending()
    if is_first_of_month():
        charge_stand_fees()
    time.sleep(86400)  # Sleep for a day