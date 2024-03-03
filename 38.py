# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

# If the function is passed a valid PIN string, return true, else return false.

# Examples (Input --> Output)
# "1234"   -->  true
# "12345"  -->  false
# "a234"   -->  false

def validate_pin(pin):
    # Check if the length is 4 or 6 and if the pin contains only digits
    if (len(pin) == 4 or len(pin) == 6) and pin.isdigit():
        return True
    else:
        return False