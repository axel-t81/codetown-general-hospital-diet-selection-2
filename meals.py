#!/usr/bin/env python3
"""
This module TO UPDATE... takes patient nutrional info from hospital staff.
TO UDATE ....It then calculates the average protein, carbohydrates, fat, and kilojoules for all patients.
"""
# Program Details
__author__ = "Axel Tracy"
__version__ = "0.1.0"

# Import Statements
import math 
import os

# Initialise global variables and dictionaries used in program
cwd = os.getcwd()
line = "*"
# justify = " "
normal_diet = {
    "protein": 32.5,
    "carbohydrates": 60.0,
    "fat": 40.86
}

oncology_diet = {
    "protein": 35.0,
    "carbohydrates": 52.5,
    "fat": 37.63
}

cardiology_diet = {
    "protein": 32.5,
    "carbohydrates": 30.0,
    "fat": 26.88
}

diabetes_diet = {
    "protein": 20.0,
    "carbohydrates": 27.5,
    "fat": 27.95
}

kidney_diet = {
    "protein": 15.0,
    "carbohydrates": 55.0,
    "fat": 23.65
}

# A function to collect valid input for nutritional macro data.
# This function validates input to confirm (a) it is a number that fits the requirements of a float, and (b) that it is non-negative.
def non_negative_only(prompt):
    """Validate patient number input."""
    while True:
        try:
            value = float(input(prompt))
        except:
            print("\nSorry, I didn't understand your input. Let's try again, using a whole number or one with decimal places, as your input please.")
            continue

        if value < 0:
            print("\nSorry, the amount must be a non-negative number. Please try again.")
            continue
        else:
            break
    return value

def valid_patient_id(prompt):
    patient_id = input(prompt)

# Find the first digit 
#def first_digit_calc(first_digit) : 
#    """Returns first digit of Patient ID."""
#    # Remove last digit from number till only one digit is left 
#    while first_digit >= 10:  
#        first_digit = first_digit / 10; 
#      
#    # return the first digit 
#    return int(first_digit) 

## A function to collect valid input for patients numbers.
## This function validates input to confirm (a) it is an integer to count people, and (b) that it is positive and above zero.
#def valid_patient_id(prompt):
#    """Validate the Patient ID input."""
#    while True:
#        try:
#            value = int(input(prompt))
#        except:
#            print("\nSorry, I didn't understand your input. Let's try again, using a whole number for the Patient ID, as your input please.")
#            continue

##### UP TO HERE: Cannot get 0 validation to work.
#        first_digit = prompt[0] 
#        if first_digit == "0":
#            print("\nSorry, the Patient ID cannot start with 0. Please try again.")
#            continue
#        elif int(math.log10(value)+1) != 6:
#            print("\nSorry, the Patient ID must be 6 numbers. Please try again.")
#            continue
#        else:
#            break
#    return value


### UP TO HERE: NEED TO STUDY (a) Dictionaries (b) Functions
#def choose_diet(protein, carbohydrates, fat)
#    pass

def calculate_error(diet, requirements):
    pro_diet = diet["protein"]
    pro_req = requirements["protein"]
    pro_error = abs(pro_diet - pro_req)

    carb_diet = diet["carbohydrates"]
    carb_req = requirements["carbohydrates"]
    carb_error = abs(carb_diet - carb_req)

    fat_diet = diet["fat"]
    fat_req = requirements["fat"]
    fat_error = abs(fat_diet - fat_req)

    total_error = (pro_error + carb_error + fat_error)
    return total_error

