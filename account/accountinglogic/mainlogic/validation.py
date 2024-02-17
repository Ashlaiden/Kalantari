from copy import copy
from core.options.main import options


# validation function

def passwd_validation(passwd, confirm_passwd):
    error = options.errors
    validation = 0
    if passwd != confirm_passwd and options.errors_type['1']:
        return {'value': validation + 1, 'error': error['1']}
    else:
        if len(str(passwd)) < 8 and options.errors_type['2']:
            return {'value': validation + 2, 'error': error['2']}
        else:
            num = 0
            char = 0
            lowe = 0
            upper = 0
            asci = 0
            none = 0
            for _ in str(passwd):
                if _.isnumeric():
                    num += 1
                elif _.isalpha():
                    char += 1
                    if _.islower():
                        lowe += 1
                    elif _.isupper():
                        upper += 1
                elif _.isascii():
                    asci += 1
                else:
                    none += 1
            if num == 0 and options.errors_type['3']:
                return {'value': validation + 3, 'error': error['3']}
            elif char == 0 and options.errors_type['4']:
                return {'value': validation + 4, 'error': error['4']}
            elif lowe == 0 and options.errors_type['5']:
                return {'value': validation + 5, 'error': error['5']}
            elif upper == 0 and options.errors_type['6']:
                return {'value': validation + 6, 'error': error['6']}
            elif asci == 0 and options.errors_type['7']:
                return {'value': validation + 7, 'error': error['7']}
            else:
                return {'value': validation, 'error': error['0']}


if __name__ == '__main__':
    # pasword = 'adF@546454'
    # confirm = copy(pasword)
    # confirm = 'adF@546454'
    # valid = passwd_is_not_valid(pasword, confirm)
    # print(valid)
    pass
