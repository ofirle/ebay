from lib.config.credentials import *
from xml.etree import ElementTree as ET
from io import BytesIO
from Items.Item import Item
import requests


def getItemsByCategory(category_id, entries_per_page, page_number):

    root = ET.Element("findItemsByCategoryRequest", xmlns="http://www.ebay.com/marketplace/search/v1/services")
    pagination_input = ET.SubElement(root, "paginationInput")
    entries_per_page_elem = ET.SubElement(pagination_input, "entriesPerPage")
    entries_per_page_elem.text = entries_per_page
    page_number_elem = ET.SubElement(pagination_input, "pageNumber")
    page_number_elem.text = page_number
    category_id_elem = ET.SubElement(root, "categoryId")
    category_id_elem.text = category_id

    et = ET.ElementTree(root)
    f = BytesIO()
    et.write(f, encoding='utf-8', xml_declaration=True)
    response = get_response(f.getvalue())
    handle_xml_response(response)


def get_response(data):
    endpoint = 'https://svcs.ebay.com/services/search/FindingService/v1'

    http_headers = {
        "X-EBAY-SOA-SECURITY-APPNAME": get_app_name(),
        "X-EBAY-SOA-OPERATION-NAME": "findItemsByCategory"
    }

    response = requests.post(endpoint, data=data, headers=http_headers)
    return response.text


def handle_xml_response(xml_string):
    root = ET.fromstring(xml_string)
    items_array = root.find('{http://www.ebay.com/marketplace/search/v1/services}searchResult')
    for item in items_array:
        item_id = item.find('{http://www.ebay.com/marketplace/search/v1/services}itemId').text
        title = item.find('{http://www.ebay.com/marketplace/search/v1/services}title').text
        primary_category = item.find('{http://www.ebay.com/marketplace/search/v1/services}primaryCategory')
        try:
            primary_category_id = primary_category.find(
                '{http://www.ebay.com/marketplace/search/v1/services}categoryId').text
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
                '{http://www.ebay.com/marketplace/search/v1/services}sellingState').text
        except:
            selling_state = None

        item_object = Item(item_id,
                           title,
                           primary_category_id,
                           listing_start_time,
                           condition_id,
                           listing_top_rated,
                           selling_state)
        item_object.insert()
