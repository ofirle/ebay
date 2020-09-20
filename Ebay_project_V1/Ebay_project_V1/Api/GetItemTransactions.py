import json
from lxml import etree
from xml.etree import ElementTree as ET
from io import BytesIO
import requests


def getItemTransactions(config_object, item_id):

    root = ET.Element("GetItemTransactionsRequest", xmlns="urn:ebay:apis:eBLBaseComponents")
    IncludeContainingOrder = ET.SubElement(root, "IncludeContainingOrder")
    IncludeContainingOrder.text = "true"
    DetailLevel = ET.SubElement(root, "DetailLevel")
    DetailLevel.text = "ReturnAll"
    IncludeVariations = ET.SubElement(root, "IncludeVariations")
    IncludeVariations.text = "true"
    Credentioals = ET.SubElement(root, "RequesterCredentials")
    TokenElement = ET.SubElement(Credentioals, "eBayAuthToken")
    TokenElement.text = 'AgAAAA**AQAAAA**aAAAAA**H5hKXw**nY+sHZ2PrBmdj6wVnY+sEZ2PrA2dj6AHl4GkAJGFpwudj6x9nY+seQ**hmYGAA**AAMAAA**I6cGW3QDc5h45yOaJ95jG9ZN7zn+WbV6xztgTcSFhB2YZQjvRB61DorP75uS1AviaZ7Doe7Dqc9CtRFsiWaTwazV06HZYXnE8jKYBGa5ROyU18nuyv0BYKPbHftqgmMEcUK2eSqzDXodjTo6ZbCl74mMgkVg/MoxDUV/51wb8sCz2p1vMq7Y6zbdpo12DBZW+0qyNRCsuLEKznLGBJd3zADs3zbmFdgG7HGLKMrUb0v9kAeKKMaKfBodrHrw/MxR0HR71T9jWiFqqdPcciQ61tZ9R1ob53A2Jf++o/i5Xa//5mIY7ClTDt7sjeNIi3LVNfOsHOMdJSepzu62Q+8xBLB4y4nrvDtfXcXLVr5nOxx/uo+0xJck2P5nyYHPbZVCZaGoOOa8CqT6nWn7hB59gDykQhv/0mQPnWa2pg8FK1KVcaDMFn9wBcSLEAi6RnFLkQaXHVcDIA3M2J87333EgcupEKYteJlLFlPN6lEHfI1Aj/3dA/UEvk0wDCRiAeJ3l4kcEqP50mueqevBodXVDonf9kztAJJAUCzgVzDOdyWW8fl6Q0HPDaomD2zhf5iFgxNKCZMTZbhIYHdCkT38Kalz4XHSoa1pbVu9YlbORy1jkwGq7EBhIzxqTudLP5OJDjsNizV1funyKw9OqXvAurAvuT76Olro9aHrdxzXcvfWQTEDcezeBZKISrnuU7hWbcmL8x/Envd6eCgWMY93UW6kHV/Mi5/gcJmlMVtjt0aWHCRNMWpnyK/mlR3OdqDw'
    itemId_elem = ET.SubElement(root, "ItemID")
    itemId_elem.text = item_id

    f = BytesIO()
    et = ET.ElementTree(root)
    et.write(f, encoding='utf-8', xml_declaration=True) 
    request = f.getvalue()

    response = get_response(request, config_object)
    # print('response:', response)
    return response

def get_response(data, config_object):
    endpoint = config_object['Production_endpoints']['trading']

    http_headers = {
        "X-EBAY-API-SITEID": '0',
        "X-EBAY-API-COMPATIBILITY-LEVEL": '967',
        "X-EBAY-API-CALL-NAME": "GetItemTransactions",
        "X-EBAY-API-CERT-NAME": 'PRD-c8eaa0db154a-19d8-45a8-a612-b1f9',
        "X-EBAY-API-DEV-NAME": '254cebd5-d713-47fd-8527-925ebb25a90e',
        "X-EBAY-API-APP-NAME": 'OfirLevy-test-PRD-6c8eaa0db-1ff29598'
        }

    response = requests.post(endpoint, data=data, headers=http_headers)
    return response.text