def choose_diet(protein, carbohydrates, fat):
    patient_diet = {
        "protein": protein,
        "carbohydrates" : carbohydrates,
        "fat": fat
        }
    error_dict = {}
    error_dict["Normal"] = calculate_error(normal_diet, patient_diet)
    error_dict["Oncology"] = calculate_error(oncology_diet, patient_diet)
    error_dict["Cardilogy"] = calculate_error(cardiology_diet, patient_diet)
    error_dict["Diabetes"] = calculate_error(diabetes_diet, patient_diet)
    error_dict["Kidney"] = calculate_error(kidney_diet, patient_diet)
    print(error_dict)

    temp = min(error_dict.values())
    print(temp)

    key_list = list(error_dict.keys())
    val_list = list(error_dict.values())
    lowest_error_diet = val_list.index(temp)
    lowest_error_diet_key = (key_list[lowest_error_diet])
    print(lowest_error_diet_key)

    return lowest_error_diet_key




# The main function; guarded by the meals.py script entry point below.
def main():
    ### YES, HAS BEEN UPDATED AND/OR CONFIRMED STILL HOLDS
    """Main entry point of program."""
    # For UI and user-friendliness, provide feedback to user of program start/entry point.
    print("\n" + line*100)
    print("WELCOME TO THE CODETOWN GENERAL HOSPITAL NUTRITION-BASED DIET SELECTION SYSTEM:")
    print(line*100 + "\n")

    # Requirement 1: "Your program should start by asking for the patient id (which is a six-digit positive integer with no leading zeroes)"
    # This uses the function above to return a six-digit integer to the variable
    patient_id = valid_patient_id("\nPlease enter the Patient ID: ")

    # For UI and user-friendliness, provide feedback and guidance to user of where they are in the program.
    print("\n\nPATIENT NUTRITION COLLECTION:")

    # Requirement 2: "your program must ask for the amount of protein, carbohydrates, and fat required by that patient (which must all be non-negative numbers)."

    # This uses the function above to return an float to the variable
    protein = non_negative_only("\nHow many grams of protein is required for the patient with ID " + patient_id + "? ")

    carbohydrates = non_negative_only("\nHow many grams of carbohydrates are required for the patient with ID " + patient_id + "? ")

    fat = non_negative_only("\nHow many grams of fat is required for the patient with ID " + patient_id + "? ")


    diet_data = choose_diet(protein, carbohydrates, fat)

    file_contents = f"{patient_id},{diet_data}\n"

    with open(os.path.join(cwd, 'meals.csv'), 'a') as file:
        file.write(file_contents)

    # Final out to provide feedback to user, and confirm the program is complete, and they can safely shut down.
    print("\n" + line*100)
    print("THE SYSTEM IS NOW COMPLETE: YOUR PATIENTS' NUTRITION-BASED DIET SELECTIONS HAVE BEEN MADE.\nTHESE DIETS HAVE BEEN SENT TO THE KITCHEN VIA A CSV FILE.\nPLEASE CLOSE THIS PROGRAM OR RUN AGAIN. THANK YOU.")
    print(line*100 + "\n")


# This is the entry point of the meals.py program/script.
# This code in this conditional statement runs when executed as a script from the command line; the file object passing to the interpreter evaluates as True.
# But this code will not run when functions are imported via a module; only the function would be used externally.
if __name__ == "__main__":
    """This is executed when run as a script from the command line."""
    main()







### FROM PROGASSIGN1
# References:
# * https://www.python-boilerplate.com/py3+executable - For boilerplate code to start with.
# * https://www.w3schools.com/python/ - Guidance on using in-built Python functions.
# * https://www.geeksforgeeks.org/ - Guidance on using in-built Python functions.
# * https://stackoverflow.com/questions/1995615/how-can-i-format-a-decimal-to-always-show-2-decimal-places - Guidance to learn about f-strings.
# * https://chatgpt.com/c/89aff71f-f728-4fdb-96c1-9e5930a845a6 - Guidance to find out why my original input validation had false negative errors in testing.
# * https://realpython.com/if-name-main-python/ - Guidance to learn about the if-name-main conditional statement, and why programs are set up this way.
# * https://www.britannica.com/topic/large-numbers-1765137 - Guidance when working out how to setup the right_align function.
# * https://packaging.python.org/en/latest/guides/making-a-pypi-friendly-readme/ - For guidance with the README.md file

