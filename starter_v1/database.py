class Table():
    '''A class to represent a SQuEaL table'''
    
    def __init__(self):
        self.table_dict = {}
    
    def set_table(self, new_dict):
        self.table_dict = new_dict

    def set_dict(self, new_dict):
        '''(Table, dict of {str: list of str}) -> NoneType

        Populate this table with the data in new_dict.
        The input dictionary must be of the form:
            column_name: list_of_values
        '''
        self.table_dict = new_dict

    def get_dict(self):
        '''(Table) -> dict of {str: list of str}

        Return the dictionary representation of this table. The dictionary keys
        will be the column names, and the list will contain the values
        for that column.
        '''
        return self.table_dict


class Database():
    '''A class to represent a SQuEaL database'''
    
    def __init__(self):
        self.database_dict = {}
    
    def set_database(self, new_dict):
        self.database_dict = new_dict

    def set_dict(self, new_dict):
        '''(Database, dict of {str: Table}) -> NoneType

        Populate this database with the data in new_dict.
        new_dict must have the format:
            table_name: table
        '''
        self.database_dict = new_dict

    def get_dict(self):
        '''(Database) -> dict of {str: Table}

        Return the dictionary representation of this database.
        The database keys will be the name of the table, and the value
        with be the table itself.
        '''
        return self.database_dict
