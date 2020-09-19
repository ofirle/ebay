import pyodbc

conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0}'"
    "Server=DESKTOP-F4IH55C;"
    "Database=test;"
    "Trusted_connection=yes"
)

read(conn)

def read(conn):
    print ("read")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM dummy1")
    for row in cursor:
        print(f'row = {row}')
    print()



