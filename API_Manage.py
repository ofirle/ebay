from configparser import ConfigParser
from Api.GetCategories import getCategories
from Api.GetItemsByCategory import getItemsByCategory
from Api.GetItem import getItem


def main(request_type):
    if request_type == 'CATEGORIES':
        getCategories()
    elif request_type == 'ITEMS_BY_CATEGORY':
        getItemsByCategory('37908', '30', '1')
    elif request_type == 'ITEM':
        getItem('254504665677')


if __name__ == '__main__':
    # request_type = sys.argv[1]
    request_type = "ITEMS_BY_CATEGORY"
    main(request_type)
