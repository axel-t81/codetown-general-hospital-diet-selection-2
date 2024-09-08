import math

def positive_int_only(prompt):
    """Validate the nutritional macro input."""
    while True:
        first = prompt[0]
        try:
            value = int(input(prompt))
        except:
            print("\nSorry, I didn't understand your input. Let's try again, using numbers for your Patient ID, as your input please.")
            continue
        if value < 1:
            print("\nSorry, the Patient ID must be a positive number. Please try again.")
            continue
        ## The two tests above are working well
        ## But the two below are not
        elif first == "0":
            print("\nSorry, the Patient ID provided starts with 0; which is invalid. Please input the Patient ID, again.")
            print("Value is", value, "Leading Zero Check")
            print("First is", first, "Leading Zero Check")
            continue
        elif math.log10((value)+1) != 6:
            print("\nSorry, the Patient ID must be 6 numbers. Please try again.")
            print("Value is", value, "math check")
            print("First is", first, "math Check")
            continue
        else:
            break
    return value

prompt = positive_int_only("Please enter Patient ID: ")