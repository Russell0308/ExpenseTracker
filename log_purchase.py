import main
import datetime


def input_check(date, time, description, amount, payment_method, merchant_name, location, recurring):
    if date == 'today' or date == 'Today':
        pass
    elif date == 'yesterday' or date == 'Yesterday':
        pass
    elif date[1] == '/' or date[2] == '/':
        month, day = date.split('/')
        if month.isdigit() == True and day.isdigit() == True:
            pass
        else:
            return False
    elif len(date) == 4:
        month = date[:2]
        day = date[2:]
        if month.isdigit() == True and day.isdigit == True:
            pass
        else:
            return False
    else:
        return False
    return True
    

print(input_check("02/01", "1", "1", "1", "1", "!", "1", "True"))

def main(date, time, description, amount, payment_method, merchant_name, location, recurring):
    pass
