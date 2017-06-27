# Functions for reading tables and databases

import glob
from database import *

# a table is a dict of {str:list of str}.
# The keys are column names and the values are the values
# in the column, from top row to bottom row.

# A database is a dict of {str:table},
# where the keys are table names and values are the tables.

# YOU DON'T NEED TO KEEP THE FOLLOWING CODE IN YOUR OWN SUBMISSION
# IT IS JUST HERE TO DEMONSTRATE HOW THE glob CLASS WORKS. IN FACT
# YOU SHOULD DELETE THE PRINT STATEMENT BEFORE SUBMITTING
# file_list = glob.glob('*.csv')
# print(file_list)

# Write the read_table and read_database functions below


def read_table(file):
    file = open(file, 'r')
    my_dict = {}
    table = []
    for line in file:
            new_line = line.strip()
            table.append(new_line.split(','))
    headings = table[0]
    rows = table[1:]
    for i in range(len(headings)):
        my_dict.update({headings[i]: []})
        for row in rows:
            if row[0] != '':
                my_dict[headings[i]].append(row[i])
    new_table = Table()
    new_table.new_dict(my_dict)
    file.close()
    return new_table


def read_database():
    file_list = glob.glob('*.csv')
    file_list = [name[:-4] for name in file_list]
    database = {}
    for file in file_list:
        database[file] = read_table(file + '.csv')
    new_database = Database()
    new_database.set_tables(database)
    return new_database
