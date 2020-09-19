from lxml import etree
import requests


def getCategoryTree(config_object, category_id, encoding):
    root = etree.Element("getCategoryTree",
                         xmlns="https://api.ebay.com/commerce/taxonomy/v1_beta/category_tree/0")

    categoryID_elem = etree.SubElement(root, "category_tree_id")
    categoryID_elem.text = str(category_id)

    request = etree.tostring(root, pretty_print=True)
    response = get_response(getCategoryTree.__name__, request, encoding, config_object)
    return response


def get_response(operation_name, data, encoding, config_object, **headers):
    app_name = config_object['Production_Keys']['AppID']
    endpoint = 'https://api.ebay.com/commerce/taxonomy/v1_beta/category_tree/0'

    http_headers = {
        "X-EBAY-SOA-OPERATION-NAME": operation_name,
        "X-EBAY-SOA-SECURITY-APPNAME": app_name,
        "X-EBAY-SOA-RESPONSE-DATA-FORMAT": encoding,
        "Accept-Encoding": "application/gzip"}  # he call returns the response with gzip compression

    response = requests.get(endpoint, data=data, headers=http_headers)

    if encoding == "JSON":
        return response.json()
    else:
        return response.text
