### import datetime


def input_check(date, time, description, amount, payment_method, merchant_name, location, recurring):
    check_list = []


    ### Date check
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
            check_list.append(date_check)
    elif len(date) == 4:
        month = date[:2]
        day = date[2:]
        if month.isdigit() == True and day.isdigit == True:
            pass
        else:
            date_check = False
            check_list.append(date_check)
    else:
        date_check = False
        check_list.append(date_check)
        
    check_list.append(date_check)


    ### time_check   FORMAT | 01:01p 
    time_check = True
    
    if len(time) != 6:       ### Remove to make input easier
        time_check = False
    elif time[:1].isdigit() == False and time[2:4].isdigit() == False:
        time_check = False
    elif time[2] != ':':      ### Remove to make input easier
        time_check = False
    elif not time[5] == 'p' and not time[5] == 'a':   
        time_check = False


    check_list.append(time_check)


    ### description
    description_check = True

    description = str(description)
    
    check_list.append(description_check)

    ### amount_check
    amount_check = True

    try: 
        int(amount)
        check_list.append(amount_check)
    except Exception:
        print(Exception)

    return check_list

    ### payment_method
    

print(input_check("02/01", "06:34a", "1", "101", "1", "!", "1", "True"))

def main(date, time, description, amount, payment_method, merchant_name, location, recurring):
    pass
