# Description: Menu options for sprint programs
# Author Robot Group 3
# Date: 2024-Jul-31 to 2024-Aug-07


# import libraries
from handlers.utility import clear_screen
from financialReport import GenerateFinancialReport
from HABEmployee import create_new_account

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


############################################################################################################
# Define Menu Functions
############################################################################################################


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
        print_header("", 80)

        
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
            GenerateFinancialReport("profit")
        elif choice == '7':
            clear_screen()
            print_driver_listing()
        elif choice == '8':
            clear_screen()
            generate_summary_report()
        elif choice == '9':
            print()
            print("Thanks for using our services!")
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
