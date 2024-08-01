# validation.py

# Description: Library of functions to validate user input
# Author: Sarah Perry


# import libraries

from datetime import datetime


def get_user_info(prompt):  
# input validation to ensure string isn't blank 
    while True:
        info = input(prompt).title().strip()
        if info != "":
            return info
        else: 
            print(" ** Field must not be blank. Please re-enter. ** ")

 


# personal information
 
def get_user_phone(prompt):   
# input validation for phone number
    while True:
        phone_number = input(prompt).replace(" ", "").replace("(", "").replace(")", "").replace("-", "")
        if phone_number.isdigit() and len(phone_number) == 10:  # Check if input consists of exactly 10 digits
            return phone_number 
        else:
            print(" ** Invalid input, please enter a 10-digit number. **")



def get_user_prov(prompt):
# input validation for Canadian province
    # Dictionary of alternative province inputs (doesn't account for accents)
    alias = {
        "NFLD":"NL", "TNL":"NL", "NEWFOUNDLAND":"NL", "LABRADOR":"NL",
        "PE":"PEI", "PE":"IPE", "PRINCE EDWARD ISLAND":"PEI",
        "NE":"NS", "N-B":"NB", "NOVA SCOTIA":"NS",
        "QUE":"QC", "QUEBEC":"QC",
        "ONT":"ON", "ONTARIO":"ON",
        "MAN":"MB", "MANITOBA":"MB",
        "SASK":"SK", "SASKATCHEWAN":"SK",
        "ALTA":"AB", "ALB":"AB", 
        "CB":"BC",
        "YN":"YT", 
        "NWT":"NT", 
        "TNO":"NT", 
        "NVT":"NU", 
        "NT":"NU"
        }
    valid_provinces = {"NL", "PE", "NS", "NB", "QC", "ON", "MB", "SK", "AB", "BC", "YT", "NT", "NU"}
    while True:
        province = input(prompt).upper().strip().replace(".", "").replace("-", "")
        province = alias.get(province, province)
        if province in valid_provinces:
            return province
        else: 
            print(" ** Invalid input, please enter the the correct two letter province code. **")


def get_user_pc(prompt):
# input validation for postal code
    while True:
        pc_add = input(prompt).upper().replace(" ", "")
        if (len(pc_add) == 6 and 
            pc_add[1].isdigit() and pc_add[3].isdigit() and pc_add[5].isdigit() and 
            pc_add[0].isalpha() and pc_add[2].isalpha() and pc_add[4].isalpha()):
            return pc_add
        else:
            print(" ** Invalid input, please enter the postal code in the form A1B 2C3. **")




def get_user_contact():
    first_name =  get_user_info("First Name:     ")
    last_name =   get_user_info("Last Name:      ")
    street_add =  get_user_info("Street:         ")
    city_add =    get_user_info("City:           ")
    prov_add =    get_user_prov("Province:       ")
    pc_add =        get_user_pc("Postal Code:    ")
    phone_num =    get_user_phone("Phone Number:   ")
 
    return {
        "first_name": first_name,
        "last_name": last_name,
        "street_add": street_add,
        "city_add" : city_add,
        "prov_add" : prov_add,   
        "pc_add": pc_add,
        "phone_num": phone_num,
    }


# input validation for options

def get_user_yesno(prompt):   
# retrives extra options in required 'Y' or 'N' format
    while True:
        option = input(prompt).upper().strip() 
        if option in ["Y", "N", "YES", "NO"]:
            return option 
        else:
            print("    ** Invalid input, please enter 'Y' for Yes or 'N' for No. **")


def get_list_option(prompt, option_list):   
# retrives extra options in required format set (shown in a list)
    while True:
        option = input(prompt)[0].upper().strip() 
        if option in option_list:
            return option 
        else:
            print(f"    ** Invalid input, please enter and option from {option_list} **")



