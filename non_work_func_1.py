# Find the first digit 
def first_digit_calc(first_digit) : 
    """Returns first digit of Patient ID."""
    # Remove last digit from number till only one digit is left 
    while first_digit >= 10:  
        first_digit = first_digit / 10; 
      
    # return the first digit 
    return int(first_digit) 