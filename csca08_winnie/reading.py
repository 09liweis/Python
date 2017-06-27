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
file_list = glob.glob('*.csv')
# print(file_list)

# Write the read_table and read_database functions below


def read_table(table_file):
    '''(str) -> Table
    Return a Table with a given table_file.
    '''
    open_file = open(table_file, "r")
    # convert file to list of strings
    table_list = open_file.readlines()
    columns = table_list[0].strip().split(",")
    table_data = {}
    # populate table_data with first line of file
    for key in columns:
        table_data[key] = []
    # loop rest of the data
    for data in table_list[1:]:
        data_list = data.strip().split(",")
        # use index to get corresponding key and value
        for i in range(len(columns)):
            key = columns[i]
            value = data_list[i].strip()
            table_data[key].append(value)
    new_table = Table()
    new_table.populate_table(table_data)
    return new_table


def read_database():
    '''() -> Database
    Return a Database with a list of file name in the current directory.
    '''
    database_data = {}
    for table_file in file_list:
        # get name of file as key
        file_name = table_file.split(".")[0]
        table = read_table(table_file)
        database_data[file_name] = table
    new_database = Database()
    new_database.populate_database(database_data)
    return new_database
