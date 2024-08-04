
# Description: Corporate Summary Report
# Author Robot Group 3
# Date: 2024-Jul-31 to 2024-Aug-07

# import libraries

from datetime import datetime
import sys
import time
import handlers.utility as util
import handlers.validation as val

# define global variables
EmployeeFile = 'python-group3/data_files/employees.dat'
ExpensesFile = 'python-group3/data_files/expenses.dat'
RevenuesFile = 'python-group3/data_files/revenues.dat'
RentalsFile = 'python-group3/data_files/rentals.dat'

HeaderMsg = "Corporate Summary Report"
TODAY = datetime.now()


# define functions

def get_list_from_file(file):
    data_list = []
    with open(file, 'r') as f:
        all_lines = f.readlines()
        for one_line in all_lines:
            entry = one_line.split(',')
            data_list.append(entry)
    return data_list





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



##############################
# Summaries
##############################

def employee_overview():

    # get data from file
    employees = get_list_from_file(EmployeeFile)

    # initialize counters and accumulators
    num_employees = 0
    num_own_car = 0
    num_company_car = 0
    num_bal_due = 0
    city_dict = {}

    # calculate number of employees
    num_employees = len(employees)

    # calculate number of employees by city
    city_dict = {}
    for employee in employees:
        city = employee[4]
        if city in city_dict:
            city_dict[city] += 1
        else:
            city_dict[city] = 1

    # calulate number of drivers with own cars and company cars
    num_own_car = 0
    num_company_car = 0

    for employee in employees:
        if employee[-2] == 'Y':
            num_own_car += 1
        else:
            num_company_car += 1

    # calculate number of employees with balance owing
    num_bal_due = 0
    for employee in employees:
        if float(employee[-1]) > 0:
            num_bal_due += 1        


    # calculate employee metrics
    # Average Balance Due per Driver: $X,X

    balance_dict = {}
    for employee in employees:
        balance = employee[-1]
        if employee in balance_dict:
            balance_dict[balance] += 1
        else:
            balance_dict[balance] = 1

    print(balance_dict)
    # Top-Performing Drivers:
    # Driver 6: $XX,
    # Driver 5: $XX,
    # Driver 4: $XX,



    # display results
    print("\nEmployee Overview\n")
    print(f"Total Number of Employees: {num_employees}")
    print(f"Drivers with Own Cars: {num_own_car}")
    print(f"Drivers Using Company Cars: {num_company_car}")
    print(f"Employees with balance owing: {num_bal_due}")
    print("Employees by City:")
    for city, count in city_dict.items():
        print(f"    {city}: {count}")

    #return num_employees, num_own_car, num_company_car, num_bal_due, city_dict


def revenue_overview():
    # get data from files
    revenues = get_list_from_file(RevenuesFile)

    # initialize counters and accumulators
    total_revenue = 0
    total_hst = 0
    revenue_by_driver = {}
    monthly_stand_fees = 0
    rental_fees = 0

    for revenue_info in revenues:
        total_revenue += float(revenue_info[-1])
        total_hst += float(revenue_info[-2])
        if revenue_info[2] == 'monthly stand fee'.strip().lower():
            monthly_stand_fees += float(revenue_info[4])
        if 'Rental Fee' in revenue_info[2]:
            rental_fees += float(revenue_info[4])
        driver = revenue_info[0]
        if driver in revenue_by_driver:
            revenue_by_driver[driver] += float(revenue_info[-1])
        else:
            revenue_by_driver[driver] = float(revenue_info[-1])

    # display results
    print("\nFinancial Overview: Revenues\n")
    print(f"Total Revenue: ${total_revenue}")
    print(f"Total HST Collected: ${total_hst}")
    print("Revenue Breakdown by Driver:")
    for driver, revenue in revenue_by_driver.items():
        print(f"    {driver}: ${revenue}")
    print(f"Monthly Stand Fees: ${monthly_stand_fees}")
    print(f"Rental Fees: ${rental_fees}")
    return total_revenue


def expense_overview():
    # get data from files
    expenses = get_list_from_file(ExpensesFile)

    # initialize counters and accumulators
    total_expenses = 0
    total_hst = 0
    expenses_by_category = {}


    # calculate total expenses, total HST, and expenses by category
    for expense_info in expenses:
        total_expenses += float(expense_info[-1])
        total_hst += float(expense_info[-2])
        category = expense_info[2]
        if category in expenses_by_category:
            expenses_by_category[category] += float(expense_info[-1])
        else:
            expenses_by_category[category] = float(expense_info[-1])

    # display results
    print("\nFinancial Overview: Expenses\n")
    print(f"Total Expenses: ${total_expenses}")
    print(f"Total HST on Expenses: ${total_hst}")
    print("Expenses Breakdown by Category:")
    for category, total in expenses_by_category.items():
        print(f"    {category}: ${total}")

    print("\n***** should we also add avg maintenance cost per car, and who was greatly above or below? *****")
    return total_expenses


def get_net_profit(profit, cost):

    print("\nNet Profit/Loss:\n")
    net_profit = profit - cost
    print(f"Total Revenue: ${profit}")
    print(f"Total Expenses: ${cost}")
    print(f"Net Profit: ${net_profit}")

    return net_profit

##############################
# Detailed Metrics
##############################

#

########################
# Main program
########################


def generate_report():
    # Generate Report
    # Report Generated On: 2024-08-07
    # Report Generated By: John Doe
    # Report Saved As: Corporate_Summary_Report_2024-08-07.txt


    # HAB Taxi Services Corporate Summary Report
    # Executive Summary
    # [text in here maybe?]


    print_header(HeaderMsg)
    print("\nWelcome to HAB Taxi's Summary Report.")
    print("Please provide the following information to do stuff\n")


    overview = employee_overview
    print(overview)

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
    print(f"{title:^{width}}").upper()
    print(f"{'-' * width}")
    print()

if __name__ == "__main__":
    #generate_report()
    print_header(HeaderMsg, 80)
