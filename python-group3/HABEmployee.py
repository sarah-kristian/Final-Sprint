# import libraries

from datetime import datetime, timedelta
import sys
import time
import handlers.utility as util
import handlers.validation as val
import handlers.display as dis

# define global variables
EmployeeFile = 'python-group3/data_files/employees.dat'
DefaultsFile = 'python-group3/data_files/defaults.dat'
HeaderMsg = "Employee Registration"


# define utlity functions
    
def ValidatePostal(PostalCode):
    for char in PostalCode:
        if char.isalnum() == False:
            if char != "-":
                return False
    return True


def ValidatePhone(PhoneNumber):
    if len(PhoneNumber) != 12:
        return False
    for i in range(len(PhoneNumber)):
        if i in [3, 7]:
            if PhoneNumber[i] != '-':
                return False
        elif not PhoneNumber[i].isdigit():
            return False
    return True


def ValidateDate(date_text):
    try:
        datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except:
        return False


#define display functions

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


# Main program

def create_new_account():

    print_header(HeaderMsg, 80)
    print("\nWelcome to HAB Taxi's Employee Registration system.")
    print("Please provide the following information to register a new driver:\n")


    while True:
        # Auto-generate DriverNumber
        f = open(DefaultsFile, "r")
        DriverNumber = int(f.readline().strip())
        f.close()

        f = open(DefaultsFile, "w")
        f.write(str(DriverNumber + 1))
        f.close()

    # Data entry for driver contact information
        DriverFirstName = val.get_user_info("   Driver's first name:                  |   ").title().strip()
        DriverSurname =               input("   Driver's surname:                     |   ").title().strip()
        StreetAdd =                   input("   Driver's street address:              |   ").title().strip()
        City =                        input("   Driver's city:                        |   ").title().strip()
        
        
        PostalCode =        val.get_user_pc("   Driver's postal code (X#X #X#):       |   ")
        PhoneNumber =    val.get_user_phone("   Driver's phone number (###-###-####): |   ")

    # Data entry for driver license information
        print("\n\nPlease provide the following driver's license information:\n")
        DrivLicNum =                  input("    License number:                      |   ")

        while True:
            LicenseExpiry =           input("    License expiry date (YYYY-MM-DD):    |   ")
            if val.ValidateDate(LicenseExpiry):
                break
            else:
                print("Data-entry error: please enter the date in the given format (YYYY-MM-DD).")

    # Data entry for driver insurance information
        print("\n\nPlease provide the following insurance information:\n")
        InsuranceCompany =            input("    Associated insurance company:        |   ")

        while True:
            InsPolicyNum =            input("    Insurance policy number:             |   ")
            try:
                int(InsPolicyNum)
                break
            except:
                print("Data-entry error: Please ensure that the insurance policy number has a strictly-numeric value.")

    # Data entry for driver vehicle information
        print("\n\nPlease provide the following information:\n")
        while True:
            OwnsCar = input("    Does the driver own their vehicle (Y/N)?: ")[0].upper()
            if OwnsCar in ["Y", "N"]:
                break
            else:
                print("Data-entry error: Please enter Y(for yes), or N(for no).")

    ##################################
    #       Do we need this?         #
    ##################################

        while True:
            try:
                BalanceDue = float(input("\nBalance Due: "))
                break
            except:
                print("Data-entry error: Please ensure that the balance due is a valid number.")

        StartDate = datetime.now().strftime("%Y-%m-%d")
        RenewalDate = (datetime.now() + timedelta(weeks=26)).strftime("%Y-%m-%d")        

        # Generating the customer ID receipt

        NameDSP = f"{DriverFirstName} {DriverSurname}"

        print()
        print("+-----------------------------------+")
        print("|         HAB TAXI SERVICES         |")
        print("|                                   |")
        print("|    Driver ID Card                 |")
        print("|                                   |")
        print("|  [Driver Photo]                   |")
        print("|                                   |")
        print(f"|  Name: {NameDSP:<23}    |")
        print(f"|  Driver ID: {DriverNumber:<6}                |")
        print("|  Job Title: Driver                |")
        print(f"|  Phone: {dis.phone_num_dsp(PhoneNumber)}            |")
        print(f"|  License No: {DrivLicNum:<9}            |")
        print(f"|  Expiry Date: {LicenseExpiry}          |")
        print("|                                   |")
        print(f"|  Start Date: {StartDate}           |") 
        print(f"|  Renewal Date: {RenewalDate}         |")  # Placeholder date
        print("+-----------------------------------+")
        print()

        # Writing to data file 

        f = open(EmployeeFile, "a")

        f.write(f"{DriverNumber},{DriverFirstName},{DriverSurname},{StreetAdd},{City},{PostalCode},{PhoneNumber},{DrivLicNum},{LicenseExpiry},{InsuranceCompany},{InsPolicyNum},{OwnsCar},{BalanceDue}\n")
        
        f.close()

        AdditionalEntry = input("\nWould you like to enter another new employee into the system (Y/N)?: ").upper()
        if AdditionalEntry == "N":
            break
      
    # Progress bar + exit message
    print()
    print("Saving your entries...")
    print()
    for i in range(10):
        time.sleep(0.1)  
        util.ProgressBar(i + 1, 10, suffix='Complete', length=50)
    print()
    print()
    print("Thank you for using HAB Taxi's Employee Registration system.")
    print()
    print("Have a great day!\n")


if __name__ == "__main__":
    create_new_account()
