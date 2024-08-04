# Profit Listing 
# Use the following to complete the rest of the summary data for the end of the report.
 
# Description:
# Author: Robot Group 3
# Date(s): Jul 31 2024 - 
 
 
#define libraries
import datetime
import handlers.display as FV  

#define file paths
ExpensesFile = 'python-group3/data_files/expenses.dat'
RevenueFile = 'python-group3/data_files/revenue.dat'



def printRevRows(StartDate_dt, EndDate_dt):
 # Open the data file
    with open(RevenueFile, "r") as f:
        # Process each line (record) in the file in a loop
        for RevRecord in f:
            # Read the record and grab values from the list
            RevLst = RevRecord.split(",")

            TransNum = RevLst[0].strip()
            TransDate = RevLst[1].strip()
            TransDate_dt = datetime.datetime.strptime(TransDate, "%Y-%m-%d")
            Description = RevLst[2].strip()
            EmplNum = RevLst[3].strip()
            TransAmnt = float(RevLst[4].strip())
            HST = float(RevLst[5].strip())
            Total = float(RevLst[6].strip())

            # Check if the invoice date falls within the specified date range
            if StartDate_dt <= TransDate_dt <= EndDate_dt:
                # Display the detail line
                print(f"  {TransNum:<11s}     {FV.FDateM(TransDate_dt):<10s}   {Description:<25s} {EmplNum:<10s} {FV.FDollar2(TransAmnt):>9s} {FV.FDollar2(HST):>9s} {FV.FDollar2(Total):>11s}")




def get_revenue_summary_data(StartDate_dt, EndDate_dt):

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
            Description = RevItem[2].strip()
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




        # Print summary data - counters and accumulators
    print("===================================================================================================")
    print(f"Total transactions: {TransCtr:<4d}                                                 Total Revenue: {FV.FDollar2(RevenueAcc):>11s}")
    print()
    print(f"Monthly Stand Fees: {StandFeesCtr} transactions, Total Amount: {FV.FDollar2(StandFeesAcc):>11s}")
    print(f"Car Rental        : {CarRentalCtr} transactions, Total Amount: {FV.FDollar2(CarRentalAcc):>11s}")
    print(f"Service Fees      : {ServiceFeesCtr} transactions, Total Amount: {FV.FDollar2(ServiceFeesAcc):>11s}")
    print(f"Product Sales     : {ProductSalesCtr} transactions, Total Amount: {FV.FDollar2(ProductSalesAcc):>11s}")
    print()
    print("                                         END OF LISTING")
    print("")

    return RevCtr, RevAcc


def printExpRows(StartDate_dt, EndDate_dt):
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


def PrintExpensesListing(StartDate_dt, EndDate_dt):
    
        # Generate report headings
 
        print("Invoice      Invoice      Employee     Description      Subtotal     HST       Total")
        print("Number        Date         Number                                               ")
        print("=====================================================================================")
        printExpRows(StartDate_dt, EndDate_dt)

def get_expenses_summary_data(StartDate_dt, EndDate_dt):
    
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
    
        # Print summary data - counters and accumulators
        print("=====================================================================================")
        print(f"Total invoices: {InvCtr:<4d}                                       Total Expenses: {FV.FDollar2(ExpensesAcc):>11s}")
        print()
        print(f"Repair parts: {TireChangeCtr} invoices, Total Amount: {FV.FDollar2(TireChangeAcc):>11s}")
        print(f"Oil change  : {OilChangeCtr} invoices, Total Amount: {FV.FDollar2(OilChangeAcc):>11s}")
        print(f"Inspection  : {InspectionCtr} invoices, Total Amount: {FV.FDollar2(InspectionAcc):>11s}")
        print(f"Other       : {OtherExpensesCtr} invoices, Total Amount: {FV.FDollar2(OtherExpensesAcc):>11s}")







