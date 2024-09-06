# A function to collect valid input for patients numbers.
# This function validates input to confirm (a) it is an integer to count people, and (b) that it is positive and above zero.
def valid_patient_id(prompt):
    """Validate the Patient ID input."""
    while True:
        try:
            value = int(input(prompt))
        except:
            print("\nSorry, I didn't understand your input. Let's try again, using a whole number for the Patient ID, as your input please.")
            continue

#### UP TO HERE: Cannot get 0 validation to work.
        first_digit = prompt[0] 
        if first_digit == "0":
            print("\nSorry, the Patient ID cannot start with 0. Please try again.")
            continue
        elif int(math.log10(value)+1) != 6:
            print("\nSorry, the Patient ID must be 6 numbers. Please try again.")
            continue
        else:
            break
    return value