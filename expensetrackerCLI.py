import log_purchase
import settings
import db_man


MODES = ['Log purchase', 'Log income', 'Card payment', 'Stats', 'Budget', 'Save up', 'Settings']


def first_screen():
    pass

def list_modes():
    for i in range(len(MODES)):
        print(i, MODES[i])


def log_purchase_mode():
    date = input('Date (mm/dd, today or yesterday): ')
    time = input('Time: ')
    description = input('Description: ')
    amount = input('Amount: ')
    paymethod = input('Payment method: ')
    merchant_name = input('Merchant name: ')
    location = input('Location: ')
    recurring = input('Recurring: ')

    paymethod_names = db_man.get_paymethod_names_out()
    
    data_safe = log_purchase.check_input(date, time, description, amount, paymethod, paymethod_names, merchant_name, location, recurring)

    print(data_safe)

    


def log_income_mode():
    pass


def create_user():    #Started as login became create_user
    def is_safe():
        ##TODO - Check if password is safe enough
        return True
    username = input('Enter Username: ')
    print('Enter Password')
    print('(Optional)')
    password = input('')

    if type(username) == str:
        pass
        if is_safe(password) == True:
            response = 0
    elif type(username) != str:
        response = 1
        print('Try again!')
    elif username == 'stop':  # Enter stop in username input to end program
        response = 2


    create_user_confirmation = input('Confirm? (yes/no) ')
    if create_user_confirmation == 'yes':
        db_man.create_user()
    elif create_user_creation == 'no':
        exit_or_stay = input('Close(0) or try again(1): ')
        if exit_or_stay == 0:
            response = 2
        elif exit_or_stay == 1:
            response == 1
     
        

    return username, password, response

def login():
    username = input('Enter Username: ')
    #password_ = db_man.get_password_existence()
    #if password_ == False:
        #pass
    #elif password_ == True:
        #pass
        #TODO - If password exists confirm password matches with username/account
    login = True
    return username, 0

    


def main(username):
    print(f'Welcome, {username}')
    print('- Select one -')
    while True:
        list_modes()
        mode_input = input('')
        if mode_input == '0':
            log_purchase_mode()
        elif mode_input == '1':
            #log_income.main()
            pass
        elif mode_input == '2':
            #card_payment.main()
            pass
        elif mode_input == '3':
            #important_stats.main()
            pass
        elif mode_input == '4':
            #set_budget.main()
            pass
        elif mode_input == '5':
            #save_up.main()
            pass
        elif mode_input == '6':
            settings.settings_main()
        elif mode_input == '69':
            #delete_db()
            pass
        elif mode_input == 'exit':
            break
        else:
            print('Try again!')


if __name__ == '__main__':
    print('Welcome to ExpenseTrackerCLI!!!')
    print('\n')
    login_or_signup = input('Login(0) or Signup(1) ')
    if int(login_or_signup) == 0:
        print('\n' * 100)
        while True:
            username, login = login()
            if login == 0:               # 0 - runs main function of CLI version
                print('\n' * 100)
                main(username)
                break
            elif login == 1:             # 1 - loops through login until different ending
                pass
            elif login == 2:             # 2 - Ends loop
                break
    elif int(login_or_signup) == 1:
        create_user()
        #TODO finish create user


