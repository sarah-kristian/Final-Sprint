import datetime
import sys
import time


print("-----------------------------------------------------------------------")
print("    __  _____    ____     ______           _ ")
print("   / / / /   |  / __ )   /_  __/___ __  __(_)")
print("  / /_/ / /| | / __  |    / / / __ `/ |/_/ / ")
print(" / __  / ___ |/ /_/ /    / / / /_/ />  </ /  ")
print("/_/ /_/_/  |_/_____/    /_/  \\__,_/_/|_/_/   ")
print()
print("          Employee Registration")
print("-----------------------------------------------------------------------")
print("Please complete the following prompts in order to register a new driver")
print()

# Blinking "loading" message

Message = "Loading prompts. Please stand by..."
for _ in range(3):  
    print(Message, end='\r')
    time.sleep(1)  
    sys.stdout.write('\033[2K\r')
    time.sleep(.7)

print("       Initialization complete!")
print("---------------------------------------------")
print()

# Define functions

def ValidateDate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except:
        return False
    
def ValidatePostal(PostalCode):
    for char in PostalCode:
        if char.isalnum() == False:
            if char != "-":
                return False
    return True
    
# Main program

while True:
    DriverNumber = input("Please enter the driver number: ")
    DriverFirstName = input("Please enter the driver's first name: ")
    DriverSurname = input("Please enter the driver's surname: ")
    StreetAdd = input("Please enter the driver's street address: ")
    City = input("Please enter the driver's city: ")

    while True:
        PostalCode = input("Please enter the driver's postal code (X#X-#X#) ").upper()
        if ValidatePostal(PostalCode):
            break
        else:
            print("Data-entry error: please ensure to strictly use alphanumeric characters and hyphens (-).")

    PhoneNumber = input("Please enter the driver's phone number ( (###)-###-#### ): ")
    DrivLicNum = input("Please enter the driver's license number: ")

    while True:
        LicenseExpiry = input("Please enter the driver's license expiry date (YYYY-MM-DD): ")
        if ValidateDate(LicenseExpiry):
            break
        else:
            print("Data-entry error: please enter the date in the given format (YYYY-MM-DD).")

    InsuranceCompany = input("Please enter the driver's associated insurance company: ")
    InsPolicyNum = input("Please enter the driver's insurance policy number: ")

    while True:
        OwnsCar = input("Does the driver own their vehicle (Y/N)?: ").upper()
        if OwnsCar in ["Y", "N"]:
            break
        else:
            print("Data-entry error: Please enter Y(for yes), or N(for no).")
    
    while True:
        try:
            BalanceDue = float(input("Balance Due: "))
            break
        except:
            print("Data-entry error: Please ensure that the balance due is a valid number.")

    # Writing to data file 

    f = open("Employees.dat", "a")

    f.write(f"{DriverNumber},{DriverFirstName},{DriverSurname},{StreetAdd},{City},{PostalCode},{PhoneNumber},"
            f"{DrivLicNum},{LicenseExpiry},{InsuranceCompany},{InsPolicyNum},"
            f"{OwnsCar},{BalanceDue}")
    
    f.close()

    AdditionalEntry = input("WOuld you like to enter another new employee into the system (Y/N)?: ").upper()
    if AdditionalEntry == "N":
        break
