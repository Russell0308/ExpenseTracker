### import datetime



def check_date(date):
    date_check = True

    if date == 'today' or date == 'Today':
        pass
    elif date == 'yesterday' or date == 'Yesterday':
        pass
    elif date[1] == '/' or date[2] == '/':
        month, day = date.split('/')
        if month.isdigit() == True and day.isdigit() == True:
            pass
        else:
            date_check = False
    elif len(date) == 4:
        month = date[:2]
        day = date[2:]
        if month.isdigit() == True and day.isdigit == True:
            pass
        else:
            date_check = False
    else:
        date_check = False
        
    return date_check


def check_time(time):
    time_check = True
    
    if len(time) != 6:       ### Remove to make input easier
        time_check = False
    elif time[:1].isdigit() == False and time[2:4].isdigit() == False:
        time_check = False
    elif time[2] != ':':      ### Remove to make input easier
        time_check = False
    elif not time[5] == 'p' and not time[5] == 'a':   
        time_check = False

    return time_check


def check_description(description):
    description_check = True

    description = str(description)
    
    return description_check


def check_amount(amount):
    amount_check = True

    try: 
        int(amount)
        return amount_check
    except Exception:
        print(Exception)


def check_paymethod(payment_method, names):
    paymethod_check = True

    for i in names:
        if i == payment_method:
            return paymethod_check
        else:
            paymethod_check = False
    return paymethod_check


def check_input(date, time, description, amount, payment_method, paymethod_names, merchant_name, location, recurring):
    check_list = []

    checked_date = check_date(date)
    check_list.append(checked_date)

    checked_time = check_time(time)
    check_list.append(checked_time)

    checked_description = check_description(description)
    check_list.append(checked_description)

    checked_amount = check_amount(amount)
    check_list.append(checked_amount)

    checked_paymethod = check_paymethod(payment_method, paymethod_names)
    check_list.append(checked_paymethod)

print(input_check("02/01", "06:34a", "1", "101", "1", "!", "1", "True"))