def CalculateProfit():

    # initialize title
    title = ""
    # For testing purposes, use the following hard-coded dates
    StartDate = "2022-01-01"
    EndDate = "2022-03-05"

    # # Get the start and end dates for the report

    # # StartDate = input("Enter the start date (YYYY-MM-DD): ")
    # # EndDate = input("Enter the end date (YYYY-MM-DD): ")

    # Convert input dates to datetime objects
    StartDate_dt = datetime.datetime.strptime(StartDate, '%Y-%m-%d')
    EndDate_dt = datetime.datetime.strptime(EndDate, '%Y-%m-%d')


    # # Generate report headings




    ListingHeader = f"""\n                               HAB COMPANY
                        {title} Listing Report\n  
From {StartDate} to {EndDate}"""
    

    RevenueHeader = """
Transaction      Transaction      Description          Employee      Subtotal     HST        Total
  Number            Date                                Number                               
==================================================================================================="""


    ExpensesHeader = """
Invoice      Invoice      Employee     Description      Subtotal     HST       Total
Number        Date         Number                                               
====================================================================================="""

    ListingFooter = "\n                END OF LISTING\n\n"

    
    # print Revenue report
    title = "Revenue"
    print(ListingHeader)
    print(RevenueHeader)
    printRevRows(StartDate_dt, EndDate_dt)
    print(ListingFooter)

    # print Expenses report
    title = "Expenses"
    print(ListingHeader)
    print(ExpensesHeader)
    printExpRows(StartDate_dt, EndDate_dt)
    print(ListingFooter)
    
    # print("                                      END OF LISTING")
    # print("")
    # print("")

    # # Generate report headings
    # print()
    # print("                                       HAB COMPANY")
    # print(f"                                Revenue Listing Report")
    # print()
    # print(f"From {StartDate} to {EndDate}")
    # print()
    # print("Transaction      Transaction      Description          Employee      Subtotal     HST        Total")
    # print("  Number            Date                                Number                               ")
    # print("===================================================================================================")

    # # Initialize counters and accumulators
    # TransCtr = 0
    # StandFeesCtr = 0
    # CarRentalCtr = 0
    # ServiceFeesCtr = 0
    # ProductSalesCtr = 0

    # RevenueAcc = 0
    # StandFeesAcc = 0
    # CarRentalAcc = 0
    # ServiceFeesAcc = 0
    # ProductSalesAcc = 0


    # # Open the data file
    # with open(RevenueFile, "r") as f:
    #     # Process each line (record) in the file in a loop
    #     for RevRecord in f:
    #         # Read the record and grab values from the list
    #         RevLst = RevRecord.split(",")

    #         TransNum = RevLst[0].strip()
    #         TransDate = RevLst[1].strip()
    #         TransDate_dt = datetime.datetime.strptime(TransDate, "%Y-%m-%d")
    #         Description = RevLst[2].strip()
    #         EmplNum = RevLst[3].strip()
    #         TransAmnt = float(RevLst[4].strip())
    #         HST = float(RevLst[5].strip())
    #         Total = float(RevLst[6].strip())

    #         # Check if the invoice date falls within the specified date range
    #         if StartDate_dt <= TransDate_dt <= EndDate_dt:
    #             # Display the detail line
    #             print(f"  {TransNum:<11s}     {FV.FDateM(TransDate_dt):<10s}   {Description:<25s} {EmplNum:<10s} {FV.FDollar2(TransAmnt):>9s} {FV.FDollar2(HST):>9s} {FV.FDollar2(Total):>11s}")
                
    #             # Update counters and accumulators
    #             TransCtr += 1
    #             RevenueAcc += Total

    #             # Accumulate totals and count by revenue type
    #             if Description == "Monthly Stand Fee":
    #                 StandFeesAcc += Total
    #                 StandFeesCtr += 1
    #             elif 'Rental' in Description:
    #                 CarRentalAcc += Total
    #                 CarRentalCtr += 1
    #             elif Description == "Service Fees":
    #                 ServiceFeesAcc += Total
    #                 ServiceFeesCtr += 1
    #             elif Description == "Product Sales":
    #                 ProductSalesAcc += Total
    #                 ProductSalesCtr += 1

    # # Print summary data - counters and accumulators
    # print("===================================================================================================")
    # print(f"Total transactions: {TransCtr:<4d}                                                 Total Revenue: {FV.FDollar2(RevenueAcc):>11s}")
    # print()
    # print(f"Monthly Stand Fees: {StandFeesCtr} transactions, Total Amount: {FV.FDollar2(StandFeesAcc):>11s}")
    # print(f"Car Rental        : {CarRentalCtr} transactions, Total Amount: {FV.FDollar2(CarRentalAcc):>11s}")
    # print(f"Service Fees      : {ServiceFeesCtr} transactions, Total Amount: {FV.FDollar2(ServiceFeesAcc):>11s}")
    # print(f"Product Sales     : {ProductSalesCtr} transactions, Total Amount: {FV.FDollar2(ProductSalesAcc):>11s}")
    # print()
    # print("                                         END OF LISTING")
    # print("")
    
    # # Calculate and print profit/loss
    # ProfitOrLoss = RevenueAcc - ExpensesAcc
    # ProfitOrLossStr = FV.FDollar2(ProfitOrLoss)
    # print("===================================================================================================")
    # print(f"Total Profit/Loss: {ProfitOrLossStr:>11s}")
    # print()
    # print("                                          END OF REPORT")
    # print()
    # print()
    # print()





if __name__ == "__main__":
    CalculateProfit()