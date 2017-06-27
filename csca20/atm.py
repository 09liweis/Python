import datetime
import sys
from banking import *

def get_date():
    '''(NoneType) -> str
    Return the todays date as YYYY-MM-DD.
    '''
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d")


# Interactive Functions

def account_balances_prompt(db, number):
    '''(str, str) -> NoneType
    Display the account balances for the given bank card.
    '''
    
    # query database for account balances
    [(savings, chequing)] = get_account_balances(db, number)
    
    # display the balances
    msg = 'Savings: ' + str(savings) + '\t Chequing: ' + str(chequing)
    print('Account Balances\n' + msg)

def pay_bill_prompt(db, number):
    '''(str, str) -> NoneType
    Get from_account, bill name, amount from user.'''
    
    values = []
    categories = ['Bill Name:', 'From Account:', 'Amount:']
    
    # prompt user for bill to be paid, from which account to pay the bill and for how much
    values.append(input('Please enter the bill to be paid: '))
    values.append(input('Please enter from which account to pay the bill (Savings or Chequing): '))
    values.append(float(input('How much do you wish to pay? ')))
    
    # update the database for the bill payment and retrieve the new balances
    new_balance = pay_bill(db, values[0],  number, values[1], values[2], get_date())
    
    # display the new balances
    print('Your new %s balance is %.2f.' %(values[1], new_balance))

def transfer_funds_prompt(db, number):
    '''(str, str) -> NoneType
    Given a database name and client number (a str).  Display the current account balances
    and get from_account, to_account and amount from the user using a multenterbox. Perform the
    tranfer of funds updating the account balances. Display the new balances using a msgbox.'''
    
    values = []
    # query database for account balances
    [(savings, chequing)] = get_account_balances(db, number)
    
    # prompt user for from account and display current balances
    values.append(input('Your current account balances: Savings: ' + str(savings)\
                          + ' Chequing: :' + str(chequing) + '\n' + \
                          'Please enter the account to transfer from (Savings or Chequing: )\n'))

    # prompt user for account to transfer to
    values.append(input('Please enter the account you with to transfer to (Savings or Chequing):\n '))

    # prompt user for amount to transfer
    values.append(float(input('Please enter the amount to transfer: ')))
       
    # get the new balances from the database
    new_balances =transfer_funds(db, number, values[0], values[1], values[2], get_date())
    
    # display the new balances
    print('Your new ' + values[0] + ' balance is ' + \
           str(new_balances[0]) + '.\nYour new ' + values[1] + ' balance is ' + \
           str(new_balances[1]) + '.')


def transactions_prompt(db, number):
    '''(str, str) -> NoneType
    Get From_account and Pay_to bill for query from user and display results.'''
    
    # ask for the "From" account
    from_account = input('Which account do you wish to pay from? Savings and Chequing: ')
    
    # query the database to find bills 
    bills =  get_bills(db, number, from_account)
    for i in range(len(bills)):
        bills[i] = str(bills[i][0])
                             
    # ask user to indicate which bills to find
    bill = input('Which transaction do you wish to search for ' + str(bills))
    
    # get the bill transactions from the database
    transactions_list = get_transactions(db, number, from_account, str(bill))
    
    # create the message to display
    msg = 'Date\t\tAmount\n'
    for item in transactions_list:
        msg += '%s\t %.2f\n' %(str(item[0]), item[1])
        
    # display the message
    print(' Transactions from %s to %s:\n ' %(from_account, str(bill)), msg)

def sum_transactions_prompt(db, number):
    '''(str, str) -> NoneType
    Get the date after which all bill payments are to be summed and report
    in a msgbox the sum of each .'''
    
    # get the date to use in the query
    date = input('Enter the date after which all bills will be summed (YYYY-MM-DD):')
    # ask the database for the sum of bills
    bills = sum_transactions(db, number, date)
    
    # create the message to display
    msg = ''    
    for (bill_name, bill_sum) in bills:
        msg += "%s:\t %.2f\n" %(str(bill_name), bill_sum)

    # display the results    
    print('Summation of Bills:\n', msg)

def account_info_prompt(dbname, number):
    '''(st, str) -> NoneType
    Display the result of the get_account_info query in a msgbox.'''
    
    # ask the database for the account info
    [(Name, Address, Savings, Chequing)] = get_account_info(dbname, number)

    # display the account info
    print( 'Name: %s\nAddress: %s\nSavings: %.2f\nChequing: %.2f\n' \
        %(Name, Address, float(Savings), float(Chequing)))



def check_password(db, password, id):
    '''(str, str, user) -> bool
        Return True if the given password matches the given id's password in the
        database db.'''
    
    [(check,)] = run_query(db,'''SELECT Password FROM Security WHERE Number = (?)''', (id,))

    return (check == password)

def quit(db = None, bank_card = None):
    '''Exists the program. '''
    
    sys.exit()


if __name__ == "__main__":
    
    db = 'banking.db'

    setup_security(db, 'password_file.txt')
    setup_accounts(db, 'accounts.txt')
    setup_transactions(db, 'transactions.txt')
    
    bank_card = input('Enter your client number: ')
    # look up in password table to ensure the correct match
    password = input('Enter your secure password: ')
    
    # get users password and continue to ask until the provide the correct one or quit
    while not check_password(db, password, bank_card) :
        if 'quit' == input('Your password did not match the one on file. '+\
                               'Do you wish to re-enter or quit? '):
            quit()
        else:
            password = input('Enter your secure password: ')
    
    

    #string containing of options for account management
    options = '(1) Quit\n(2) Get Account Balances\n(3) Pay Bill\n(4) Get Transactions\n' + \
        '(5) Sum Bill Payments\n(6) Get Account Info\n(7) Transfer Funds\n' 
    
    # dictionary mapping option numbers to function calls
    
    functions = {1: quit, 2 : account_balances_prompt, 3 : pay_bill_prompt, 4 : transactions_prompt,
                 5 : sum_transactions_prompt, 6 : account_info_prompt, 7 : transfer_funds_prompt}
    
    
    while 1:
        # continue to execute commands until the user asks to quit or puts in 0
        choice = int(input('\nPlease select what you would like to do. Enter the number in paranthesis: \n\n' + options))
        if choice:
            func = functions[choice]
            func(db, bank_card)
        else:
            exit()


