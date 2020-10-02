from lib.operation import DB
from datetime import datetime


class ItemLog:
    def __init__(self,
                 item_id,
                 quantity):
        self.item_id = item_id
        self.quantity = quantity

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def insert(self):
        list_values = {
            'item_id': self.item_id,
            'quantity_sold': self.quantity,
            'adate': int(datetime.timestamp(datetime.now()))
        }
        DB.insert('item_selling_log', list_values)

    @staticmethod
    def get_properties_names():
        list_properties_names = []
        list_properties_names.extend(
            ('item_id',
             'quantity_sold',
             'adate')
        )
        return list_properties_names
