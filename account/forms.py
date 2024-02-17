from re import match, sub
from django import forms
from jdatetime import datetime

# function from account-logic
from .accountinglogic.mainlogic.existence import is_user_exist
from .accountinglogic.mainlogic.validation import passwd_validation


class LoginForm(forms.Form):
    email = forms.CharField(required=True)
    passwd = forms.CharField(required=True)
    login_remember = forms.BooleanField(required=False)

    # def clean_user_name(self):
    #     usr_name = self.cleaned_data.get('user_name')
    #     is_user_exist = User.objects.filter(username=usr_name).exists()
    #     if not is_user_exist:
    #         raise forms.ValidationError('کاربری با این مشخصات ثبت نام نکرده است!')
    #     else:
    #         return usr_name


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    confirm_passwd = forms.CharField(max_length=50, required=True)
    passwd_confirmed = forms.BooleanField(required=True)
    passwd = forms.CharField(max_length=50, required=True)
    gender = forms.CharField(max_length=5, required=True)
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    phone_number = forms.CharField(max_length=11, required=True)
    birth_date = forms.DateField(required=False)
    privacy_accepted = forms.BooleanField(required=True)

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        regex = r'^[A-Za-z\s]+$'
        if match(regex, first_name):
            return first_name
        else:
            return forms.ValidationError('error, the first name is not valid')

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        first_name = self.cleaned_data.get('first_name')
        if last_name == first_name:
            raise forms.ValidationError('نام و نام خانوادگی یکسان است!')
        else:
            regex = r'^[A-Za-z\s]+$'
            if match(regex, last_name):
                return last_name
            else:
                return forms.ValidationError('error, the last name is not valid')

    def clean_email_address(self):
        email_address = self.cleaned_data.get('email_address')
        if is_user_exist(email_address):
            raise forms.ValidationError('این آدرس ایمیل قبلا ثبت شده است.')
        else:
            return email_address

    def clean_passwd(self):
        passwd = self.cleaned_data.get('passwd')
        confirm_passwd = self.cleaned_data.get('confirm_passwd')
        passwd_confirmed = self.cleaned_data.get('passwd_confirmed')
        if str(passwd_confirmed).lower() == 'true':
            result = passwd_validation(passwd, confirm_passwd)
            if result['value'] == 0:
                return passwd
            else:
                raise forms.ValidationError(result['error'])
        else:
            return forms.ValidationError('Internal error, please try again.')

    def clean_gender(self):
        gender = self.cleaned_data['gender']
        if gender in ['male', 'female', 'other']:
            return gender[0].upper()
        else:
            return forms.ValidationError('error, the gender you entered is not valid')

    # -----------------
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        # Remove non-digit characters
        cleaned_phone_number = sub(r'\D', '', phone_number)

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
            return forms.ValidationError('error, Invalid phone number')

    def clean_birth_date(self):
        birth_date = self.cleaned_data.get('birth_date')
        if birth_date:
            # Parse the date string
            parsed_date = datetime.strptime(birth_date, '%Y-%m-%d')
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
                    return forms.ValidationError('error, you don\'t have minimum age')
            else:
                return forms.ValidationError('error, Invalid birth date')
        else:
            return False

    def clean_privacy(self):
        privacy_accepted = self.cleaned_data.get('privacy_accepted')
        # Check if the checked parameter is a boolean
        if privacy_accepted:
            # Assign the privacy attribute
            return privacy_accepted
        else:
            return forms.ValidationError('error, you should accept our rules')

