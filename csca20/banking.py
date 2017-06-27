import sqlite3


def run_query(db, query, args=None):
    '''(str, str, [tuple]) -> list of tuple
    Return the results of running the given query on database db.'''

    con = sqlite3.connect(db)
    cur = con.cursor()
    if args is None:
        cur.execute(query)
    else:
        cur.execute(query, args)
    data = cur.fetchall()
    cur.close()
    con.close()
    return data


def run_command(db, command, args=None):
    '''(str, str, [tuple]) -> NoneType
    Execute the given command with the args on database db.'''

    con = sqlite3.connect(db)
    cur = con.cursor()
    if args is None:
        cur.execute(command)
    else:
        cur.execute(command, args)
    cur.close()
    con.commit()
    con.close()


def setup_accounts(db, filename):
    '''(str, str) -> NoneType
    Create and populate the Accounts table for database db using the
    contents of the file named filename.'''

    data_file = open(filename)
    con = sqlite3.connect(db)
    cur = con.cursor()
    # create Accounts table
    cur.execute('''CREATE TABLE Accounts(Number TEXT, Savings REAL, \
    Chequing REAL)''')
    # loop line in file and insert data into table
    for line in data_file:
        data = line.split(', ')
        number = data[0].strip()
        savings = float(data[1].strip())
        chequing = float(data[2].strip())
        data_args = (number, savings, chequing)
        cur.execute('INSERT INTO Accounts VALUES (?,?,?)', data_args)
    data_file.close()
    cur.close()
    con.commit()
    con.close()


def setup_transactions(db, filename):
    '''(str, str) -> NoneType
    Create and populate the Transactions table for database db using the
    contents of the file named filename.'''

    data_file = open(filename)
    con = sqlite3.connect(db)
    cur = con.cursor()

    # create and populate the table here
    cur.execute('''CREATE TABLE Transactions(Date TEXT, Number TEXT, \
    Type TEXT, PayFrom TEXT, PayTo TEXT, Amount REAL)''')
    # loop through line in file insert data into table
    for line in data_file:
        data = line.split(', ')
        date = data[0].strip()
        number = data[1].strip()
        pay_type = data[2].strip()
        pay_from = data[3].strip()
        pay_to = data[4].strip()
        amount = float(data[5].strip())
        data_args = (date, number, pay_type, pay_from, pay_to, amount)
        cur.execute('INSERT INTO Transactions VALUES (?,?,?,?,?,?)', data_args)
    data_file.close()
    cur.close()
    con.commit()
    con.close()


def setup_security(db, filename):
    '''(str, str) -> NoneType
    Create and populate the Security table for database db using the
    contents of the file named filename.'''

    data_file = open(filename)
    con = sqlite3.connect(db)
    cur = con.cursor()

    # create and populate the table here
    cur.execute('''CREATE TABLE Security(Number TEXT, Password TEXT, \
    Name TEXT, Address TEXT)''')
    # loop through line in file and insert data into table
    for line in data_file:
        data = line.split(', ')
        number = data[0].strip()
        password = data[1].strip()
        name = data[2].strip()
        address = data[3].strip()
        data_args = (number, password, name, address)
        cur.execute('INSERT INTO Security VALUES (?,?,?,?)', data_args)
    data_file.close()
    cur.close()
    con.commit()
    con.close()


def get_account_balances(db, client_number):
    '''(str, str) -> list of tuple
    Return a list of tuple contains savings and chequing amount with a
    client_number in the given db.
    '''
    command = 'SELECT Savings, Chequing FROM Accounts WHERE Number = ?'
    args = (client_number,)
    account_balances = run_query(db, command, args)
    return account_balances


def get_transactions(db, client_number, from_acc, payto):
    '''(str, str, str, str) -> list of tuple
    Return a list of tuple that each tuple contains date and amount with given
    db, client_number, from_acc, payto.
    '''
    command = 'SELECT Date, Amount FROM Transactions \
    WHERE Number = ? AND PayFrom = ? AND PayTo = ?'
    args = (client_number, from_acc, payto)
    client_trans = run_query(db, command, args)
    return client_trans


