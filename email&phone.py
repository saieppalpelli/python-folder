

import re
def validate_phone_number(phone_number):

    phone_pattern = r'^[6-9]\d{9}$'
    if re.match(phone_pattern, phone_number):
        return True
    else:
        return False
def validate_email(email):

    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(email_pattern, email):
        return True
    else:
        return False
phone_number = input("Enter your phone number: ")
if validate_phone_number(phone_number):
    print("Phone number is valid.")
else:
    print("Invalid phone number format.")
email = input("Enter your email address: ")
if validate_email(email):
    print("Email address is valid.")
else:
    print("Invalid email address format.")