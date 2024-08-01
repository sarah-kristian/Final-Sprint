# utility_module.py

# Description: Library of utility functions
# Author: Sarah Perry

import os
import time

# Clear the screen
def clear_screen():
    os.system('clear')

# Get the last ID from a file
def get_last_id(file_path, default_id):
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            if lines:
                last_line = lines[-1]
                last_id = int(last_line.split(",")[0].strip())
                return last_id
            else:
                return default_id          
    except FileNotFoundError:
        return default_id
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return default_id

# Generate progress indicator
def progress_dots(prompt):
    total_iterations = 10 # The more iterations, the more time is takes.
    print("")
    print(f"{prompt}...", end="")
    for _ in range(total_iterations):
        time.sleep(0.3)  # Simulate a delay
        print(".", end="", flush=True)  # Print a dot and flush the output buffer
    print("\n")  


# Check if the password is correct
def check_password(password):
    password_attempt = 0
    while True:
        password_attempt += 1
        password_check = input("Password: ")  
        if password_check == password:
            print("\nLogin successful!")
            break
        elif password_attempt in [1,2]:
            print(f" ** Incorrect password. Please try again. You have {4-password_attempt} attempts remaining.")
        elif password_attempt == 3:
            print(f" ** Incorrect password. Please try again. You have 1 attempt remaining.")
        else:
            exit(" ** Too many attempts. Please contact customer service.")

