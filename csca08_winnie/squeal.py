from reading import *
from database import *

# Below, write:
# *The cartesian_product function
# *All other functions and helper functions
# *Main code that obtains queries from the keyboard,
#  processes them, and uses the below function to output csv results


def cartesian_product(t1, t2):
    '''(Table, Table) -> Table
    Return a cartesian product Table with the given two Table t1, t2.
    '''
    t1_table = t1.table
    t2_table = t2.table
    # if both two table are not empty
    if t1_table != {} and t2_table != {}:
        table_data = {}
        row_num_t1 = num_rows(t1)
        row_num_t2 = num_rows(t2)
        # populate table_data with keys from t1_table
        for key in t1_table:
            table_data[key] = []
            # for every data in list of key
            for index in range(row_num_t1):
                # repeat number of row_num_t2 times
                for loop in range(row_num_t2):
                    table_data[key].append(t1_table[key][index])
        # populate table_data with keys from t2_table
        for key in t2_table:
            table_data[key] = []
            # for every value of key repeat row_num_t1 times
            for index in range(row_num_t1):
                table_data[key] += t2_table[key]
        new_table = Table()
        new_table.populate_table(table_data)
        return new_table
    # if either of table is empty
    elif t1_table == {} and t2_table != {}:
        return t2
    else:
        return t1


def handle_cartesian_products(list_of_table):
    '''(list of Table) -> Table
    Return a cartesian product Table handle multiple Tables.
    '''
    table = Table()
    table.populate_table({})
    # if there are more than two tables
    for tb in list_of_table:
        table = cartesian_product(table, tb)
    return table


def num_rows(table):
    '''(Table) -> int
    Return number of rows with a given table.
    '''
    value_list = list(table.table.values())
    # get the length of value
    rows_num = len(value_list[0])
    return rows_num


def handle_constraint(table, constraint):
    '''(Table, str) -> Table
    Return a new Table contains data only corresponding constraint.
    '''
    # get the operator
    if ">" in constraint:
        operator = ">"
    elif "=" in constraint:
        operator = "="
    list_constraint = constraint.split(operator)
    # get column from constraint
    column = list_constraint[0]
    row_num = num_rows(table)
    table_data = table.table
    new_table_dict = {}
    # populate new_table_dict with keys from table_data
    for key in table_data:
        new_table_dict[key] = []
    for index in range(row_num):
        column_value = list_constraint[1]
        # check if second place if column or value
        if "'" in column_value:
            column_value = column_value.strip("'")
        else:
            column_value = table_data[column_value][index]
        if operator == ">":
            # check comparison
            if table_data[column][index] > column_value:
                # add data to new_table_dic
                for key in table_data:
                    value = table_data[key][index]
                    new_table_dict[key].append(value)
        elif operator == "=":
            if table_data[column][index] == column_value:
                for key in table_data:
                    value = table_data[key][index]
                    new_table_dict[key].append(value)
    new_table = Table()
    new_table.populate_table(new_table_dict)
    return new_table


def handle_constraints(table, list_of_constraints):
    '''(Table, list of str) -> Table
    Return a Table that handle mutiple constrains.
    '''
    for constraint in list_of_constraints:
        # if there are more than one constraint
        table = handle_constraint(table, constraint)
    return table


def run_query(database, query):
    '''(Database, str) -> NoneType
    Print out the Table display version with the given database and SQL query.
    '''
    query_list = query.strip().split()
    list_of_columns = query_list[1].split(",")
    list_of_tables = query_list[3].split(",")
    constrain_list = []
    if (len(query_list) > 4):
        constrain_list = query_list[5].split(",")
    for i in range(len(list_of_tables)):
        list_of_tables[i] = database.database[list_of_tables[i]]
    table = Table()
    # handle mutiple table
    table = handle_cartesian_products(list_of_tables)
    # add constrain to table
    if constrain_list != []:
        table = handle_constraints(table, constrain_list)
    # select all columns
    if list_of_columns == ["*"]:
        return table
    else:
        new_table_dic = {}
        table_dict = table.table
        # select specifiy columns
        for column in list_of_columns:
            new_table_dic[column] = table_dict[column]
        new_table = Table()
        new_table.populate_table(new_table_dic)
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
    database = read_database()
    table = run_query(database, query)
    print_csv(table)
