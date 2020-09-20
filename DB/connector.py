import pyodbc

class DBConnector:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = cls.create_connection()
        return cls.__instance

    @staticmethod
    def create_connection():
        server = "DESKTOP-F4IH55C"
        db = "Ebay"
        return pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=' + server + ';'
            'DATABASE=' + db + ';'
            'Trusted_Connection=yes'
        )

# class DBConnection(object):
#     conn = None
#     def getInstance(self):
#         server = "DESKTOP-F4IH55C"
#         db = "test"
#         return pyodbc.connect(
#             'DRIVER={ODBC Driver 17 for SQL Server};'
#             'SERVER=' + server + ';'
#                                  'DATABASE=' + db + ';'
#                                                     'Trusted_Connection=yes'
#         )
#
#     def __str__(self):
#         return 'Database connection object'
#
# # server = "DESKTOP-F4IH55C"
# # db = "test"
# # conn = pyodbc.connect(
# #     'DRIVER={ODBC Driver 17 for SQL Server};'
# #     'SERVER=' + server + ';'
# #     'DATABASE=' + db + ';'
# #     'Trusted_Connection=yes'
# # )
# #
# # def read(conn):
# #     print("read")
# #     cursor = conn.cursor()
# #     cursor.execute("SELECT * FROM dummy1")
# #     for row in cursor:
# #         print(f'row = {row}')
# #     print()
# #
# # read(conn)
