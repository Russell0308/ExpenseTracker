import queries as q
import to_db 

lis_of_settings = ['Bank Accounts', 'Credit/Debit Card Accounts']


def settings_main():
    #main.post_login()
    print('\n' * 100)
    print('- Select one -')
    for i in range(len(lis_of_settings)):
        print(i, lis_of_settings[i])
    while True:
        setting_input = input('')
        if setting_input == '0':
            bank_account_settings()
            break
        elif setting_input == '1':
            paymethod_settings()
            break
        elif setting_input == '2':
            pass
        elif setting_input == '3':
            pass
        elif setting_input == '4':
            pass
        elif setting_input == '5':
            pass
        elif setting_input == '6':
            pass
        elif setting_input == '7':
            pass
        elif setting_input == '8':
            pass
        elif setting_input == '9':
            pass
        elif setting_input == 'exit':
            break
        else:
            print('Try again!')


def log_purchase_settings():
    



def bank_account_settings():
    mode = input('(N)ew, (E)dit, (D)elete: ')
    if mode == 'N':                                     #NEW 
        def create_bank_account():
            bank_name = input("Enter your bank's name: ")
            account_type = input('Enter your account type: ')
            balance = input('Enter your current balance: ')
            return bank_name, account_type, balance


        def confirm_new_bank(bank_data):
            print("Bank name: ", bank_data[0])
            print("Account type: ", bank_data[1])
            print("Balance: ", bank_data[2])
            confirm_new_bank = input("Is this all correct? (y/n) ")
            if len(confirm_new_bank) == 1:
                return confirm_new_bank
            else:
                pass

        bank_data = create_bank_account()
        confirm_bank = confirm_new_bank(bank_data)
        if confirm_bank == 'y':
            main.insert_execute_query(q.insert_table_banks, bank_data)
        else:
            print("try again")

    elif mode == 'E':                                   #Edit
        edit_bank_d = (main.execute_query(q.select_all_bank))
        for i in range(len(edit_bank_d)):
            print(edit_bank_d[i][0], edit_bank_d[i][1], edit_bank_d[i][2], '-', edit_bank_d[i][3])
        account_edit = int(input('Which account would you like to edit? '))
        chng_id = account_edit
        manual_edit = input('(N)ame, (T)ype, or (B)alance: ')
        if manual_edit == 'N':                          #Edit name
            new_bank_name = input('What would you like to rename it? ')
            data_bank_name = (new_bank_name, chng_id)
            main.insert_execute_query(q.update_bank_name, data_bank_name)
        elif manual_edit == 'T':                        #Edit type
            new_bank_type = input('What is the bank type? ')
            data_bank_type = (new_bank_type, chng_id)
            main.insert_execute_query(q.update_bank_type, data_bank_type)
        elif manual_edit == 'B':                        #Edit balance
            new_bank_balance = float(input('What is the updated balance? '))
            data_bank_balance = (new_bank_balance, chng_id)
            main.insert_execute_query(q.update_bank_balance, data_bank_balance)
        else:
            print('Try Again!')

    elif mode == 'D':                                   #Delete
        edit_bank_d = (main.execute_query(q.select_all_bank))
        for i in range(len(edit_bank_d)):
            print(edit_bank_d[i][0], edit_bank_d[i][1], edit_bank_d[i][2], '-', edit_bank_d[i][3])
        delete_row = str(input('Which would you like to delete? '))
        main.insert_execute_query(q.delete_from_banks, delete_row)

    else:
        print('Try Again!')
        bank_account_settings()


def paymethod_settings():
    #input(new, edit, delete)
    mode = input('(N)ew, (E)dit, (D)elete: ')
    if mode == 'N':
        new_paymethod_name = input("Enter new payment methods name: ")
        new_paymethod_type = input("Enter new payment methods type: ")
        new_paymethod_last_4 = input("Enter new payment methods last 4 (Optional enter to skip): ")
        new_paymethod_balance = input("Enter new payment methods current balance: ")
        new_paymethod_limit = input("Enter new payment methods current limit (Optional enter to skip): ")
        #new_paymethod_data = 
        def check_input(new_paymethod_name, new_paymethod_type, new_paymethod_last_4, new_paymethod_balance, new_paymethod_limit):
            return True
        if check_input(new_paymethod_name, new_paymethod_type, new_paymethod_last_4, new_paymethod_balance, new_paymethod_limit) == True:
            ### To DB
            pass
        else:
            return

    elif mode == 'E':
        pass
    elif mode == 'D':
        pass




