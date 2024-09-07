import math

def leading_zero_check(n) : 
    """Checks for leading zero."""
    first = n[0]
    if first == "0":
        print("It's False")
        return False
    else:
        print("It's True")
        return True
    
# A function to collect valid input for patients numbers.
# This function validates input to confirm (a) it is an integer to count people, and (b) that it is positive and above zero.
def valid_id_1(prompt):
    """Validate the Patient ID input."""
    while True:
        try:
            value = int(input(prompt))
        except:
            print("\nSorry, I didn't understand your input. Let's try again, using a whole number for the Patient ID, as your input please.")
            continue
        return value

def valid_id_2(prompt):  

    y = valid_id_1(prompt)

    while True: 
        x = leading_zero_check(prompt)
        if x == False:
            print("\nSorry, the Patient ID cannot start with 0. Please try again.")
            continue
        elif int(math.log10(y)+1) != 6:
            print("\nSorry, the Patient ID must be 6 numbers. Please try again.")
            continue
        else:
            break


prompt = input("Please enter Patient ID: ")
valid_id_1(prompt)