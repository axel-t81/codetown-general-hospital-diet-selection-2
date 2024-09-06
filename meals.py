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

# Initialise global variables used in program
line = "*"
protein = 0.00
carbohydrates = 0.00
fat = 0.00
# justify = " "

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


    
    ### YES, HAS BEEN UPDATED AND/OR CONFIRMED STILL HOLDS
    # Final out to provide feedback to user, and confirm the program is complete, and they can safely shut down.
    print("\n" + line*100)
    print("THE SYSTEM IS NOW COMPLETE: YOUR PATIENTS' NUTRIBUTION-BASED DIET SELECTIONS HAVE BEEN MADE.\nTHESE DIETS HAVE BEEN SENT TO THE KITCHEN VIA A CSV FILE.\nPLEASE CLOSE THIS PROGRAM OR RUN AGAIN. THANK YOU.")
    print(line*100 + "\n")


### YES, HAS BEEN UPDATED AND/OR CONFIRMED STILL HOLDS
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




# A function to format the averages output.
# The idea and template here was drawn from my submission to the Week 3 Assessable Tutorial, the 'Right Justify' problem.
# In short, there are three scenarios to this selection statement;
# 1) A standard number that is 12 digits or less, which should cover all cases in regards to the current nutrition use case,
# 2) A alternative option if there an extremely large number with 13 to 30 digits, which should be highly unlikely.
# 3) A final catch-all case, to tie up any number that isn't covered by the last two options.
# def right_align(input_string):
#    """Calculate the length of the input string and align string to the right."""
#    info = input_string
#    characters = len(info)
#    if characters <= 12:
#        blanks = 12 - characters
#        return (blanks*justify + info)
#    elif (12 < characters <= 30):
#        blanks = 30 - characters
#        return (blanks*justify + info)
#    else:
#        return info


## The main function; guarded by the diet.py script entry point below.
# def main():


## Calculating the average by summing List items to get a total for numerator; and using len() function to count items to use as denominator
    ## This is rounded to two decimal places to improve UI and user experience
    #protein_average_float = round(sum(all_protein) / len(all_protein),2)
    ## 1) Using the right_align function decribed earlier
    ## 2) Typecasting the float, the average, to a string so it can be used in string concatination
    ## 3) Using the f-string capabilities of Python to format the output to 2 decimal places
    #protein_average = right_align(str(f'{protein_average_float:.2f}'))
    ## The justify variable is used here by manually calculating the length of string to left and hardcoding into string; the goal of this is to have all strings of the average calculations in line with each other.
    ## Achieving this goals allow easier recognigtion of the size of each number, e.g. 1000 should be easily distinguishable vs 100.
    #print("Protein - The average protein over all patients is:" + justify*13 + protein_average + " grams")
    #
    #carbs_average_float = round(sum(all_carbs) / len(all_carbs),2)
    #carbs_average = right_align(str(f'{carbs_average_float:.2f}'))
    #print("Carbohydrates - The average carbohydrates over all patients is:" + justify*1 + carbs_average + " grams")
    #
    #fat_average_float = round(sum(all_fat) / len(all_fat),2)
    #fat_average = right_align(str(f'{fat_average_float:.2f}'))
    #print("Fat - The average fat over all patients is:" + justify*21 + fat_average + " grams")
    #
    #kjs_average_float = round(sum(all_kjs) / len(all_kjs),2)
    #kjs_average = right_align(str(f'{kjs_average_float:.2f}'))
    #print("Kilojoules - The average kilojoules over all patients is:" + justify*7 + kjs_average + " kJs\n")