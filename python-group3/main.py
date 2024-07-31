# Description: Menu options for sprint programs
# Author Robot Group 3
# Date: 2024-Jul-31 to 


# import libraries
from datetime import datetime
import time
from utility_module import clear_screen

#define constants:
MENU = """
    ==========================================
     *          HAB Taxi Services           *
             Company Services System
    ==========================================

        
       1. Enter a New Employee (driver)
       2. Enter Comapny Revenues 
       3. Enter Company Expenses
       4. Track Car Rentals
       5. Record Employee Payment
       6. Print Company Profit Listing
       7. Print Driver Financial Listing
       8. Coroporate Summary Report
       9. Quit Program

        
    ==========================================
    """

############################################################################################################
# Define Menu Functions
############################################################################################################


def create_new_account():
    new_account = "This will be employee info"

    return new_account

def update_revenues():
    new_revenue = "This will be revenue info"

    return new_revenue

def update_expenses():
    new_expense = "This will be expense info"

    return new_expense

def track_rentals():
    rental_info = "This will be rental info"

    return rental_info

def record_employee_payment():
    employee_payment = "This will be employee payment info"

    return employee_payment

def print_profit_listing():
    profit_list = "This will be profit listing"

    return profit_list

def print_driver_listing():
    driver_list = "This will be driver listing"

    return driver_list

def generate_summary_report():
    summary_report = "This will be a summary report"

    return summary_report




############################################################################################################
# Define Main Function
############################################################################################################


# Main Program
def menu():
    
    while True:
        clear_screen()
        print(MENU)

    # User inputs        
        choice = input("\nEnter the number of the program would you like to run: ").strip()

    # Calculations (function selector)    
        if choice == '1':
            clear_screen()
            create_new_account()
        elif choice == '2':
            clear_screen()
            update_revenues()
        elif choice == '3':
            clear_screen()
            update_expenses()
        elif choice == '4':
            clear_screen()
            track_rentals()
        elif choice == '5':
            clear_screen()
            record_employee_payment()
        elif choice == '6':
            clear_screen()
            print_profit_listing()
        elif choice == '7':
            clear_screen()
            print_driver_listing()
        elif choice == '8':
            clear_screen()
            generate_summary_report()
        elif choice == '9':
            print()
            print("Thanks for playing!")
            print()
            break
        else:
            print("Invalid choice. Please enter a number 1 to 9.")
        

    # Housekeeping
        print()
        print()
        go_on = input("\nWould you like to run another program (Y/N)  ").lower().strip()
        if go_on == "n" or go_on == "no":
            print()
            print("Have a great day!")
            print()
            print()
            break


if __name__ == "__main__":
    menu()
