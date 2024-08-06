# Description:This program generates a profit listing and summary report for a specified date range.
# Author: Robot Group 3
# Date(s): Jul 31 2024 - 
 
 
# define libraries

import datetime
import handlers.display as FV  
from handlers.utility import print_header, convert_to_datetime
from handlers.validation import get_date_string



# define file paths
ExpensesFile = 'python-group3/data_files/expenses.dat'
RevenueFile = 'python-group3/data_files/revenue.dat'




# get constants
TODAY = datetime.datetime.today()


##############################################
#   Revenue and Expense Listing Functions    #
##############################################





def PrintRevRows(Rows, Ctr, Acc):

    # Generate report

    print("======================================================================================")
    print("Trans.      Trans.     Employee     Description         Subtotal     HST       Total")
    print("Number      Date        Number                                                ")
    print("======================================================================================")    
    for row in Rows:
        print(row) 

    print("======================================================================================")
    print(f"Total records: {Ctr:<4d}                                       Total Revenue: {FV.FDollar2(Acc):>11s}")




def PrintExpRows(Rows, Ctr, Acc):

    # Generate report

    print("======================================================================================")
    print("Invoice     Invoice      Employee     Description      Subtotal     HST       Total")
    print("Number       Date         Number                                               ")
    print("======================================================================================")
    
    for row in Rows:
        print(row) 

    print("======================================================================================")
    print(f"Total invoices: {Ctr:<4d}                                       Total Expenses: {FV.FDollar2(Acc):>11s}")





########################################################
# Define Functions to Calculate info For Summary Reports
########################################################

def CalculateRevSummary(StartDate_dt, EndDate_dt):

    # Initialize counters and accumulators
    TransCtr = 0
    StandFeesCtr = 0
    CarRentalCtr = 0
    ServiceFeesCtr = 0
    ProductSalesCtr = 0

    RevenueAcc = 0
    StandFeesAcc = 0
    CarRentalAcc = 0
    ServiceFeesAcc = 0
    ProductSalesAcc = 0

    RevByDriver = {}
    
    # Open the data file
    with open(RevenueFile, "r") as f:
        # Process each line (record) in the file in a loop
        for RevRecord in f:
            # Read the record and grab values from the list
            RevItem = RevRecord.split(",")
            TransDate = RevItem[1].strip()
            TransDate_dt = datetime.datetime.strptime(TransDate, "%Y-%m-%d")
            Driver = RevItem[2].strip()
            Description = RevItem[3].strip()
            Total = float(RevItem[6].strip())

            # Check if the invoice date falls within the specified date range
            if StartDate_dt <= TransDate_dt <= EndDate_dt:
            # Update counters and accumulators
                TransCtr += 1
                RevenueAcc += Total

                # Accumulate totals and count by revenue type
                if Description == "Monthly Stand Fee":
                    StandFeesAcc += Total
                    StandFeesCtr += 1
                elif 'Rental' in Description:
                    CarRentalAcc += Total
                    CarRentalCtr += 1
                elif Description == "Service Fees":
                    ServiceFeesAcc += Total
                    ServiceFeesCtr += 1
                elif Description == "Product Sales":
                    ProductSalesAcc += Total
                    ProductSalesCtr += 1

                # Accumulate totals by driver
                if Driver in RevByDriver:
                    RevByDriver[Driver] += Total
                else:
                    RevByDriver[Driver] = Total

    RevCtr = [StandFeesCtr, CarRentalCtr, ServiceFeesCtr, ProductSalesCtr]
    RevAcc = [StandFeesAcc, CarRentalAcc, ServiceFeesAcc, ProductSalesAcc]   

    return RevCtr, RevAcc, RevByDriver


