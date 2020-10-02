# from Categories.Category import Category
import xml.etree.ElementTree as ET
from lib.operation import DB
from datetime import datetime

class Item:
    def __init__(self,
                 item_id,
                 title,
                 primary_category_id,
                 listing_start_time,
                 condition_id,
                 top_rated_listing,
                 selling_state):
        self.item_id = item_id
        self.title = title
        self.primary_category_id = primary_category_id
        self.listing_start_time = listing_start_time
        self.condition_id = condition_id
        self.top_rated_listing = top_rated_listing
        self.selling_state = selling_state

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def insert(self):
        output_date = datetime.strptime(self.listing_start_time, "%Y-%m-%dT%H:%M:%S.%fZ")
        listing_start_time_timestamp = int(output_date.replace(microsecond=0).timestamp())
        list_values = {
            'item_id': self.item_id,
            'title': self.title,
            'primary_category_id': self.primary_category_id,
            'listing_start_time': listing_start_time_timestamp,
            'condition_id': self.condition_id,
            'top_rated_listing': '1' if self.top_rated_listing == 'true' else '0',
            'selling_state': self.selling_state
        }
        DB.insert('items', list_values)

    @staticmethod
    def get_properties_names():
        list_properties_names = []
        list_properties_names.extend(
            ('item_id',
             'title',
             'primary_category_id',
             'listing_start_time',
             'condition_id',
             'top_rated_listing',
             'selling_state')
        )
        return list_properties_names