import log_purchase
import settings


MODES = ['Log purchase', 'Log income', 'Card payment', 'Stats', 'Budget', 'Save up', 'Settings']


def list_modes():
    for i in range(len(MODES)):
        print(i, MODES[i])


def main():
    print('- Select one -')
    while True:
        list_modes()
        mode_input = ('')
        if mode_input == '0':
            log_purchase.main()
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
