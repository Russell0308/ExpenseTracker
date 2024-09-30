# CREATE TABLES #
create_table_users = """
users(
user_id INTEGER PRIMARY KEY AUTOINCREMENT,
username VARCHAR(25),
password VARCHAR(256),
db_names VARCHAR(255),
);"""
create_table_expense = """CREATE TABLE IF NOT EXISTS
expenses(
expense_id INTEGER PRIMARY KEY AUTOINCREMENT,
date DATE,
time TIME,
description VARCHAR(1000),
amount INTEGER,
payment_method VARCHAR(255),
merchant_name VARCHAR(255),
location VARCHAR(255),
recurring BOOLEAN
);"""

create_table_paymethod = """CREATE TABLE IF NOT EXISTS
paymethods(
method_id INTEGER PRIMARY KEY AUTOINCREMENT,
method_name VARCHAR(255),
method_type VARCHAR(255),
method_last_4 INTEGER,
method_balance INTEGER,
method_limit INTEGER
);"""

create_table_bank = """CREATE TABLE IF NOT EXISTS
banks(
bank_id INTEGER PRIMARY KEY AUTOINCREMENT,
bank_name VARCHAR(255),
account_type VARCHAR(255),
balance INTEGER
);"""

create_table_income = """CREATE TABLE IF NOT EXISTS
income(
id INTEGER PRIMARY KEY AUTOINCREMENT,
pay_date DATE,
amount INTEGER,
gross_amount INTEGER
);"""

create_table_save_up = """CREATE TABLE IF NOT EXISTS
saveup(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name VARCHAR(55),
price INTEGER,
target_date DATE,
priority INTEGER,
financed BOOLEAN,
downpayment INTEGER, 
monthly INTEGER, 
finlength VARCHAR(55)
);"""

create_table_pay_periods = """CREATE TABLE IF NOT EXISTS
pay_periods(
id INTEGER PRIMARY KEY AUTOINCREMENT,
pay_day DATE
);"""

# INSERT TO TABLES #
insert_table_expense = """INSERT INTO expenses(date, time, description, amount, payment_method, merchant_name, location, recurring) VALUES (?, ?, ?, ?, ?, ?, ?, ?);"""

insert_table_banks = """INSERT INTO banks(bank_name, account_type, balance) VALUES (?, ?, ?)"""

insert_table_paymethod = """INSERT INTO paymethods(method_name, method_type, method_last_4, method_balance, method_limit) VALUES (?, ?, ?, ?, ?)"""

insert_table_income = """INSERT INTO income(pay_date, amount, gross_amount) VALUES (?, ?, ?);"""

insert_table_save_up = """INSERT INTO saveup(name, price, target_date, priority, financed, downpayment) VALUES (?, ?, ?, ?, ?, ?);"""

insert_table_pay_periods = """INSERT INTO pay_periods(pay_day) VALUES (?);"""

# SELECT FROM TABLES #
select_all_bank = """SELECT * FROM banks"""

select_bank_balance = """SELECT * FROM banks WHERE account_type="""

get_balance_banking = """SELECT balance FROM banks WHERE account_type='Banking'"""

get_balance_savings = """SELECT balance FROM banks WHERE account_type='Savings'"""

get_paymethod_balance = """SELECT * FROM paymethods WHERE method_name="""

get_next_pay_week = """SELECT * FROM pay_periods;"""

get_paymethod_names = """SELECT method_name from paymethods;"""

get_users = """SELECT username from   """

# UPDATE TABLE VALUES #
update_bank_balance = """UPDATE banks SET balance=? WHERE bank_id=?;"""

update_bank_name = """UPDATE banks SET bank_name=? WHERE bank_id=?;"""

update_bank_type = """UPDATE banks SET account_type=? WHERE bank_id=?;"""

update_card_balance = """UPDATE paymethods SET method_balance=? WHERE method_name=?;"""

#REMOVE ROWS FROM TABLE#
delete_from_banks = """DELETE FROM banks WHERE bank_id=?;"""
