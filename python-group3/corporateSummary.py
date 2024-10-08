
# Description: Corporate Summary Report
# Author Robot Group 3
# Date: 2024-Jul-31 to 2024-Aug-07

# import libraries

from datetime import datetime
import handlers.utility as util
import handlers.validation as val
import handlers.display as dsp
from financialReport import GenerateFinancialReport


# define global variables
EmployeeFile = 'python-group3/data_files/employees.dat'
ExpensesFile = 'python-group3/data_files/expenses.dat'
RevenuesFile = 'python-group3/data_files/revenues.dat'


HeaderMsg = "Corporate Summary Report"
TODAY = datetime.now()
TODAY_dsp = dsp.date_dsp(TODAY)


# define functions

def get_list_from_file(file):
    data_list = []
    with open(file, 'r') as f:
        all_lines = f.readlines()
        for one_line in all_lines:
            entry = one_line.split(',')
            data_list.append(entry)
    return data_list


def get_top_X(dictionary, num):
    num = int(num)
    topX = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True)[:num])
    return topX

def get_bottom_X(dictionary, num):
    bottomX = dict(sorted(dictionary.items(), key=lambda item: item[1])[:num])
    return bottomX


##############################
# Summaries
##############################

def print_employee_report():
    width = 86

    # initialize counters and accumulators
    num_employees = 0
    num_own_car = 0
    num_company_car = 0
    num_bal_due = 0

    ins_company_dict = {}
    city_dict = {}
    balance_dict = {}


    # get data from file
    employee_data = get_list_from_file(EmployeeFile)
    
    # calculate number of employees
    num_employees = len(employee_data)

    for line in employee_data:
        employee_ID = line[0].strip()
        city = line[4].strip()
        insurance_company = line[9].strip()
        own_car = line[-2].strip()
        balance = float(line[-1])


    # # calculate number of employees by city
    #     if city in city_dict:
    #         city_dict[city] += 1
    #     else:
    #         city_dict[city] = 1

    # calculate number of employees by insurance company
        if insurance_company in ins_company_dict:
            ins_company_dict[insurance_company] += 1
        else:
            ins_company_dict[insurance_company] = 1

    # calulate number of drivers with own cars and company cars

        if own_car == 'Y':
            num_own_car += 1
        else:
            num_company_car += 1

    # calculate number of employees with balance owing
        if balance > 0:
            num_bal_due += 1        


    # calculate employee metrics

        if employee_ID in balance_dict:
            balance_dict[employee_ID] += balance
        else:
            balance_dict[employee_ID] = balance

    # calculate average balance due
    avg_bal_due = sum(balance_dict.values()) / len(balance_dict)
    highest_bal_due = max(balance_dict.values())
    lowest_bal_due = min(balance_dict.values())
    top3_bal = get_top_X(balance_dict, 3)
    


    # display results
    print()
    print(f"{'=' * width}")
    print(f"{'Employee Summary Report':^{width}}")
    print(f"{'=' * width}")

    print()
    print(f"Total Number of Employees:   {num_employees}")
    print(f"Drivers with their Own Cars:  {num_own_car}")
    print(f"Drivers Using Company Cars:   {num_company_car}")
    print()
    print(f"Employees with balance owing: {num_bal_due}")
    print(f"    Average Balance Due: ${avg_bal_due:,.2f}")
    print(f"    Highest Balance Due: ${highest_bal_due:,.2f}")
    print(f"    Lowest Balance Due:  ${lowest_bal_due:,.2f}")

    #print("\nEmployees by City:")
    #for city, count in city_dict.items():
    #    print(f"    {city}: {count}")

    print("\nEmployees by Insurance Company:")
    for company, count in ins_company_dict.items():
        print(f"    {company:<20}: {count}")



    print("\nDrivers with highest balance:")
    for driver, balance in top3_bal.items():
        print(f"    Driver {driver}: ${balance:,.2f}")

    print()
    print(f"{'END OF REPORT':^{width}}\n\n")



########################
# Main program
########################


def generate_report():
    print()

    util.print_header(HeaderMsg, 86)
    print("\nWelcome to HAB Taxi's Corporate Summary Report.")
    print("\nThis program will first print an employee summary and then a financial summary.\n")

    go_on = input("Press Enter to continue...")
    print()
    print(f"{'Report Generated On:':<30} {TODAY_dsp}")
    print_employee_report()
    print("")

    go_on = input("Press Enter to continue for the next report...")
    print()
    print(f"{'Report Generated On:':<30} {TODAY_dsp}")
    GenerateFinancialReport("profit summary")

    print()
    


if __name__ == "__main__":
    generate_report()