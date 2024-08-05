# utility_module.py

# Description: Library of utility functions
# Author: Sarah Perry

import os
import sys
import time
import datetime

# Clear the screen
def clear_screen():
    os.system('clear')


##########################################################
# Date and Time Handling
###########################################################

def convert_to_datetime(date):
    # Convert date string (format YYYY-MM-DD) to datetime object 
    date_dt = datetime.datetime.strptime(date, '%Y-%m-%d')
    return date_dt




##########################################################
# Handling Files
###########################################################

# Get the last ID from a file
def get_last_id(file_path, default_id):
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            if lines:
                last_line = lines[-1]
                last_id = int(last_line.split(",")[0].strip())
                return last_id
            else:
                return default_id          
    except FileNotFoundError:
        return default_id
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return default_id


# Turn file into a list
def get_list_from_file(file):
    data_list = []
    with open(file, 'r') as f:
        all_lines = f.readlines()
        for one_line in all_lines:
            entry = one_line.split(',')
            data_list.append(entry)
    return data_list





##########################################################
# Progress Indicators
###########################################################


# Generate progress indicator
def progress_dots(prompt):
    total_iterations = 10 # The more iterations, the more time is takes.
    print("")
    print(f"{prompt}...", end="")
    for _ in range(total_iterations):
        time.sleep(0.3)  # Simulate a delay
        print(".", end="", flush=True)  # Print a dot and flush the output buffer
    print("\n")  



def ProgressBar(iteration, total, prefix='', suffix='', length=30, fill='█'):
 
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
    sys.stdout.flush()


def blink_message(message, duration=3):
    end_time = time.time() + duration
    while time.time() < end_time:
        sys.stdout.write(f"\r{message}   ")
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write(f"\r{' ' * len(message)}   ")
        sys.stdout.flush()
        time.sleep(0.5)


##########################################################
# Dictionary Handling
###########################################################


def get_top_Xnum(dictionary, num):
    num = int(num)
    topX = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True)[:num])
    return topX

def get_bottom_Xnum(dictionary, num):
    bottomX = dict(sorted(dictionary.items(), key=lambda item: item[1])[:num])
    return bottomX



##########################################################
# Specific to HAB Taxi
###########################################################


def print_header(title, width):
    if width < 44:
        width = int(44)
        new_width = int(0)
    else:
        new_width = int((width-44)/2)

    print()
    print(f"{'-' * width}")
    print(f" " * new_width + '    __  _____    ____     ______           _ ' + " " * new_width)
    print(f" " * new_width + '   / / / /   |  / __ )   /_  __/___ __  __(_)' + " " * new_width)
    print(f" " * new_width + '  / /_/ / /| | / __  |    / / / __ `/ |/_/ / ' + " " * new_width)
    print(f" " * new_width + ' / __  / ___ |/ /_/ /    / / / /_/ />  </ /  ' + " " * new_width)
    print(f" " * new_width + '/_/ /_/_/  |_/_____/    /_/  \\__,_/_/|_/_/  ' + " " * new_width)
    print()
    print(f"{title:^{width}}")
    print(f"{'-' * width}")
    print()
