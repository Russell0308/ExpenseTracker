import queries as q
import sqlite3


U_db_conn = sqlite3.connect('Users_db.sqlite3')


def db_connect(username):
    

    db_conn = sqlite3.connect('db.sqlite3')


#def eat_password():


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


def log_purchase(data):
    insert_execute_query(q.insert_table_expense, data)


def get_paymethod_names_out():
    return execute_query(q.get_paymethod_names)


