import json
from lxml import etree
from xml.etree import ElementTree as ET
from io import BytesIO
import requests


def getItemsByCategory(config_object, category_id, entries_per_page, page_number):

    root = ET.Element("findItemsByCategoryRequest", xmlns="http://www.ebay.com/marketplace/search/v1/services")
    pagination_input = ET.SubElement(root, "paginationInput")
    entries_per_page_elem = ET.SubElement(pagination_input, "entriesPerPage")
    entries_per_page_elem.text = entries_per_page
    page_number_elem = ET.SubElement(pagination_input, "pageNumber")
    page_number_elem.text = page_number
    category_id_elem = ET.SubElement(root, "categoryId")
    category_id_elem.text = category_id

    f = BytesIO()
    et = ET.ElementTree(root)
    et.write(f, encoding='utf-8', xml_declaration=True) 
    request = f.getvalue()

    response = get_response(request, config_object)
    return response

def get_response(data, config_object):
    endpoint = config_object['Production_endpoints']['items_by_category']

    http_headers = {
        "X-EBAY-SOA-SECURITY-APPNAME": "OfirLevy-test-PRD-6c8eaa0db-1ff29598",
        "X-EBAY-SOA-OPERATION-NAME": "findItemsByCategory"
    }

    response = requests.post(endpoint, data=data, headers=http_headers)
    return response.text
