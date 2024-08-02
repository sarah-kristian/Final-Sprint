
# import libraries

import datetime
import sys
import time
import handlers.utility as util
import handlers.validation as val

# define global variables
EmployeeFile = 'python-group3/data_files/employees.dat'
HeaderMsg = "Employee Registration"


# define functions
    
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



def print_header(prompt):
    print()
    print("-----------------------------------------------------------------------")
    print("            __  _____    ____     ______           _ ")
    print("           / / / /   |  / __ )   /_  __/___ __  __(_)")
    print("          / /_/ / /| | / __  |    / / / __ `/ |/_/ / ")
    print("         / __  / ___ |/ /_/ /    / / / /_/ />  </ /  ")
    print("        /_/ /_/_/  |_/_____/    /_/  \\__,_/_/|_/_/   ")
    print()
    print(f"                       {prompt}")
    print("-----------------------------------------------------------------------")
    print()


# Main program

def create_new_account():

    print_header(HeaderMsg)
    print("\nWelcome to HAB Taxi's Employee Registration system.")
    print("Please provide the following information to register a new driver\n")



    ##############################################################
    # Should we move this to the end and have it auto generated? #
    ##############################################################

    while True:
        while True:
            DriverNumber = input("Please enter the driver number: ")
            try:
                int(DriverNumber)
                break
            except:
                print("Data-entry error: Please ensure that the driver's number has a strictly-numeric value.")

    # Data entry for driver contact information
        DriverFirstName = input("Please enter the driver's first name: ").title().strip()
        DriverSurname = input("Please enter the driver's surname: ").title().strip()
        StreetAdd = input("Please enter the driver's street address: ").title().strip()
        City = input("Please enter the driver's city: ").title().strip()

        while True:
            PostalCode = input("Please enter the driver's postal code (X#X-#X#) ").upper()
            if ValidatePostal(PostalCode):
                break
            else:
                print("Data-entry error: please ensure to strictly use alphanumeric characters and hyphens (-).")

        while True:    
            PhoneNumber = input("Please enter the driver's phone number ( ###-###-#### ): ")
            if ValidatePhone(PhoneNumber):
                break
            else:
                print("Data-entry error: please ensure that the phone number is entered in the requested format, including hyphens (-).")

    # Data entry for driver license information
        print("\nPlease provide the following driver's license information:")
        DrivLicNum = input("Please enter the driver's license number: ")

        while True:
            LicenseExpiry = input("Please enter the driver's license expiry date (YYYY-MM-DD): ")
            if val.ValidateDate(LicenseExpiry):
                break
            else:
                print("Data-entry error: please enter the date in the given format (YYYY-MM-DD).")


    # Data entry for driver insurance information
        print("\nPlease provide the following insurance information:")
        InsuranceCompany = input("Please enter the driver's associated insurance company: ")

        while True:
            InsPolicyNum = input("Please enter the driver's insurance policy number: ")
            try:
                int(InsPolicyNum)
                break
            except:
                print("Data-entry error: Please ensure that the insurance policy number has a strictly-numeric value.")


    # Data entry for driver vehicle information
        while True:
            OwnsCar = input("Does the driver own their vehicle (Y/N)?: ").upper()
            if OwnsCar in ["Y", "N"]:
                break
            else:
                print("Data-entry error: Please enter Y(for yes), or N(for no).")



    ##################################
    #       Do we need this?         #
    ##################################


        while True:
            try:
                BalanceDue = float(input("Balance Due: "))
                break
            except:
                print("Data-entry error: Please ensure that the balance due is a valid number.")

        # Writing to data file 

        f = open(EmployeeFile, "a")

        f.write(f"{DriverNumber},{DriverFirstName},{DriverSurname},{StreetAdd},{City},{PostalCode},{PhoneNumber},{DrivLicNum},{LicenseExpiry},{InsuranceCompany},{InsPolicyNum},{OwnsCar},{BalanceDue}\n")
        
        f.close()

        AdditionalEntry = input("Would you like to enter another new employee into the system (Y/N)?: ").upper()
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