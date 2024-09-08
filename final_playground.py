def valid_patient_id(prompt):
    while True:
        leading_zeros = len(prompt.split('1', 1)[0])
        value_string = str(input(prompt))
        if leading_zeros > 0:
            print("\nSorry, the Patient ID provided starts with 0; which is invalid. Please input the Patient ID, again.")
            continue
        else:
            break
    return value_string

test = input("Enter data here: ")
valid_patient_id(test)


#elif len(prompt) != 6:
        #    print("\nSorry, the Patient ID must be 6 numbers. Please try again.")
        #    continue