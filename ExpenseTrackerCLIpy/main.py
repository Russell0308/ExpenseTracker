import os
import sqlite3
import queries as q
import datetime
import settings

year = datetime.datetime.now().year
current_date = datetime.datetime.now()

pay_period_delta = datetime.timedelta(days = 14)
week_delta = datetime.timedelta(days = 7)

message = ''

username = 'russ'
password = 'sfhkl' # username and password are placeholders
login = False

modes = ['Log purchase', 'Log income', 'Card payment', 'Stats', 'Budget', 'Save up', 'Settings']

def post_login():
    global db_conn
    db_conn = sqlite3.connect('db.sqlite3')
    print('\n'*100)
    print('Hello,', username)


def execute_query(query):
    curs = db_conn.cursor()
    curs.execute(query)
    db_conn.commit()
    return curs.fetchall()


def insert_execute_query(query, data):
    curs = db_conn.cursor()
    curs.execute(query, data)
    db_conn.commit()


def create_tables():
    execute_query(q.create_table_expense)
    execute_query(q.create_table_paymethod)
    execute_query(q.create_table_bank)
    execute_query(q.create_table_income)
    execute_query(q.create_table_save_up)
    execute_query(q.create_table_pay_periods)


def login():
    global message
    global login
    print('-----Login-----')
    user_name = ''
    try:
        user_name = input('Enter Username: ')
    except EOFError:
        print('Do not run in NVIM')
    if user_name == username:
        pass_word = input('Enter Password: ')
        if pass_word == password:
            login = True
        elif pass_word == 'hint':
            print('Middle row')
        else:
            message = 'Password is incorrect'
    else:
        message = 'Username is incorrect'


def list_modes():
    for i in range(len(modes)):
        print(i, modes[i])


def log_purchase():
    date = input('Date: ')
    time = input('Time: ')
    description = input('Description: ')
    amount = input('Price: ')
    payment_method = input('Payment method: ')
    merchant_name = input('Merchant name: ')
    location = input('City: ')
    recurring = input('Recurring: ')
    
    amount = float(amount)

    if payment_method == 'Amex':
        current_balance = execute_query(q.get_paymethod_balance + "'Amex'")
        new_balance = amount + current_balance[0][3]
        insert = (new_balance, payment_method)
        insert_execute_query(q.update_card_balance, insert)

    elif payment_method == 'Visa':
        current_balance = execute_query(q.get_paymethod_balance + "'Visa'")
        new_balance = amount + current_balance[0][3]
        insert = (new_balance, payment_method) 
        insert_execute_query(q.update_card_balance, insert)

    elif payment_method == 'Apple card':
        current_balance = execute_query(q.get_paymethod_balance + "'Apple card'")
        new_balance = amount + current_balance[0][3]
        insert = (new_balance, payment_method)
        insert_execute_query(q.update_card_balance, insert)

    elif payment_method == 'Banking':
        current_balance = execute_query(q.get_balance_banking)
        new_balance = amount + current_balance[0][0]
        insert = (new_balance, payment_method)
        insert_execute_query(q.update_bank_balance, insert)

    if len(date) == 5: date = str(year) + '-' + date
    recurring = bool(recurring)
    
    log_all = (date, time, description, amount, payment_method, merchant_name, location, recurring)
    insert_execute_query(q.insert_table_expense, log_all)


def log_income():
    run = True
    while run == True:
        pay_date = input('What day did you get paid?: ')
        income_amount = input('How much did you make?: ')
        gross_amount = input('How much did you make before tax?: ')
        try:
            income_amount = float(income_amount)
            gross_amount = float(gross_amount)
            run = False
        except:
            print('\n' * 20)
            print('Try again, invalid input.')
            pass
    current_balance = execute_query(q.get_balance_banking)
    new_balance = float(income_amount) + float(current_balance[0][0])
    insert = (new_balance, 'Banking')
    insert_execute_query(q.update_bank_balance, insert)
    income_data = (pay_date, income_amount, gross_amount)
    insert_execute_query(q.insert_table_income, income_data)
    print('$' + str(new_balance))
    

