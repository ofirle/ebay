from lib.config.credentials import *
from xml.etree import ElementTree as ET
from io import BytesIO
from Items.Item import Item
import requests


def getItem(item_id):
    root = ET.Element("GetSingleItemRequest", xmlns="urn:ebay:apis:eBLBaseComponents")
    item_id_elem = ET.SubElement(root, "ItemID")
    item_id_elem.text = item_id
    output_type_elem = ET.SubElement(root, "IncludeSelector")
    output_type_elem.text = "Details,TextDescription,ItemSpecifics"

    f = BytesIO()
    et = ET.ElementTree(root)
    et.write(f, encoding="utf-8", xml_declaration=True)
    response = get_response(f.getvalue())
    handle_xml_response(response)


def get_response(data):
    endpoint = 'https://open.api.ebay.com/shopping'

    http_headers = {
        "X-EBAY-API-APP-ID": get_app_name(),
        "X-EBAY-API-SITE-ID": "0",
        "X-EBAY-API-CALL-NAME": "GetSingleItem",
        "X-EBAY-API-VERSION": "863",
        "X-EBAY-API-REQUEST-ENCODING": "xml"
    }

    response = requests.post(endpoint, data=data, headers=http_headers)
    return response.text


def handle_xml_response(xml_string):
    root = ET.fromstring(xml_string)
    item = root.find('{urn:ebay:apis:eBLBaseComponents}Item')
    item_id = item.find('{urn:ebay:apis:eBLBaseComponents}ItemID').text
    description = item.find('{urn:ebay:apis:eBLBaseComponents}Description').text
    primary_category_id = item.find('{urn:ebay:apis:eBLBaseComponents}PrimaryCategoryID').text
    title = item.find('{urn:ebay:apis:eBLBaseComponents}Title').text
    listing_start_time = item.find('{urn:ebay:apis:eBLBaseComponents}StartTime').text
    try:
        condition_id = item.find('{urn:ebay:apis:eBLBaseComponents}ConditionID').text
    except:
        condition_id = 0
    try:
        listing_top_rated = item.find('{urn:ebay:apis:eBLBaseComponents}TopRatedListing').text
    except:
        listing_top_rated = None
    quantity_sold = item.find('{urn:ebay:apis:eBLBaseComponents}QuantitySold').text
    item_object = Item(item_id=item_id,
                       title=title,
                       description=description,
                       primary_category_id=primary_category_id,
                       listing_start_time=listing_start_time,
                       condition_id=condition_id,
                       top_rated_listing=listing_top_rated,
                       quantity=quantity_sold)
    item_object.insert()
