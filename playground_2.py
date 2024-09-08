def valid_patient_int(prompt):
    while True:
        try:
            value = int(input(prompt))
        except:
            print("\nSorry, I didn't understand your input. Let's try again, using numbers for your Patient ID, as your input please.")
            continue
        if value < 1:
            print("\nSorry, the Patient ID must be a positive number. Please try again.")
            continue
        else:
            break
    return value

patient = valid_patient_int("Test data: ")
print(value)