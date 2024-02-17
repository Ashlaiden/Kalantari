from re import match, sub

from jdatetime import datetime

# from account.accountinglogic.mainlogic.existence import is_user_exist
from account.accountinglogic.mainlogic.validation import passwd_is_not_valid


def clean_first_name(first_name):
    regex = r'^[A-Za-z\s]+$'
    if match(regex, str(first_name)):
        return first_name
    else:
        return 'Enter a valid first name'

def clean_last_name(last_name, first_name):
    if last_name == first_name:
        raise 'Please enter your last name'
    else:
        regex = r'^[A-Za-z\s]+$'
        if match(regex, last_name):
            return last_name
        else:
            return 'Enter a valid last name'

# def clean_email_address(email_address):
#     if is_user_exist(email_address):
#         raise 'Email address is already exist'
#     else:
#         return email_address

def clean_passwd(passwd, confirm_passwd, passwd_confirmed):
    if passwd_confirmed:
        result = passwd_is_not_valid(passwd, confirm_passwd)
        if result['value'] == 0:
            return passwd
        else:
            raise 'Password is not valid. Please'
    else:
        return 'Internal error, please try again.'

def clean_gender(gender):
    if gender in ['male', 'female', 'other']:
        return gender[0].upper()
    else:
        return 'error, the gender you entered is not valid'

# -----------------
def clean_phone_number(phone_number):
    # Remove non-digit characters
    cleaned_phone_number = sub(r'\D', '', str(phone_number))

    # Check if the cleaned phone number is numeric and has a valid length
    if match(r'^\d{10}$', cleaned_phone_number):
        # Check for 10-digit number starting with 9
        if cleaned_phone_number[0] == '9' and cleaned_phone_number[0] != '0':
            # Assign the phoneNumber attribute with a leading 0
            return '0' + cleaned_phone_number
    elif match(r'^\d{11}$', cleaned_phone_number):
        # Check for 11-digit number starting with 09
        if cleaned_phone_number[0] == '0' and cleaned_phone_number[1] == '9':
            # Assign the phoneNumber attribute
            return cleaned_phone_number
    else:
        return 'error, Invalid phone number'


def clean_birth_date(birth_date):
    if birth_date:
        # Parse the date string
        parsed_date = datetime.strptime(birth_date, '%Y/%m/%d')
        # Get the minimum age
        min_age = 18

        # Check if the parsed date is valid
        if parsed_date:
            # Get the current year
            current_year = datetime.now().year
            # Calculate the minimum birth year
            min_birth_year = current_year - min_age
            # Get the year from the parsed date
            year = parsed_date.year
            # Check if the year is less than or equal to the minimum birth year
            if year <= min_birth_year:
                # Assign the birthday attribute
                return parsed_date
            else:
                return 'error, you don\'t have minimum age'
        else:
            return 'error, Invalid birth date'
    else:
        return None


def clean_privacy(privacy_accepted):
    # Check if the checked parameter is a boolean
    if privacy_accepted:
        # Assign the privacy attribute
        return privacy_accepted
    else:
        return 'error, you should accept our rules'


if __name__ == '__main__':
    print(clean_birth_date('1359/8/2'))



