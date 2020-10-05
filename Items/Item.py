from lib.operation import DB
from datetime import datetime
from Items.ItemLog import ItemLog


class Item:
    def __init__(self,
                 item_id,
                 title,
                 description,
                 primary_category_id,
                 listing_start_time,
                 condition_id,
                 top_rated_listing,
                 quantity):
        self.item_id = item_id
        self.title = title
        if description is None:
            description = ''
        self.description = description
        self.primary_category_id = primary_category_id
        self.listing_start_time = listing_start_time
        self.condition_id = condition_id
        self.top_rated_listing = top_rated_listing
        self.quantity = quantity

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def insert(self):
        output_date = datetime.strptime(self.listing_start_time, "%Y-%m-%dT%H:%M:%S.%fZ")
        listing_start_time_timestamp = int(output_date.replace(microsecond=0).timestamp())
        list_values = {
            'item_id': self.item_id,
            'title': self.title,
            'description': self.description.replace("'", ""),
            'primary_category_id': self.primary_category_id,
            'listing_start_time': listing_start_time_timestamp,
            'condition_id': self.condition_id,
            'top_rated_listing': '1' if self.top_rated_listing == 'true' else '0',
            'adate': int(datetime.timestamp(datetime.now()))
        }
        DB.insert('items', list_values)
        item_selling_log_obj = ItemLog(self.item_id, self.quantity)
        item_selling_log_obj.insert()

    @staticmethod
    def get_properties_names():
        list_properties_names = []
        list_properties_names.extend(
            ('item_id',
             'title',
             'description',
             'primary_category_id',
             'listing_start_time',
             'condition_id',
             'top_rated_listing',
             'adate')
        )
        return list_properties_names

    @staticmethod
    def is_item_exist(item_id):
        return DB.is_exist('items', 'item_id', item_id)
