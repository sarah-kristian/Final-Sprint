# import libraries

from datetime import datetime, timedelta
import time
import handlers.utility as util
import handlers.validation as val
import handlers.display as dsp


# Define global variables
EmployeeFile = 'python-group3/data_files/employees.dat'
DefaultsFile = 'python-group3/data_files/defaults.dat'

HeaderMsg = "Employee Registration"
RENEWAL_PD = int(26)

# Assign default data to constants

with open(DefaultsFile, "r") as f:
    lines = f.readlines()
    NEW_TRANS_NUM = int(lines[0].strip())
    DRIVER_NUMBER = int(lines[1].strip())
    MONTH_STAND_FEE = float(lines[2].strip())
    DAILY_RENTAL_FEE = float(lines[3].strip())
    WEEKLY_RENTAL_FEE = float(lines[4].strip())
    HST_RATE = float(lines[-1].strip())

# define functions
    
def ValidateDate(date_text):
    try:
        datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        print("Data-entry error: please enter the date in the given format (YYYY-MM-DD).")



# Main program

def create_new_account():

    util.print_header(HeaderMsg, 80)
    print("\nWelcome to HAB Taxi's Employee Registration system.")
    print("Please provide the following information to register a new driver:\n")



    while True:
         # Auto-generate DriverNumber

##########################
# N.B.: I edit this part because you actuall get this info at the beginning of the program; 
# I also got it to write all the lines to prevent it from erasing the remaining lines
# in the defaults.dat file
#########################


    #     f = open(DefaultsFile, "r")
    #     DriverNumber = int(f.readline().strip())
    #     f.close()
    
        # f = open(DefaultsFile, "w")
        # f.write(str(DriverNumber + 1))
        # f.close()

        with open(DefaultsFile, "w") as f:
            lines[0] = str(NEW_TRANS_NUM + 1) + "\n"
            lines[1] = str(DRIVER_NUMBER + 1) + "\n"
            f.writelines(lines)


        #Data entry for driver contact information
        DriverFirstName = val.get_user_info("   Driver's first name:                  |   ").title().strip()
        DriverSurname =   val.get_user_info("   Driver's surname:                     |   ").title().strip()
        StreetAdd =       val.get_user_info("   Driver's street address:              |   ").title().strip()
        City =            val.get_user_info("   Driver's city:                        |   ").title().strip()
        
        
        PostalCode =        val.get_user_pc("   Driver's postal code (X#X #X#):       |   ")
        PostalCodeDSP = dsp.pc_add_dsp(PostalCode)
        PhoneNumber =    val.get_user_phone("   Driver's phone number (###-###-####): |   ")
        PhoneNumberDSP = dsp.phone_num_dsp(PhoneNumber)

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
        InsuranceCompany = val.get_user_info("    Associated insurance company:        |   ")

        while True:
            InsPolicyNum = val.get_user_info("    Insurance policy number:             |   ")
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


        StartDate = datetime.now()
        StartDateDSP = dsp.FDateM(StartDate)
        #StartDate.strftime("%Y-%m-%d")

        CurrentDay = StartDate.day
        RenewalDate = (datetime.now() + timedelta(weeks=RENEWAL_PD))
        RenewalDateDSP = dsp.FDateM(RenewalDate)

        DaysInMonth = (StartDate.replace(month=StartDate.month % 12 + 1, day=1) - timedelta(days=1)).day     

    # Calculating the balance due

        if OwnsCar == "Y":
            BalanceDue = (MONTH_STAND_FEE / DaysInMonth) * (DaysInMonth - CurrentDay + 1)

        else:
            while True:
                RentalType = input("    Is the vehicle a daily rental or weekly rental? (D/W): ")[0].upper()

                if RentalType in ["D", "W"]:
                    if RentalType == "D":
                        BalanceDue = DAILY_RENTAL_FEE * (DaysInMonth - CurrentDay + 1)

                    elif RentalType == "W":
                        BalanceDue = WEEKLY_RENTAL_FEE
                    break
                else:
                    print("Data-entry error: Please enter D(for daily), or W(for weekly).")   

        # Generating the customer ID receipt

        BalanceDueDSP = f"{BalanceDue:.2f}"
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
        print(f"|  Driver ID: {DRIVER_NUMBER:<6}                |")
        print("|  Job Title: Driver                |")
        print(f"|  Phone: {PhoneNumberDSP}            |")
        print(f"|  License No: {DrivLicNum:<9}            |")
        print(f"|  Expiry Date: {LicenseExpiry}          |")
        print("|                                   |")
        print(f"|  Start Date: {StartDateDSP}            |") 
        print(f"|  Renewal Date: {RenewalDateDSP}          |")  
        print("+-----------------------------------+")
        print()

        # Writing to data file 

        f = open(EmployeeFile, "a")
        f.write(f"{DRIVER_NUMBER},{DriverFirstName},{DriverSurname},{StreetAdd},{City},{PostalCodeDSP},{PhoneNumberDSP},{DrivLicNum},{LicenseExpiry},{InsuranceCompany},{InsPolicyNum},{OwnsCar},{BalanceDueDSP}\n")
        f.close()



    #####################
    # Should we add a statment saying what the balance is or anything like that? I'm thinking no....
    #####################

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
