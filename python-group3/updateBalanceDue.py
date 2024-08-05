import datetime
import time
import sys

# Define File Paths
EmployeeFile = 'python-group3/data_files/employees.dat'
ExpensesFile = 'python-group3/data_files/expenses.dat'
RevenuesFile = 'python-group3/data_files/revenue.dat'
DefaultsFile = 'python-group3/data_files/defaults.dat'


# Define Constants from Default File

with open(DefaultsFile, "r") as f:
    lines = f.readlines()
    NEW_TRANS_NUM = int(lines[0].strip())
    MONTHLY_STAND_FEE = float(lines[2].strip())
    HST_RATE = float(lines[-1].strip())



def blink_message(message, duration=3):
    end_time = time.time() + duration
    while time.time() < end_time:
        sys.stdout.write(f"\r{message}   ")
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write(f"\r{' ' * len(message)}   ")
        sys.stdout.flush()
        time.sleep(0.5)


def charge_stand_fees():
    NewTransNum = NEW_TRANS_NUM
    
    try:
        # Prompt user for date input


        ######################
        #CurDate=datetime.datetime.today()
        #CurDate = input("Enter date (YYYY-MM-DD): ") # assuming the entry date is the first day of the month
        CurDate="2024-01-01" #this should be the current date from the system, it is just for testing here
        ######################
        CurDate  = datetime.datetime.strptime(CurDate , '%Y-%m-%d')

        if CurDate.day == 1:   # Check if the current date is the first day of the month.
            # Read the employee file to identify drivers with their own cars
            Employees = []            #Initialize an empty list to store employees with their own cars.
            with open(EmployeeFile, "r") as EmpFile:
                EmployeeRecords = EmpFile.readlines()
                for i, Record in enumerate(EmployeeRecords):
                    EmpLst = Record.split(",")
                    EmpNum = EmpLst[0].strip()
                    BalanceDue = float(EmpLst[12].strip())
                    OwnCar = EmpLst[11].strip()  # Assuming 'N' or 'Y'
                    if OwnCar == 'Y':
                        Employees.append((EmpNum, BalanceDue, i))  # Add index to update later
                #print(Employees)

            # Read the revenue file to find the last transaction number
            # LastTransnum = 0
            # with open(RevenueFile, "r") as RevFile:
            #     for Record in RevFile:
            #         if Record.strip():  # Ensure the line is not empty
            #             RevLst = Record.split(",")
            #             try:
            #                 TransNum = int(RevLst[0].strip())
            #                 if TransNum> LastTransnum:
            #                     LastTransnum = TransNum
            #             except:
            #                 print(f"Error reading transaction number from record: {Record}")
                            

            # # Increment the transaction number for new records
            # NewTransNum = LastTransnum+ 1

            # Generate the revenue records and update the revenue file
            with open(RevenuesFile, "a") as RevFile:
                for Emp in Employees:
                    EmpNum, BalanceDue, i = Emp     #Unpack the employee's data.
                    HST_amt = MONTHLY_STAND_FEE * HST_RATE
                    Total = MONTHLY_STAND_FEE + HST_amt 

                    # Create new record and write to the revenue file
                    NewRecord = f"{NewTransNum},{CurDate .strftime('%Y-%m-%d')},Monthly Stand Fees,{EmpNum},{MONTHLY_STAND_FEE:.2f},{HST_amt:.2f},{Total:.2f}\n"
                    RevFile.write(NewRecord)

                    NewTransNum += 1  # Increment transaction number for each new record
                    print(f"Added record: {NewRecord.strip()}")  # Debug print to confirm addition

            # Update BalanceDue for the employees
            for Emp in Employees:
                EmpNum, BalanceDue, i = Emp
                NewBalanceDue = BalanceDue + Total  # Not sure if we need to add the Monthly Stand Fees only or Total 
                Emplst = EmployeeRecords[i].split(",")
                Emplst[12] = f"{NewBalanceDue:.2f}"
                EmployeeRecords[i] = ",".join(Emplst) + "\n"  #Reconstruct the record
                
                # Display blinking message for each update
                blink_message(f"Updating Balance Due for Employee {EmpNum}", duration=1.5)
                    
            # Write the updated employee records back to the file
            with open(EmployeeFile, "w") as EmpFile:
                EmpFile.writelines(EmployeeRecords)
            print("Updated Balance Due in Employees.dat")

    except:
        print(f"An error occurred.")

# Call the function to charge stand fees
if __name__ == "__main__":
    charge_stand_fees()