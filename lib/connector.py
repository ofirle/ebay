import pyodbc
from lib.config.server_conf import *


class DBConnector:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = cls.create_connection()
        return cls.__instance

    @staticmethod
    def create_connection():
        return pyodbc.connect(
            'DRIVER={' + db_driver + '};'
            'SERVER=' + db_server + ';'
            'DATABASE=' + db_name + ';'
            'Trusted_Connection=yes'
        )