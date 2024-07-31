# display_handler.py

# import libraries
from datetime import datetime


def pc_add_dsp(postal_code):
# Returns a postal code in this format: A1A 1A1
    formatted_pc = (f"{postal_code[0]}{postal_code[1]}{postal_code[2]} {postal_code[3]}{postal_code[4]}{postal_code[5]}")
    return formatted_pc

def phone_num_dsp_wl(number, label):     
# Returns a phone number in this format: (999) 999-9999 (label)
    formatted_number = (
    f"({number[0]}{number[1]}{number[2]}) "
    f"{number[3]}{number[4]}{number[5]}-"
    f"{number[6]}{number[7]}{number[8]}{number[9]}")
    return f"{formatted_number} {label}".strip()

def phone_num_dsp(number):     
# Returns a phone number in this format: (999) 999-9999
    formatted_number = (
    f"({number[0]}{number[1]}{number[2]}) "
    f"{number[3]}{number[4]}{number[5]}-"
    f"{number[6]}{number[7]}{number[8]}{number[9]}")
    return formatted_number

def plate_number_dsp(plate_number):
# Returns a plate number in this format: AAA 111
    formatted_plate_num = (f"{plate_number[0:3]} {plate_number[3:6]}")
    return formatted_plate_num


def dollar_dsp_wl(value, label):     
# Returns a float as a formatted string with a label
    formatted_value = f"${value:,.2f}"
    return f"{label:<22s}{formatted_value:>10}".strip()


def dollar_dsp(value):     
# Returns a float as a formatted string, no label
    formatted_value = f"${value:,.2f}"
    return formatted_value


def percent_dsp_wl(value, label):     
# Displays a number as %  with a label
    formatted_value = f"{value:>12.0%}"
    return f"{label:<30s} {formatted_value}".strip()

def percent_dsp(value):     
# Displays a number as %  with a label
    formatted_value = f"{value:>12.0%}"
    return formatted_value

def date_yyyy_dsp(date):
# Function will accept a value and format it to yyyy-mm-dd.
    date = datetime.strftime(date, "%Y-%m-%d")
    return date


def date_dd_Mon_dsp(date):
# Function will accept a value and format it to dd-Mon-yy.
    date = datetime.strftime(date, "%d-%b-%y")
    return date


def date_dsp(date):
    # Function will accept a value and format it to Day, Month dd, yyyy.
    date = datetime.strftime(date, "%A, %B %d, %Y")
    return date


        #for key, value in user_contact.items():
        #    print(f"{key}: {value}")

