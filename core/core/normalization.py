from re import sub, match


def normalize_phone(phone):
    # Remove non-digit characters
    cleaned_phone = sub(r'\D', '', str(phone))

    # Check if the cleaned phone number is numeric and has a valid length
    if match(r'^\d{10}$', cleaned_phone):
        # Check for 10-digit number starting with 9
        if cleaned_phone[0] == '9' and cleaned_phone[0] != '0':
            # Assign the phoneNumber attribute with a leading 0
            return '0' + cleaned_phone
    elif match(r'^\d{11}$', cleaned_phone):
        # Check for 11-digit number starting with 09
        if cleaned_phone[0] == '0' and cleaned_phone[1] == '9':
            # Assign the phoneNumber attribute
            return cleaned_phone
    else:
        return None


if __name__ == '__main__':
    print(normalize_phone('9999999999'))



