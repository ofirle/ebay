from configparser import ConfigParser
from Api.GetCategories import getCategories
from Api.GetItemsByCategory import getItemsByCategory
from Api.GetItemTransactions import getItemTransactions
import xml.etree.ElementTree as ET
from Categories.Category import Category
from Items.Item import Item

# Read config.ini file
config_object = ConfigParser()
config_object.read("Resources.ini")


def main(request_type):
    if request_type == 'CATEGORIES':
        xml = (getCategories(config_object, encoding="XML"))
        root = ET.fromstring(xml)
        category_array = root.find('{urn:ebay:apis:eBLBaseComponents}CategoryArray')
        for category in category_array:
            # category.handle_xml_response(category)
            try:
                best_offer_enabled = category.find('{urn:ebay:apis:eBLBaseComponents}BestOfferEnabled').text
            except:
                best_offer_enabled = "false"
            try:
                auto_pay_enabled = category.find('{urn:ebay:apis:eBLBaseComponents}AutoPayEnabled').text
            except:
                auto_pay_enabled = "false"
            try:
                leaf_category = category.find('{urn:ebay:apis:eBLBaseComponents}LeafCategory').text
            except:
                leaf_category = "false"
            category_id = category.find('{urn:ebay:apis:eBLBaseComponents}CategoryID').text
            category_level = category.find('{urn:ebay:apis:eBLBaseComponents}CategoryLevel').text
            category_name = category.find('{urn:ebay:apis:eBLBaseComponents}CategoryName').text
            category_parent_id = category.find('{urn:ebay:apis:eBLBaseComponents}CategoryParentID').text
            category_object = Category(best_offer_enabled,
                                       auto_pay_enabled,
                                       category_id,
                                       category_level,
                                       category_name,
                                       category_parent_id, leaf_category)
            category_object.insert()
    elif request_type == 'ITEMS_BY_CATEGORY':
        xml = (getItemsByCategory(config_object, '37908', '1', '1'))
        root = ET.fromstring(xml)
        items_array = root.find('{http://www.ebay.com/marketplace/search/v1/services}searchResult')
        for item in items_array:
            item_id = item.find('{http://www.ebay.com/marketplace/search/v1/services}itemId').text
            title = item.find('{http://www.ebay.com/marketplace/search/v1/services}title').text
            primary_category = item.find('{http://www.ebay.com/marketplace/search/v1/services}primaryCategory')
            try:
                primary_category_id = primary_category.find('{http://www.ebay.com/marketplace/search/v1/services}categoryId').text
            except:
                primary_category_id = None

            listing_info = item.find('{http://www.ebay.com/marketplace/search/v1/services}listingInfo')
            try:
                listing_start_time = listing_info.find(
                    '{http://www.ebay.com/marketplace/search/v1/services}startTime').text
            except:
                listing_start_time = None
            try:
                listing_top_rated = listing_info.find(
                    '{http://www.ebay.com/marketplace/search/v1/services}topRatedListing').text
            except:
                listing_top_rated = None

            condition = root.find('{http://www.ebay.com/marketplace/search/v1/services}condition')
            try:
                condition_id = condition.find('{http://www.ebay.com/marketplace/search/v1/services}conditionId').text
            except:
                condition_id = 0
            selling_status = root.find('{http://www.ebay.com/marketplace/search/v1/services}sellingStatus')
            try:
                selling_state = selling_status.find(
                    '{http://www.ebay.com/marketplace/search/v1/services}sellingStatus').text
            except:
                selling_state = None

            item_object = Item(item_id,
                               title,
                               primary_category_id,
                               listing_start_time,
                               condition_id,
                               listing_top_rated,
                               selling_state)
            print(item_object)
            item_object.insert()
            # try:
            #     best_offer_enabled = item.find('{urn:ebay:apis:eBLBaseComponents}BestOfferEnabled').text
            # except:
            #     best_offer_enabled = "false"
            # try:
            #     auto_pay_enabled = item.find('{urn:ebay:apis:eBLBaseComponents}AutoPayEnabled').text
            # except:
            #     auto_pay_enabled = "false"
            # try:
            #     leaf_category = item.find('{urn:ebay:apis:eBLBaseComponents}LeafCategory').text
            # except:
            #     leaf_category = "false"
            # category_id = item.find('{urn:ebay:apis:eBLBaseComponents}CategoryID').text
            # category_level = item.find('{urn:ebay:apis:eBLBaseComponents}CategoryLevel').text
            # category_name = item.find('{urn:ebay:apis:eBLBaseComponents}CategoryName').text
            # category_parent_id = item.find('{urn:ebay:apis:eBLBaseComponents}CategoryParentID').text

        # print(xml)
    elif request_type == 'ITEM_TRANSACTIONS':
        xml = (getItemTransactions(config_object, '254504665677'))
        root = ET.fromstring(xml)
        for elem in root:
            print(elem.tag)


if __name__ == '__main__':
    # request_type = sys.argv[1]
    request_type = "ITEM_TRANSACTIONS"
    main(request_type)
