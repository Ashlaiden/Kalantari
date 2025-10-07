from re import sub, match

def normalize_phone(phone):
    s = str(phone).strip()

    # keep leading + if present, otherwise only digits
    if s.startswith('+'):
        cleaned = sub(r'[^\d+]', '', s)   # keep '+' and digits
    else:
        cleaned = sub(r'\D', '', s)       # only digits

    # Case: already +<country><rest>, e.g. +989123456789
    if match(r'^\+\d{1,3}9\d{9}$', cleaned):
        return cleaned

    # Case: starts with 00 like 00989123456789 -> convert to +...
    if cleaned.startswith('00') and match(r'^00\d{11,12}$', cleaned):
        fixed = '+' + cleaned[2:]
        if match(r'^\+\d{1,3}9\d{9}$', fixed):
            return fixed

    # Case: starts with country code without +, e.g. 989123456789
    if match(r'^\d{12}$', cleaned) and cleaned.startswith('98') and cleaned[2] == '9':
        return '+' + cleaned

    # Case: 11 digits starting with 09 -> local format -> convert to +98...
    if match(r'^09\d{9}$', cleaned):
        return '+98' + cleaned[1:]

    # Case: 10 digits starting with 9 -> like 9123456789 -> convert to +98...
    if match(r'^9\d{9}$', cleaned):
        return '+98' + cleaned

    # not a supported/valid form
    return None


if __name__ == '__main__':
    tests = [
        '+989123456789',
        '00989123456789',
        '989123456789',
        '09123456789',
        '9123456789',
        'some garbage',
    ]
    for t in tests:
        print(t, '->', normalize_phone(t))
