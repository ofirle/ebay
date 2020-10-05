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
            if sqlstate == '23000':
                print("Duplicate Row: " + sql)
                pass
            else:
                print(ex)

    @staticmethod
    def is_exist(table_name, column_key, column_value):
        try:
            conn = DBConnector()
            cursor = conn.cursor()
            value = "{} = {}".format(column_key, column_value)
            sql = "SELECT 1 FROM %s WHERE %s;" % (table_name, value)
            cursor.execute(sql)
            rows = cursor.fetchall()
            conn.commit()
            if len(rows) != 0:
                return True
            else:
                return False

        except pyodbc.Error as ex:
            print(ex)
            print("Error: " + sql)