def card_payment():
    card = input('Which card?: ')
    payment_amt = input('How much are you paying?: ')
    if payment_amt == 'all':
        card_amt = execute_query(q.get_paymethod_balance + "'" + card + "'")
        bank_amt = execute_query(q.get_balance_banking)
        new_bank_amt = bank_amt[0][0] - card_amt[0][3]
        new_bank_amt = round(new_bank_amt, 2) 
        print('Banking: $' + str(new_bank_amt))
        new_card_amt = 0
        print(card + ': $' + str(new_card_amt))
        insert_bank = (new_bank_amt, 'Banking')
        insert_execute_query(q.update_bank_balance, insert_bank)
        insert_card = (new_card_amt, card)
        insert_execute_query(q.update_card_balance, insert_card)

    else: 
        card_amt = execute_query(q.get_paymethod_balance + "'" + card + "'")
        bank_amt = execute_query(q.get_balance_banking)
        new_bank_amt = bank_amt[0][0] - float(payment_amt)
        new_bank_amt = round(new_bank_amt, 2)
        print('Banking: $' + str(new_bank_amt))
        new_card_amt = card_amt[0][3] - float(payment_amt)
        new_card_amt = round(new_card_amt, 2)
        print(card_amt[0][1] + ': $' + str(new_card_amt))
        insert_bank = (new_bank_amt, 'Banking')
        insert_execute_query(q.update_bank_balance, insert_bank)
        insert_card = (new_card_amt, card)
        insert_execute_query(q.update_card_balance, insert_card)


def important_stats():
    query = q.select_bank_balance + "'Banking'"
    query0 = q.select_bank_balance + "'Savings'"
    bank_balance = execute_query(query)
    bank_balance0 = execute_query(query0)
    print('---'*10)
    print(bank_balance[0][1] + ' Balances')
    print('Total: $' + str(round(float(bank_balance[0][3] + bank_balance0[0][3]), 2)))
    print(bank_balance[0][2] + ': $' + str(bank_balance[0][3]))
    print(bank_balance0[0][2] + ': $' + str(bank_balance0[0][3]))

    query = q.get_paymethod_balance + "'Amex'"
    query0 = q.get_paymethod_balance + "'Visa'"
    query1 = q.get_paymethod_balance + "'Apple card'"
    card_balance = execute_query(query)
    card_balance0 = execute_query(query0)
    card_balance1 = execute_query(query1)
    print('---'*10)
    print('Credit Card Balances')
    print('Total Credit Card debt: $' + str(card_balance[0][3] + card_balance0[0][3] + card_balance1[0][3]))
    print(card_balance[0][1], str(card_balance[0][2]) + ' $' + str(card_balance[0][3]))
    print(card_balance0[0][1], str(card_balance0[0][2]) + ' S' + str(card_balance0[0][3]))
    print(card_balance1[0][1], str(card_balance1[0][2]) + ' $' + str(card_balance1[0][3]))


def update_next_pay_week():
    pay_day = execute_query(q.get_next_pay_week)
    print(datetime.datetime.strptime(pay_day[0][1], '%y/%m/%d') + pay_period_delta)


def save_up():
    try_again = True
    while try_again == True:
        mode = input('Are you saving for a bundle or a big purchase? ')
        if mode == 'bundle':
            # BEEP
            x = 'bundle'
            try_again = False
        elif mode == 'big':
            name = input('Enter the name of your next big purchase: ')
            assert name == str
            price = int(input('Enter the current listed price: '))
            target_date = input('Enter the target purchase date (mm/dd/yy) : ')
            priority = int(input('Enter the priority of the purchase: '))
            financed = bool(input('Will this be financed? '))
            assert financed == bool
            if financed == 'Yes':
                downpayment = int(input('How much do you want to put down? '))
                monthly = int(input('What is the monthly amount? '))
                finlength = input('What is the length of this finance agreement? ')
            elif financed == 'No': 
                pass
            #how many 2 weeks from today to target day
            


    


            #price per check
            while current_date != target_date:
                    current_date = pay_periods 

            ppc = price/pay_periods





            try_again = False
            save_up = (name, price, target_date, priority, financed, downpayment, monthly, finlength)
            insert_execute_query(q.insert_table_save_up, save_up)
        else:
            print('Try again!')
            try_again = True


def delete_db():
    danger = input("Enter 'db.sqlite3': ")
    if danger == 'db.sqlite3':
        delorkeep = input('Are you sure you want to delete(Y/n) ')
        if delorkeep == 'Y':
            os.system('rm db.sqlite3')
            quit()
        else:
            pass
    else:
        pass


def main():
    print('- Select one -')
    while True:
        list_modes()
        mode_input = input('')
        if mode_input == '0':
            log_purchase()
        elif mode_input == '1':
            log_income()
        elif mode_input == '2':
            card_payment()
        elif mode_input == '3':
            #important_stats()
            pass
        elif mode_input == '4':
            #set_budget()
            pass
        elif mode_input == '5':
            save_up()
        elif mode_input == '6':
            settings.settings_main()
        elif mode_input == '7':
            delete_db()
        elif mode_input == 'exit':
            break
        else:
            print('Try again!')




if __name__ == '__main__':
    while True:
        login()
        if login == True:
            print('Successful login')
            post_login()
            create_tables()
            main()
            db_conn.close()
            break
        else:
            print(message)
            login_atmp = ''
            try:
                login_atmp = input('Try again?(y/n) ')
            except EOFError:
                print('No input...')
            if login_atmp != 'y':
                exit()
# END #
