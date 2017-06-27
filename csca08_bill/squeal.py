from reading import *
from database import *

# Below, write:
# *The cartesian_product function
# *All other functions and helper functions
# *Main code that obtains queries from the keyboard,
#  processes them, and uses the below function to output csv results

def cartesian_product(table1, table2):
    needed_table = {}
    dict1 = table1.table
    dict2 = table2.table
    if dict1 == {} and dict2 != {}:
        return table2
    elif dict2 == {} and dict1 != {}:
        return table1
    else:
        for header in dict1:
            needed_table[header] = []
            for i in range(num_rows(table1)):
                for j in range(num_rows(table2)):
                    needed_table[header].append(dict1[header][i])
                
        for header in dict2:
            needed_table[header] = []
            for i in range(num_rows(table1)):
                needed_table[header] += dict2[header]
    table = Table()
    table.new_dict(needed_table)
    return table

# not using this one
def num_col(table):
    dicta = table.new_table()
    num = 0
    for key in dicta:
        num += 1
    return num

def get_operator(constraint):
    if "=" in constraint:
        operator = "="
    elif ">" in constraint:
        operator = ">"
    return operator

def constraint_list_handle(new_table, constraint_list):
    for constraint in constraint_list:
        # get the operator
        operator = get_operator(constraint)
        # split the constraint
        split_c = constraint.split(operator)
        column1 = split_c[0]
        column2_or_value = split_c[1]
        
        new_table_dict = {}
        table_dict = new_table.new_table()
        # set new dictionary
        for k in table_dict:
            new_table_dict[k] = []
        
        # loop through the rows
        for i in range(num_rows(new_table)):
            column2_or_value = split_c[1]
            # determine if the second argument is column or value
            if "'" not in constraint:
                column2_or_value = table_dict[column2_or_value][i]
            else:
                column2_or_value = column2_or_value.strip("'")
            # put first argument here
            column1_value = table_dict[column1][i]
            if operator != "=":
                if column1_value > column2_or_value:
                    # populate the key with i index data from row
                    for key in table_dict:
                        new_table_dict[key].append(table_dict[key][i])
            else:
                if column1_value == column2_or_value:
                    for key in table_dict:
                        new_table_dict[key].append(table_dict[key][i])
        new_table = Table()
        new_table.new_dict(new_table_dict)
    return new_table

def run_query(database, query):
    '''(Database, str) -> Table
    This function returns the require columns of table. 
    '''
    result = {}
    query_list = query.split()
    column_list = query_list[1].split(",")
    table_list = query_list[3].split(",")
    # split the query to get each compoment
    table_object_list = []
    # get table object from database with table name
    for table_name in table_list:
        table_object_list.append(database.database[table_name])
    
    # combine all those table
    new_table = Table()
    for table_object in table_object_list:
        new_table = cartesian_product(new_table, table_object)
    
    constraint_list = []
    # if there is where token
    if 'where' in query:
        constraint_list = query_list[-1].split(",")
        new_table = constraint_list_handle(new_table, constraint_list)
        
    if "*" in query:
        return new_table
    else:
        final_dict = {}
        # populate column value into final_dict
        for column in column_list:
            final_dict[column] = new_table.table[column]
        final_table = Table()
        final_table.new_dict(final_dict)
    return final_table


# not using this function
def database_to_dict(Database):
    '''(Databse)-> dict of list
    '''
    result = {}
    dict_of_table = Database.get_tables()
    for key in dict_of_table:
        result[key] = dict_of_table[key].new_table()
    return result


## I am not using this function
def no_cond_sql(database, query_list):
    '''(Database, list of str) ->  Table
    '''
    search_key = query_list[1][0].split(',')
    tables = query_list[3][0].split(',')
    table_list = [] #store needed table from database
    column_list = [] #store needed column from tables
    # this part is good
    if '*' in search_key:
        for table in tables:
            db = database.get_tables()    
            table_list.append(db[table])
        new_table = Table()
        for table in table_list:
            new_table = cartesian_product(new_table, table)
        result = new_table.get_dict() 
    # this part has bug
    else:
        for table in tables:
            db = database.get_tables()    
            table_list.append(db[table])
        for table in table_list:
            dict_form = table.new_table()
            for header in search_key:
                if header in dict_form:
                    column = Table()
                    column.new_dict({header: dict_form[header]})
                    column_list.append(column)
        print(column_list)
        for i in column_list:
            print(i.new_table())
        new_table = Table()
        for i in range(len(column_list)):
            new_table = cartesian_product(new_table, column_list[i]) # this part has bug, see shell. [x,x,x]x[x,x] returns [x,x,x] and [x]
            print(new_table.new_table())
        result = new_table.get_dict()
        return result


def num_rows(table):
    '''(table) -> int
    This function returns the number of rows in a table object.
    
    REQ: Table cannot be empty
    
    a = Table()
    a.new_dict({'a': 'aaa', 'b': 'bbb'})
    num_rows(a)
    >>>2
    b = Table()
    b.new_dcit({})
    num_rows(b)
    >>>0
    '''
    values = list(table.table.values())
    value = values[0]
    return len(value)


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
    query = "select b.gross,i.rating,b.year,b.studio,i.title from boxoffice,imdb where i.title=b.title,i.rating>'8',b.year='2010'"
    #query = input("Enter a SQuEaL query, or a blank line to exit:")
    result = run_query(read_database(), query)
    print_csv(result)