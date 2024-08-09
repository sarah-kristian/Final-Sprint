# Description: Menu options for sprint programs
# Author Robot Group 3
# Date: 2024-Jul-31 to 2024-Aug-07


# import libraries
from handlers.utility import clear_screen, print_header
from financialReport import GenerateFinancialReport
from HABEmployee import create_new_account
from corporateSummary import generate_report

# define funtions
def draw_car():
    car = (f"""
             ______
            /|_||_\\`.__
           (   _    _ _\\
    hjw     =`-(_)--(_)-'

        """)
    print(car)
    


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





############################################################################################################
# Define Main Function
############################################################################################################


# Main Program
def menu():

    # define header & menu options
    width = 56
    header_msg = '*       Company Services Menu       *'
    option1 = 'Enter a New Employee (driver)'
    option2 = 'Enter Comapny Revenues'
    option3 = 'Enter Company Expenses'
    option4 = 'Track Car Rentals'
    option5 = 'Record Employee Payment'
    option6 = 'Print Company Profit Listing'
    option7 = 'Print Driver Financial Listing'
    option8 = 'Coroporate Summary Report'
    option9 = 'Quit Program'

    options = [option1, option2, option3, option4, option5, option6, option7, option8, option9]


    footer_line = f"{'-' * width}"

# main loop starts here
    while True:
        clear_screen()
    # initialize variables
        opt_num = 0
    # Display Menu
        print_header(header_msg, width)
        for option in options:
            opt_num += 1
            print(f"{' '*10}{opt_num}. {option}")
        print()
        print(footer_line)


    # User inputs        
        choice = input("\nWhich menu option would you like to run (1-9)?: ").strip()

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
            generate_report()
        elif choice == '9':
            print()
            print("Thanks for using our services!")
            draw_car()
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
            print("         Have a great day!")
            draw_car()

            print()
            print()
            break


if __name__ == "__main__":
    menu()
