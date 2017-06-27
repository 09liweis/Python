import sqlite3
import datetime


def create_customers(db, data_file):
    '''Create and populate the Customer table with
    the data from the open file data_file.'''

    # connect to the database
    con = sqlite3.connect(db)
    # create a cursor
    cur = con.cursor()

    # Create the customer table
    cur.execute('''CREATE TABLE Customers(id TEXT,last_name TEXT,\
    first_name TEXT,street_num TEXT,street_name TEXT,city TEXT,province TEXT,\
    code TEXT,tel TEXT,alt_tel TEXT,email TEXT)''')

    # Populate the Custormer Table
    # Loop through each line in the file:
    for line in data_file:
        # Split the data in each line and store in a
        # list called data
        data = line.split(',')
        if len(data) > 1:
            # insert the data into the table (careful about types!)
            cur.execute('INSERT INTO Customers \
                        VALUES(?,?,?,?,?,?,?,?,?,?,?)', \
                        (data[0].strip(), data[1].strip(), \
                            data[2].strip(), data[3].strip(), \
                            data[4].strip(), data[5].strip(), \
                            data[6].strip(), data[7].strip(), \
                            data[8].strip(), data[9].strip(), \
                            data[10].strip()))

    # close the cursor
    cur.close()

    # commit the changes
    con.commit()

    # close the connection
    con.close()


def create_books(db, reader):
    '''Create and populate the Books table with
    the data from the open file data_file.'''

    # connect to the database
    con = sqlite3.connect(db)
    # create a cursor
    cur = con.cursor()

    # Create the Book table

    # add your code here
    cur.execute('''CREATE TABLE Books(id TEXT, title TEXT, author TEXT)''')

    # Populate the Books Table
    # Loop through each line in the file:

    # add your code here
    for line in reader:
        data = line.split(',')
        if len(data) > 1:
            cur.execute('''INSERT INTO Books VALUES(?, ?, ?)''', \
                        (data[0].strip(), data[1].strip(), data[2].strip()))

    # close the cursor
    cur.close()

    # commit the changes
    con.commit()

    # close the connection
    con.close()


def create_loans(db):
    '''Create the Loans table.'''

    # connect to the database
    con = sqlite3.connect(db)
    # create a cursor
    cur = con.cursor()

    # Create the customer table
    # put your code here
    cur.execute('''CREATE TABLE Loans(CustomerID TEXT, BookID TEXT,\
    BorrowedDate TEXT, DueDate TEXT, ReturnDate TEXT)''')
    loans = []
    loans.append(["148", "5866", "20151101", "20151121", "NULL"])
    loans.append(["185", "6413", "20151201", "20151230", "20151215"])
    loans.append(["537", "4013", "20151202", "20151230", "NULL"])
    loans.append(["148", "4013", "20151107", "20151122", "NULL"])
    for loan in loans:
        cur.execute('''INSERT INTO Loans VALUES(?, ?, ?, ?, ?)''', \
                    (loan[0], loan[1], loan[2], loan[3], loan[4]))
    # close the cursor
    cur.close()

    # commit the changes
    con.commit()

    # close the connection
    con.close()


def run_query(db, query, args=None):
    '''Return the results of running query q on database db.
    If given, args contains the query arguments.'''

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


def get_info_by_id(db, id):
    '''
    Return infomation about a customer with given db, id.
    '''
    query = 'SELECT * FROM Customers WHERE id = ?'
    args = (id,)
    info = run_query(db, query, args)
    return info


def get_id_by_name(db, last, first):
    '''
    Return a list of ids with given db, last name, first name.
    '''
    query = 'SELECT id FROM Customers WHERE last_name = ? AND first_name = ?'
    args = (last, first)
    ids = run_query(db, query, args)
    return ids


def get_all_loans_by_id(db, id):
    '''
    Return a list of book ids have not been return by customer id.
    '''
    query = 'SELECT BookID FROM Loans WHERE ReturnDate = ? AND CustomerID = ?'
    args = ("NULL", id)
    bookIds = run_query(db, query, args)
    return bookIds


def get_checked_out_by_id(db, id):
    '''
    Return a list of book ids checkout by the customer id.
    '''
    query = 'SELECT BookID FROM Loans WHERE ReturnDate <= DueDate AND \
    CustomerID = ?'
    args = (id,)
    bookIds = run_query(db, query, args)
    return bookIds


def get_overdue_by_id(db, id):
    '''
    Return a list of book ids passed due date by the customer id.
    '''
    query = 'SELECT BookID FROM Loans WHERE DueDate < ? AND CustomerID = ?'
    args = (str(datetime.datetime.now().date()).replace('-', ''), id)
    bookIds = run_query(db, query, args)
    return bookIds


if __name__ == '__main__':

    # open the data files
    customer = open("address.txt")
    books = open("books.txt")

    # populate the tables
    db = "lab.db"
    create_customers(db, customer)
    create_books(db, books)
    create_loans(db)

    # close the files
    customer.close()
    books.close()
    # call queries
    print(get_info_by_id(db, "904"))
    print(get_id_by_name(db, "Snyder", "Angel"))
    print(get_all_loans_by_id(db, "148"))
    print(get_checked_out_by_id(db, "185"))
    print(get_overdue_by_id(db, "148"))