def CalculateExpSummary(StartDate_dt, EndDate_dt):
    
        # Initialize counters and accumulators
        InvCtr = 0
        TireChangeCtr = 0
        OilChangeCtr = 0
        InspectionCtr = 0
        OtherExpensesCtr = 0
        
        ExpensesAcc = 0
        TireChangeAcc = 0
        OilChangeAcc = 0
        InspectionAcc = 0
        OtherExpensesAcc = 0

        ExpByCat = {}
    
        # Open the data file
        with open(ExpensesFile, "r") as f:
            # Process each line (record) in the file in a loop
            for ExpRecord in f:
                # Read the record and grab values from the list
                ExpLst = ExpRecord.split(",")
    
                InvDate = ExpLst[1].strip()
                InvDate_dt = get_date_string(InvDate)
                Description = ExpLst[3].strip()
                Total = float(ExpLst[6].strip())
    
                # Check if the invoice date falls within the specified date range
                if StartDate_dt <= InvDate_dt <= EndDate_dt:
                    # Update counters and accumulators
                    InvCtr += 1
                    ExpensesAcc += Total
    
                    # Accumulate totals and count by expense type
                    if Description == "Tire Change":
                        TireChangeAcc += Total
                        TireChangeCtr += 1
                    elif Description == "Oil Change":
                        OilChangeAcc += Total
                        OilChangeCtr += 1
                    elif "Inspection" in Description:
                        InspectionAcc += Total
                        InspectionCtr += 1
                    else:
                        OtherExpensesAcc += Total
                        OtherExpensesCtr += 1


                    if Description in ExpByCat:
                        ExpByCat[Description] += Total
                    else:
                        ExpByCat[Description] = Total

    
        ExpCtr = [TireChangeCtr, OilChangeCtr, InspectionCtr, OtherExpensesCtr]
        ExpAcc = [TireChangeAcc, OilChangeAcc, InspectionAcc, OtherExpensesAcc]


        return ExpCtr, ExpAcc, ExpByCat

################################################
# Print Summary Reports for Revenue and Expenses
################################################


def PrintRevSummary(StartDate_dt, EndDate_dt):

    RevCtr, RevAcc, RevByDriver = CalculateRevSummary(StartDate_dt, EndDate_dt)

    StandFeesCtr, CarRentalCtr, ServiceFeesCtr, ProductSalesCtr = RevCtr
    StandFeesAcc, CarRentalAcc, ServiceFeesAcc, ProductSalesAcc = RevAcc

    Top3_Rev = dict(sorted(RevByDriver.items(), key=lambda item: item[1], reverse=True)[:3])
    Bottom3_Rev = dict(sorted(RevByDriver.items(), key=lambda item: item[1])[:3])

    print(f"Monthly Stand Fees: {StandFeesCtr} transactions, Total Amount: {FV.FDollar2(StandFeesAcc):>11s}")
    print(f"Car Rental        : {CarRentalCtr} transactions, Total Amount: {FV.FDollar2(CarRentalAcc):>11s}")
    print(f"Service Fees      : {ServiceFeesCtr} transactions, Total Amount: {FV.FDollar2(ServiceFeesAcc):>11s}")
    print(f"Product Sales     : {ProductSalesCtr} transactions, Total Amount: {FV.FDollar2(ProductSalesAcc):>11s}")
    print()

    print("Top Drivers by Revenue:")
    for driver, revenue in Top3_Rev.items():
        print(f"    {driver}: ${revenue}")
    
    print("\nBottom Drivers by Revenue:")
    for driver, revenue in Bottom3_Rev.items():
        print(f"    {driver}: ${revenue}")


