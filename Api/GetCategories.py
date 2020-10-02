from lib.config.credentials import *
from xml.etree import ElementTree as ET
from Categories.Category import Category
from io import BytesIO
import requests


def getCategories():
    root = ET.Element("GetCategoriesRequest", xmlns="urn:ebay:apis:eBLBaseComponents")
    detail_level = ET.SubElement(root, "DetailLevel")
    detail_level.text = "ReturnAll"
    view_all_nodes = ET.SubElement(root, "ViewAllNodes")
    view_all_nodes.text = "true"
    credentials_element = ET.SubElement(root, "RequesterCredentials")
    token_element = ET.SubElement(credentials_element, "eBayAuthToken")
    token_element.text = get_credentials()

    f = BytesIO()
    et = ET.ElementTree(root)
    et.write(f, encoding='utf-8', xml_declaration=True)
    response = get_response(f.getvalue())
    handle_xml_response(response)


def get_response(data):
    endpoint = "https://api.ebay.com/ws/api.dll"
    http_headers = {
        "X-EBAY-API-SITEID": '0',
        "X-EBAY-API-COMPATIBILITY-LEVEL": '967',
        "X-EBAY-API-CALL-NAME": "GetCategories"
        }
    response = requests.post(endpoint, data=data, headers=http_headers)
    return response.text


def handle_xml_response(xml_string):
    root = ET.fromstring(xml_string)
    category_array = root.find('{urn:ebay:apis:eBLBaseComponents}CategoryArray')
    for category in category_array:
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
                                   category_parent_id,
                                   leaf_category)
        category_object.insert()
