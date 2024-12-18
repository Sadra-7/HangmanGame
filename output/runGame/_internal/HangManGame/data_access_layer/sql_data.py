import pyodbc as odbc

Driver_name = 'SQL SERVER'

# server which the database is located
Server_name = 'DESKTOP-5FKB3Q2'
# your database name
Database_name = 'name'

class Get_data:


    def __init__(self):
        self.name_list = []
        self.connection_string = f"""
        DRIVER={{{Driver_name}}};
        SERVER={Server_name};
        DATABASE={Database_name};
        Trust_Connection = yes;
        """

    def get_names(self):
        conn = odbc.connect(self.connection_string)

        SQL_QUERY = """
        select [first_name] from [dbo].[name$] 
        """


        cursor = conn.cursor()
        cursor.execute(SQL_QUERY).fetchone()

        return cursor


