import pyodbc
from lib.connector import DBConnector


class DB:
    @staticmethod
    def insert(table_name, values):
        try:
            conn = DBConnector()
            cursor = conn.cursor()
            columns = ', '.join('"' + str(x).replace('/', '_') + '"' for x in values.keys())
            values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in values.values())
            sql = "INSERT INTO %s ( %s ) VALUES ( %s );" % (table_name, columns, values)
            response = cursor.execute(sql)
            if response:
                print("Row Inserted")
            conn.commit()
        except pyodbc.Error as ex:
            sqlstate = ex.args[0]
            print(ex)
            if sqlstate == '23000':
                print("Duplicate Row: " + sql)
                pass


