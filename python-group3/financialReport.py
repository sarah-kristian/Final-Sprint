# Description:This program generates a profit listing and summary report for a specified date range.
# Author: Robot Group 3
# Date(s): Jul 31 2024 - 
 
 
#define libraries
import datetime
import handlers.display as FV  

#define file paths
ExpensesFile = 'python-group3/data_files/expenses.dat'
RevenueFile = 'python-group3/data_files/revenue.dat'


# define header function
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


##############################################
#   Revenue and Expense Listing Functions    #
##############################################



def GetRows(FilePath, StartDate_dt, EndDate_dt):

    # Initialize counters and accumulators
    Ctr = 0
    Acc = 0
    Rows = []


    # Open the data file
    
    with open(FilePath, "r") as f:
        # Process each line (record) in the file in a loop
        for Record in f:
            # Read the record and grab values from the list
            RecordLine = Record.split(",")

            RecordNum = RecordLine[0].strip()
            TransDate = RecordLine[1].strip()
            TransDate_dt = datetime.datetime.strptime(TransDate, "%Y-%m-%d")
            idNum = RecordLine[2].strip()
            Description = RecordLine[3].strip()
            Subtotal = float(RecordLine[4].strip())
            HST = float(RecordLine[5].strip())
            Total = float(RecordLine[6].strip())

            # Check if the revenue date falls within the specified date range
            if StartDate_dt <= TransDate_dt <= EndDate_dt:

                # Update counters and accumulators
                Ctr += 1
                Acc += Total

                # Display the detail line
                row = f"  {RecordNum:<9s}{FV.FDateM(TransDate_dt):<10s}{idNum:^12s}  {Description:<20s}{FV.FDollar2(Subtotal):>9s} {FV.FDollar2(HST):>9s} {FV.FDollar2(Total):>11s}"

                Rows.append(row)
    
    return Rows, Ctr, Acc




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






###############################
# Options for summary reports #
###############################

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
    
    # Open the data file
    with open(RevenueFile, "r") as f:
        # Process each line (record) in the file in a loop
        for RevRecord in f:
            # Read the record and grab values from the list
            RevItem = RevRecord.split(",")
            TransDate = RevItem[1].strip()
            TransDate_dt = datetime.datetime.strptime(TransDate, "%Y-%m-%d")
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

    RevCtr = [TransCtr, StandFeesCtr, CarRentalCtr, ServiceFeesCtr, ProductSalesCtr]
    RevAcc = [RevenueAcc, StandFeesAcc, CarRentalAcc, ServiceFeesAcc, ProductSalesAcc]   

    return RevCtr, RevAcc


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
    
        # Open the data file
        with open(ExpensesFile, "r") as f:
            # Process each line (record) in the file in a loop
            for ExpRecord in f:
                # Read the record and grab values from the list
                ExpLst = ExpRecord.split(",")
    
                InvDate = ExpLst[1].strip()
                InvDate_dt = datetime.datetime.strptime(InvDate, "%Y-%m-%d")
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
    
        ExpCtr = [InvCtr, TireChangeCtr, OilChangeCtr, InspectionCtr, OtherExpensesCtr]
        ExpAcc = [ExpensesAcc, TireChangeAcc, OilChangeAcc, InspectionAcc, OtherExpensesAcc]

        return ExpCtr, ExpAcc




def PrintRevSummary(StartDate_dt, EndDate_dt):

    RevCtr, RevAcc = CalculateRevSummary(StartDate_dt, EndDate_dt)

    TransCtr, StandFeesCtr, CarRentalCtr, ServiceFeesCtr, ProductSalesCtr = RevCtr
    RevenueAcc, StandFeesAcc, CarRentalAcc, ServiceFeesAcc, ProductSalesAcc = RevAcc

        # Print summary data - counters and accumulators
    #print("===================================================================================================")
    #print(f"Total transactions: {TransCtr:<4d}                                                 Total Revenue: {FV.FDollar2(RevenueAcc):>11s}")
    #print()
    print(f"Monthly Stand Fees: {StandFeesCtr} transactions, Total Amount: {FV.FDollar2(StandFeesAcc):>11s}")
    print(f"Car Rental        : {CarRentalCtr} transactions, Total Amount: {FV.FDollar2(CarRentalAcc):>11s}")
    print(f"Service Fees      : {ServiceFeesCtr} transactions, Total Amount: {FV.FDollar2(ServiceFeesAcc):>11s}")
    print(f"Product Sales     : {ProductSalesCtr} transactions, Total Amount: {FV.FDollar2(ProductSalesAcc):>11s}")
    print()



def PrintExpSummary(StartDate_dt, EndDate_dt):
    ExpCtr, ExpAcc = CalculateExpSummary(StartDate_dt, EndDate_dt)

    InvCtr, TireChangeCtr, OilChangeCtr, InspectionCtr, OtherExpensesCtr = ExpCtr
    ExpensesAcc, TireChangeAcc, OilChangeAcc, InspectionAcc, OtherExpensesAcc = ExpAcc

    #print("======================================================================================")
    #print(f"Total invoices: {InvCtr:<4d}                                       Total Expenses: {FV.FDollar2(ExpensesAcc):>11s}")
    #print()
    print(f"Repair parts: {TireChangeCtr} invoices, Total Amount: {FV.FDollar2(TireChangeAcc):>11s}")
    print(f"Oil change  : {OilChangeCtr} invoices, Total Amount: {FV.FDollar2(OilChangeAcc):>11s}")
    print(f"Inspection  : {InspectionCtr} invoices, Total Amount: {FV.FDollar2(InspectionAcc):>11s}")
    print(f"Other       : {OtherExpensesCtr} invoices, Total Amount: {FV.FDollar2(OtherExpensesAcc):>11s}")




#############
# main program starts here    
#############


def GenerateFinancialReport(type):
    # For testing purposes, use the following hard-coded dates
    StartDate = "2022-01-01"
    EndDate = "2022-03-05"

    # # Get the start and end dates for the report

    # StartDate = input("Enter the start date (YYYY-MM-DD): ")
    # EndDate = input("Enter the end date (YYYY-MM-DD): ")

    # Convert input dates to datetime objects
    StartDate_dt = datetime.datetime.strptime(StartDate, '%Y-%m-%d')
    EndDate_dt = datetime.datetime.strptime(EndDate, '%Y-%m-%d')


# set report width
    width = int(86)

# Generate report headings
    if "summary" in type:
        print_header("Summary Report", width)
    elif "revenue" in type:
        print_header("Revenue Report", width)
    elif "expenses" in type:
        print_header("Expenses Report", width)
    elif "profit" in type:
        print_header("Profit Report", width)

    RevenueHeader = f"{'Expense Listing Report':^{width}}\n"
    ExpensesHeader = f"{'Expense Listing Report':^{width}}\n"
    DateLine = f"From {StartDate} to {EndDate}"


# Calculate revenue data
    RevRows, TransCtr, RevenueAcc = GetRows(RevenueFile, StartDate_dt, EndDate_dt)

# Calculate expenses data
    ExpRows, InvCtr, ExpensesAcc = GetRows(ExpensesFile, StartDate_dt, EndDate_dt)

# Calculate profit/loss
    ProfitOrLoss = RevenueAcc - ExpensesAcc
    ProfitOrLossStr = FV.FDollar2(ProfitOrLoss)

# generate footers 
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