def get_dict_option(prompt, dict_option):
# retrives extra options in required format set (shown in a dictionary)
    # Create a reverse mapping from values to keys
    value_to_key = {v.upper().strip(): k for k, v in dict_option.items()}
    
    while True:
        option = input(prompt).upper().strip()
        if option in dict_option:
            return option
        elif option in value_to_key:
            return value_to_key[option]
        else:
            print(f"    ** Invalid input, please enter an option from {list(dict_option.keys()) + list(dict_option.values())} **")



# input validation for numbers

def get_user_date(prompt):
    while True:
        date = input(prompt).strip()
        try:
            return datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            print(" ** Invalid date format. Please enter the date in YYYY-MM-DD format. **")


def get_user_int(prompt):
# input validation for integers
    while True:
        digits = input(prompt).replace(",", "")
        try:
            digits = int(digits)  # Attempt to convert the input to an integer
            return digits
        except ValueError:
            print(" ** That's not a valid value. Please enter a whole number. **")


def get_user_float(prompt):
# input validation for floats
    while True:
        digits = input(prompt).replace("$","")
        try:
            digits = float(digits)         # Attempt to convert the input to a float
            return digits
        except ValueError:
            print(" ** That's not a valid number. Please enter a number. **")


def get_year(prompt): 
# input validation for year (YYYY); should be updated if want year to be a current-ish year
    while True:
        year = input(prompt).strip()
        
        # Check if the input is a 4-digit number
        if not year.isdigit() or len(year) != 4:
            print(" ** Invalid input. Please enter a valid 4-digit year (YYYY). **")
            continue

        # Convert the year to an integer
        year = int(year)
        return year



def get_year_between(prompt, start, end):
    # Convert the start year to a datetime object
    start = datetime.strptime(start, '%Y').year
    
    # Handle special cases for the end year
    if end.lower() in ['today', 'now', 'current']:
        end = datetime.now().year
    else:
        end = datetime.strptime(end, '%Y').year

    while True:
        year = input(prompt).strip()
        
        # Check if the input is a 4-digit number
        if not year.isdigit() or len(year) != 4:
            print(" ** Invalid input. Please enter a valid 4-digit year (YYYY). **")
            continue

        # Convert the year to an integer
        year = int(year)

        # Validate the year range
        if year < start:
            print(f" ** Invalid input. Year cannot be before {start}. **")
        elif year > end:
            print(f" ** Invalid input. Year cannot be later than {end}. **")
        else:
            return year


def get_plate_number(prompt):
# input validation for Canadian car plate number
    while True:
        plate_number = input(prompt).upper().replace(" ", "")
        if (len(plate_number) == 6 and 
            plate_number[0:3].isalpha() and plate_number[3:6].isdigit()):
            return plate_number
        else:
            print(" ** Invalid input, please enter the plate number in the form XXX999. **")







# input validation for credit card

def get_exp_date(prompt): 
# input validation for year (MM/YY); should be updated if want year to be a current-ish year
    while True:
        date = input(prompt).strip().replace("/", "").replace("-", "")
        if date.isdigit() is False:
            print(" ** Invalid input. Expiry date must be written as digits. **")
        elif len(date) != 4:
            print(" ** Invalid input. Please enter a valid expiry date (MM/YY). **")
        elif int(date[0:2]) > 12:
            print(" ** Invalid input. Please enter a valid month (MM). **")
        elif int(date[2:4]) < 20:
            print(" ** Invalid input. Please enter a valid year (YY). **")
        else:
            return date



def get_credit_card(prompt):
# input validation for credit card number    
    while True:
        card_number = input(prompt).replace(" ", "").replace("-", "")
        # Check if all characters are digits
        if not card_number.isdigit():
            print(" ** Invalid input. Credit card number must contain only digits. **")
        # Check length of the card number (13-19 digits)
        elif not 13 <= len(card_number) <= 19:
            print(" ** Credit card number must be between 13 and 19 digits long. **")
        else:
            return card_number
