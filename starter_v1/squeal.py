from reading import *
from database import *

# Below, write:
# *The cartesian_product function
# *All other functions and helper functions
# *Main code that obtains queries from the keyboard,
#  processes them, and uses the below function to output csv results
def cartesian_product(table1, table2):
    '''(Table, Table) -> Table
    Return a cartesian product Table with the give two Tables.
    '''
    if table1.table_dict == {}:
        return table2
    elif table2.table_dict == {}:
        return table1
    new_table = {}
    t1_d = table1.table_dict
    t2_d = table2.table_dict
    t1_d_columns = t1_d.keys()
    t2_d_columns = t2_d.keys()
    t1_d_num_rows = num_rows(table1)
    t2_d_num_rows = num_rows(table2)
    new_table_column = t1_d_columns + t2_d_columns
    # populate columns with empty list in new_table
    for column in new_table_column:
        new_table[column] = []
    # insert data from table1
    for column in t1_d_columns:
        for i in range(t1_d_num_rows):
            # for every data repeat number of t2 rows number times
            for j in range(t2_d_num_rows):
                new_table[column].append(t1_d[column][i])
    # insert data from table2
    for column in t2_d_columns:
        # for every list repeat number of t1 rows number times
        for i in range(t1_d_num_rows):
            new_table[column] += t2_d[column]
    table = Table()
    table.set_table(new_table)
    return table

def num_rows(table):
    '''(Table) -> int
    Return the number of values in a single key-value pair with the given table.
    '''
    value_list = table.table_dict.values()
    return len(value_list[0])

def split_constraint(constraint):
    '''(str) -> list
    return list contains column, column or value and operator.
    '''
    if "=" in constraint:
        operator = "="
    else:
        operator =  ">"
    constraint_split = constraint.split(operator)
    if "'" in constraint:
        constraint_split[1] = constraint_split[1].strip("'")
    constraint_split.append(operator)
    return constraint_split

def constraint_check(table, constraint):
    '''(Table, str) -> Table
    Return a Table that only matches the limitation of constraint with
    the give table.
    '''
    constraint_split = split_constraint(constraint)
    operator = constraint_split[2]
    column1 = constraint_split[0]
    new_table = {}
    table_dict = table.table_dict
    table_column = table_dict.keys()
    # populate columns in the new_table
    for column in table_column:
        new_table[column] = []
    for i in range(num_rows(table)):
        col_val = constraint_split[1]
        # check if the col_val is a column or a value
        if "'" not in constraint:
            # assign column value to col_val
            col_val = table_dict[col_val][i]
        else:
            # assign value to col_value
            col_val = constraint_split[1]
        if operator == "=":
            if table_dict[column1][i] == col_val:
                # if match, loop the table_dict key value by index i
                for key in table_dict:
                    # add to new_table
                    new_table[key].append(table_dict[key][i])
        else:
            if table_dict[column1][i] > col_val:
                for key in table_dict:
                    new_table[key].append(table_dict[key][i])
    table = Table()
    table.set_table(new_table)
    return table

def run_query(database, query):
    '''(Database, str) -> NoneType
    Print out the Table display version with the given database and SQL query.
    '''
    query_list = query.strip().split()
    column_list = query_list[1].split(",")
    table_list = query_list[3].split(",")
    constrain_list = []
    if (len(query_list) > 4):
        constrain_list = query_list[5].split(",")
    for i in range(len(table_list)):
        table_list[i] = database.database_dict[table_list[i]]
    table = Table()
    # handle mutiple table
    for i in range(len(table_list)):
        table = cartesian_product(table, table_list[i])
    # add constrain to table
    if constrain_list != []:
        for constraint in constrain_list:
            table = constraint_check(table, constraint)
    # select all columns
    if column_list == ["*"]:
        return table
    else:
        new_dict = {}
        table_dict = table.table_dict
        # select specifiy columns
        for column in column_list:
            new_dict[column] = table_dict[column]
        new_table = Table()
        new_table.set_table(new_dict)
        return new_table

def print_csv(table):
    '''(Table) -> NoneType
    Print a representation of table.
    '''
    dict_rep = table.get_dict()
    columns = list(dict_rep.keys())
    print(','.join(columns))
    rows = num_rows(table)
    for i in range(rows):
        cur_column = []
        for column in columns:
            cur_column.append(dict_rep[column][i])
        print(','.join(cur_column))

if(__name__ == "__main__"):
    query = input("Enter a SQuEaL query, or a blank line to exit:")
    # query = "select b.gross,i.rating,b.year,b.studio,i.title from boxoffice,imdb where i.title=b.title,i.rating>'8',b.year='2010'"
    database = read_database()
    table = run_query(database, query)
    print_csv(table)