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
def read_database():
    '''() -> Database
    return Database with all file_list.
    '''
    new_database = {}
    # loop file_list
    for file in file_list:
        # get the file name without type
        fname = file[:-4]
        new_table = read_table(file)
        # insert key value
        new_database[fname] = new_table
    database = Database()
    database.set_database(new_database)
    return database

def read_table(file_name):
    '''(str) -> Table
    Return a Table with a given file name.
    '''
    reader = open(file_name, "r")
    new_dict = {}
    # get first line of column name
    column_line = reader.readline()
    column_list = column_line.strip().split(",")
    # fill the new table with key and empty list
    for column in column_list:
        new_dict[column] = []
    # loop the rest of the data line
    for line in reader:
        # check if line is empty
        if line.strip() != "":
            data_list = line.strip().split(",")
            # use index to get conresponding column and its data
            for index in range(len(column_list)):
                column = column_list[index]
                data = data_list[index]
                new_dict[column].append(data)
    table = Table()
    table.set_table(new_dict)
    return table
