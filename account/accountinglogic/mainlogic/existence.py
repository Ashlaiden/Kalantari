from account.models import Account


# existence function
def is_user_exist(email_address=None):
    if email_address:
        user_exist = Account.objects.get(email=email_address).exists()
        if user_exist:
            return True
        else:
            return False
    else:
        return False
