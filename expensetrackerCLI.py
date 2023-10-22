import sqlite3
import queries as q
import datetime

year = datetime.datetime.now().year

message = ''

username = 'russ'
password = 'sfhkl' # username and password are placeholders
login = False

modes = ['Log purchase', 'Log income', 'Card payment', 'View bank balance', 'View card balance', 'View calender', 'View important stats', 'Set budget', 'Save up', 'Settings']

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


def login():
    global message
    global login
    print('-----Login-----')
    user_name = input('Enter Username: ')
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

    if len(date) == 5:
        date = str(year) + '-' + date
    recurring = bool(recurring)
    
    log_all = (date, time, description, amount, payment_method, merchant_name, location, recurring)
    insert_execute_query(q.insert_table_expense, log_all)


def log_income():
    income_amount = input('How much did you make?: ')
    current_balance = execute_query(q.get_balance_banking)
    new_balance = float(income_amount) + float(current_balance[0][0])
    print('$' + str(new_balance))


def view_bank_balance():
    account_type = input('Which account?: ')
    query = q.select_bank_balance + "'" + account_type + "'"
    balance_data = execute_query(query)
    print('Bank:', balance_data[0][1])
    print('Account:', balance_data[0][2])
    print('Balance:', '$' + str(balance_data[0][3]))


def view_card_balance():
    card_name = input('Enter card name: ')
    query = q.get_paymethod_balance + "'" + card_name + "'"
    paymethod_balance = execute_query(query)
    print(paymethod_balance[0][1] + ': $' + str(paymethod_balance[0][3]))


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
    print('Total: $' + str(bank_balance[0][3] + bank_balance0[0][3]))
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




def main():
    print('- Select one -')
    list_modes()
    while True:
        mode_input = input('')
        if mode_input == '0':
            log_purchase()
            break
        elif mode_input == '1':
            log_income()
            break
        elif mode_input == '2':
            card_payment()
            break
        elif mode_input == '3':
            view_bank_balance()
            break
        elif mode_input == '4':
            view_card_balance()
            break
        elif mode_input == '5':
            #view_calender()
            break
        elif mode_input == '6':
            important_stats()
            break
        elif mode_input == '7':
            #set_budget()
            break
        elif mode_input == '8':
            #save_up()
            break
        elif mode_input == '9':
            #settings()
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
            login_atmp = input('Try again?(y/n) ')
            if login_atmp != 'y':
                exit()
# END #
