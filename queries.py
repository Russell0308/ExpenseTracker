# CREATE TABLES #
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
method_last_4 INTEGER,
method_balance INTEGER
);"""

create_table_bank = """CREATE TABLE IF NOT EXISTS
banks(
bank_id INTEGER PRIMARY KEY AUTOINCREMENT,
bank_name VARCHAR(255),
account_type VARCHAR(255),
balance INTEGER
);"""

# INSERT TO TABLES #
insert_table_expense = """INSERT INTO expenses(date, time, description, amount, payment_method, merchant_name, location, recurring) VALUES (?, ?, ?, ?, ?, ?, ?, ?);"""

# SELECT FROM TABLES #
select_bank_balance = """SELECT * FROM banks WHERE account_type="""

get_balance_banking = """SELECT balance FROM banks WHERE account_type='Banking'"""

get_balance_savings = """SELECT balance FROM banks WHERE account_type='Savings'"""

get_paymethod_balance = """SELECT * FROM paymethods WHERE method_name="""

# UPDAATE TABLE VALUES #
update_bank_balance = """UPDATE banks SET balance=? WHERE account_type=?;"""

update_card_balance = """UPDATE paymethods SET method_balance=? WHERE method_name=?;"""

