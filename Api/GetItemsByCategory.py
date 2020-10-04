from lib.config.credentials import *
from xml.etree import ElementTree as ET
from io import BytesIO
from Api.GetItem import getItem
import requests


def getItemsByCategory(category_id, entries_per_page, page_number):

    root = ET.Element("findItemsByCategoryRequest", xmlns="http://www.ebay.com/marketplace/search/v1/services")
    pagination_input = ET.SubElement(root, "paginationInput")
    entries_per_page_elem = ET.SubElement(pagination_input, "entriesPerPage")
    item_filter = ET.SubElement(root, "itemFilter")
    item_filter_name = ET.SubElement(item_filter, "name")
    item_filter_name.text = "HideDuplicateItems"
    item_filter_value = ET.SubElement(item_filter, "value")
    item_filter_value.text = "true"
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
    if items_array is None or len(items_array) == 0:
        print("No Items")
        return
    for idx, item in enumerate(items_array):
        item_id = item.find('{http://www.ebay.com/marketplace/search/v1/services}itemId').text
        getItem(item_id)
        print("index: " + str(idx) + " - item_id: " + item_id)
