# Using regular expression module from Standard Library
import re

""" EMAIL VALIDATION """

user_email = input('Enter your email: ')

def validate_email(user_email):
    # regex expression to use
    reg = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    # compile regex into pattern
    pattern = re.compile(reg)

    # using pattern to search the input string and validating condition
    if pattern.search(user_email):
        return 'Email is valid.'
    else:
        return 'Email is not valid. Try again!'

print(validate_email(user_email))


""" PASSWORD VALIDATION """

user_pass = input('Enter your password: ')

def validate_pass(user_pass):
    # regex expression to use
    # {8,20} at the end of "reg" means password has to be 6-20 characters long
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,20}$"
    # compile regex into pattern
    pattern = re.compile(reg)
    # using pattern to search the input string
    user_pass_check = (pattern.search(user_pass))
    #validating condition
    if user_pass_check:
        return 'Password is valid.'
    else:
        return 'Password is not valid. Try again!'

print(validate_pass(user_pass))