def PrintExpSummary(StartDate_dt, EndDate_dt):
    # get calculated values
    ExpCtr, ExpAcc, ExpByCat = CalculateExpSummary(StartDate_dt, EndDate_dt)

    TireChangeCtr, OilChangeCtr, InspectionCtr, OtherExpensesCtr = ExpCtr
    TireChangeAcc, OilChangeAcc, InspectionAcc, OtherExpensesAcc = ExpAcc

    Top3_Exp = dict(sorted(ExpByCat.items(), key=lambda item: item[1], reverse=True)[:3])
    #Bottom3_Exp = dict(sorted(ExpByCat.items(), key=lambda item: item[1])[:3])

    # print summary lines
    print(f"Repair parts: {TireChangeCtr} invoices, Total Amount: {FV.FDollar2(TireChangeAcc):>11s}")
    print(f"Oil change  : {OilChangeCtr} invoices, Total Amount: {FV.FDollar2(OilChangeAcc):>11s}")
    print(f"Inspection  : {InspectionCtr} invoices, Total Amount: {FV.FDollar2(InspectionAcc):>11s}")
    print(f"Other       : {OtherExpensesCtr} invoices, Total Amount: {FV.FDollar2(OtherExpensesAcc):>11s}")


    print("\nTop Expenses by Category:")
    for category, expense in Top3_Exp.items():
        print(f"    {category}: {FV.FDollar2(expense)}")




##################################################
# main program starts here    
##################################################


def GenerateFinancialReport(type):
    # For testing purposes, use the following hard-coded dates
    StartDate = "2022-01-01"
    EndDate = "2022-03-05"

    # # Get the start and end dates for the report


    # while True:
    #     StartDate = get_date_string("Enter the start date (YYYY-MM-DD): ")
    #     if TODAY < StartDate:
    #         print("Start date must be earlier than the current date. Please try again.")
    #     else:
    #         break


    # while True:
    #     EndDate = get_date_string("Enter the end date (YYYY-MM-DD): ")
    #     if EndDate < StartDate:
    #         print("End date must be greater than start date. Please try again.")
    #     else:
    #         break


    # Convert input dates to datetime objects
    StartDate_dt = convert_to_datetime(StartDate)
    EndDate_dt = convert_to_datetime(EndDate)



# Set report width
    width = int(86)

# Generate report headings
    if "summary" in type:
        print()
        print(f"{'='*width}")
        print(f"{'Financial Summary Report':^{width}}")
        print(f"{'='*width}")
        print()
    elif "revenue" in type:
        print_header("Revenue Listing Report", width)
    elif "expenses" in type:
        print_header("Expenses Listing Report", width)
    elif "profit" in type:
        print_header("Profit Listing Report", width)

    RevenueHeader = f"{'Revenue Listing':^{width}}\n"
    ExpensesHeader = f"{'Expense Listing':^{width}}\n"
    DateLine = f"From {StartDate} to {EndDate}"


# Calculate revenue data
    RevRows, TransCtr, RevenueAcc = GetRows(RevenueFile, StartDate_dt, EndDate_dt)

# Calculate expenses data
    ExpRows, InvCtr, ExpensesAcc = GetRows(ExpensesFile, StartDate_dt, EndDate_dt)

# Calculate profit/loss
    ProfitOrLoss = RevenueAcc - ExpensesAcc
    ProfitOrLossStr = FV.FDollar2(ProfitOrLoss)

# Generate footers 
    ListingFooter = f"\n{'END OF LISTING':^{width}}\n\n"
    


# Display the reports

    if "revenue" in type or "profit" in type:
        print(RevenueHeader)
        print(DateLine)
        PrintRevRows(RevRows, TransCtr, RevenueAcc)
        print()
        if "summary" in type:
            PrintRevSummary(StartDate_dt, EndDate_dt)
        print(ListingFooter)
    

    if "expenses" in type or "profit" in type:
        print(ExpensesHeader)
        print(DateLine)
        PrintExpRows(ExpRows, InvCtr, ExpensesAcc)
        print()
        if "summary" in type:
            PrintExpSummary(StartDate_dt, EndDate_dt)
        print(ListingFooter)

    if "profit" in type:
        # print Report footer
        print("======================================================================================")
        print(f"Total Profit/Loss: {ProfitOrLossStr:>11s}")


    print()
    print(f"{'END OF REPORT':^{width}}\n\n")


if __name__ == "__main__":
    GenerateFinancialReport("profit")