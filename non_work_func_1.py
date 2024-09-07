# Find the first digit 
def leading_zero_check(n) : 
    """Checks for leading zero."""
    first = n[0]
    if first == "0":
        print("It's False")
        return False
    else:
        print("It's True")
        return True

leading_zero_check("1000000")