def get_bills(db, client_number, paid_from):
    '''(str, str, str) -> list of tuple
    Return a list of tuple that each tuple contains the name of the PayTo bill
    with given db, client_number and name of the paid_from account.
    '''
    command = 'SELECT PayTo FROM Transactions WHERE Number = ? AND PayFrom = ?'
    args = (client_number, paid_from)
    bills_list = run_query(db, command, args)
    return bills_list


def get_account_info(db, client_number):
    '''(str, str) -> a list of tuple
    Return a list of single tuple contains client's name, address, Savings
    and Chequing account balances with client_number in db.
    '''
    command = 'SELECT S.Name, S.Address, A.Savings, A.Chequing \
    FROM Security S JOIN Accounts A WHERE S.Number = A.Number AND S.Number = ?'
    args = (client_number,)
    account_info = run_query(db, command, args)
    return account_info


def update_account_balance(db, client_number, account, amount):
    '''(str, str, str, float) -> flat
    Update the account balance with account_balances and client_number in db.
    '''
    # update the account balance with amount
    command = 'UPDATE Accounts SET ' + account + ' = ' + account + ' + ? \
    WHERE Number = ?'
    args = (amount, client_number)
    run_command(db, command, args)

    command = 'SELECT ' + account + ' FROM Accounts WHERE Number = ?'
    args = (client_number,)
    # select account current balance
    account_balances = run_query(db, command, args)
    return account_balances[0][0]


def pay_bill(db, pay_to, client_number, pay_from, amount, date):
    '''(str, str, str, str, float, str) -> float
    Update the new balance of pay_from in Accounts, then insert new transaction
    in Transactions, return the new balance of pay_from in Accounts.
    '''
    # insert the new transaction in Transactions
    command = 'INSERT INTO Transactions VALUES(?, ?, ?, ?, ?, ?)'
    args = (date, client_number, "Bill", pay_from, pay_to, amount)
    run_command(db, command, args)
    # since pay bill will decrease the balance, we set the amount to negative
    amount = (0 - amount)
    # get new balance
    new_balance = update_account_balance(db, client_number, pay_from, amount)
    return new_balance


def sum_transaction(db, client_number, date):
    '''(str, str, str) -> list of tuples
    Return a list of tuples that each tuple is bill name and its sum of amount
    with a given database db, client_number, and date.
    '''
    # sum up the amount group by payTo account
    command = 'SELECT PayTo, SUM(Amount) FROM Transactions \
    WHERE Number = ? AND Date > ? AND Type = ? GROUP BY PayTo'
    args = (client_number, date, "Bill")
    transactions = run_query(db, command, args)
    return transactions


def transfer_funds(db, number, from_acc, to_acc, amount, date):
    '''(str, str, str, float, str) -> list of float
    Add a row to the transactions table, update the account balance and
    return the new account balances as a list where the the first item
    is the new balance for the "from" account and the second item is the
    new balance of the "to" account.
    '''

    from_new_balance = update_account_balance(db, number, from_acc, (0-amount))
    to_new_balance = update_account_balance(db, number, to_acc, amount)
    command = 'INSERT INTO Transactions VALUES(?, ?, ?, ?, ?, ?)'
    args = (date, number, 'Transfer', from_acc, to_acc, amount)
    run_command(db, command, args)

    return [from_new_balance, to_new_balance]


# setup_accounts("banking.db", "accounts.txt")
# setup_security("banking.db", "password_file.txt")
# setup_transactions("banking.db", "transactions.txt")
# db = "banking.db"
# print(get_account_balances(db, "12345"))
# print(get_transactions(db, "12345", "Savings", "Chequing"))
# print(get_bills(db, "12345", "Chequing"))
# print(get_account_info(db, "12345"))
# print(update_account_balance(db, "12345", "Savings", 10.0))
# print(pay_bill(db, "Visa", "12345", "Savings", 10.0, "2015-12-02"))
# print(sum_transaction(db, "12345", "2011-02-12"))
