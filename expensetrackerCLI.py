import log_purchase
import settings
import db_man


MODES = ['Log purchase', 'Log income', 'Card payment', 'Stats', 'Budget', 'Save up', 'Settings']


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

    


def log_income_mode():
    pass


def main():
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
    main()
