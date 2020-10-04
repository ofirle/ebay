from Api.GetCategories import getCategories
from Api.GetItemsByCategory import getItemsByCategory
from Api.GetItem import getItem


def main(request_type):
    if request_type == 'CATEGORIES':
        getCategories()
    elif request_type == 'ITEMS_BY_CATEGORY':
        for i in range(26, 50):
            print("getItemsByCategory: " + str(i))
            getItemsByCategory('9355', '100', str(i))
    elif request_type == 'ITEM':
        getItem('254504665677')


if __name__ == '__main__':
    # request_type = sys.argv[1]
    request_type = "ITEMS_BY_CATEGORY"
    main(request_type)
