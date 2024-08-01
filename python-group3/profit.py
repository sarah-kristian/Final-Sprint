# Profit Listing 
# Use the following to complete the rest of the summary data for the end of the report.
 
# Description:
# Author: Robot Group 3
# Date(s): Jul 31 2024 - 
 
 
#define libraries
import datetime
import display_handler as FV  

#define file paths
ExpensesFile = 'python-group3/expenses.dat'
RevenueFile = 'python-group3/revenue.dat'


def CalculateProfit():
    # Get the start and end dates for the report
    print()
    print("This program will generate a profit report for a specified date range.")
    print()
    #StartDate = input("Enter the start date (YYYY-MM-DD): ")
    #EndDate = input("Enter the end date (YYYY-MM-DD): ")
    StartDate = "2022-01-01"
    EndDate = "2024-07-31"


    # Convert input dates to datetime objects
    StartDate_dt = datetime.datetime.strptime(StartDate, '%Y-%m-%d')
    EndDate_dt = datetime.datetime.strptime(EndDate, '%Y-%m-%d')

    # Generate report headings
    print()
    print("                               HAB COMPANY")
    print(f"                        Expenses Listing Report  ")
    print()
    print(f"From {StartDate} to {EndDate}")
    print()
    print("Invoice      Invoice      Employee     Description      Subtotal     HST       Total")
    print("Number        Date         Number                                               ")
    print("=====================================================================================")



    # Initialize counters and accumulators
    InvCtr = 0
    ExpensesAcc = 0

    # Open the data file
    with open(ExpensesFile, "r") as f:
        # Process each line (record) in the file in a loop
        for ExpRecord in f:
            # Read the record and grab values from the list
            ExpLst = ExpRecord.split(",")

            InvNum = ExpLst[0].strip()
            InvDate = ExpLst[1].strip()
            InvDate_dt = datetime.datetime.strptime(InvDate, "%Y-%m-%d")
            EmpNum = ExpLst[2].strip()
            Description = ExpLst[3].strip()
            Subtotal = float(ExpLst[4].strip())
            HST = float(ExpLst[5].strip())
            Total = float(ExpLst[6].strip())

            # Check if the invoice date falls within the specified date range
            if StartDate_dt <= InvDate_dt <= EndDate_dt:
                # Display the detail line
                print(f"{InvNum:<11s} {FV.FDateM(InvDate_dt):<10s}     {EmpNum:<10s} {Description:<15s} {FV.FDollar2(Subtotal):>9s} {FV.FDollar2(HST):>9s} {FV.FDollar2(Total):>11s}")
                
                # Update counters and accumulators
                InvCtr += 1
                ExpensesAcc += Total

    # Print summary data - counters and accumulators
    print("=====================================================================================")
    print(f"Total invoices: {InvCtr:<4d}                                      Total Expenses: {FV.FDollar2(ExpensesAcc):>11s}")
    print()
    print("                                      END OF LISTING")
    print("")
    print("")



    # Generate report headings
    print()
    print("                                       HAB COMPANY")
    print(f"                                Revenue Listing Report")
    print()
    (f"From {StartDate} to {EndDate}")
    print()
    print("Transaction      Transaction      Description          Employee      Subtotal     HST        Total")
    print("  Number            Date                                Number                               ")
    print("===================================================================================================")



    # Initialize counters and accumulators
    TransCtr = 0
    RevenueAcc = 0

    # Open the data file
    with open(RevenueFile, "r") as f:
        # Process each line (record) in the file in a loop
        for RevRecord in f:
            # Read the record and grab values from the list
            RevLst = RevRecord.split(",")

            TransNum = RevLst[0].strip()
            TransDate = RevLst[1].strip()
            TransDate_dt = datetime.datetime.strptime(InvDate, "%Y-%m-%d")
            Description = RevLst[2].strip()
            EmplNum = RevLst[3].strip()
            TransAmnt = float(RevLst[4].strip())
            HST = float(RevLst[5].strip())
            Total = float(RevLst[6].strip())

            # Check if the invoice date falls within the specified date range
            if StartDate_dt <= InvDate_dt <= EndDate_dt:
                # Display the detail line
                print(f"  {TransNum:<11s}     {FV.FDateM(TransDate_dt):<10s}   {Description:<25s} {EmplNum:<10s} {FV.FDollar2(TransAmnt):>9s} {FV.FDollar2(HST):>9s} {FV.FDollar2(Total):>11s}")
                
                # Update counters and accumulators
                TransCtr += 1
                RevenueAcc += Total

    # Print summary data - counters and accumulators
    print("===================================================================================================")
    print(f"Total invoices: {TransCtr:<4d}                                                     Total Revenue: {FV.FDollar2(RevenueAcc):>11s}")
    print()
    print("                                         END OF LISTING")
    print("")
    # Calculate and print profit/loss
    ProfitOrLoss = RevenueAcc - ExpensesAcc
    ProfitOrLossStr = FV.FDollar2(ProfitOrLoss)
    print("===================================================================================================")
    print(f"Total Profit/Loss: {ProfitOrLossStr:>11s}")
    print()
    print("                                          END OF REPORT")
    print()
    print()
    print()




CalculateProfit()