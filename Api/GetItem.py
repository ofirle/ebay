import json
from lxml import etree
from xml.etree import ElementTree as ET
from io import BytesIO
import requests


def getItem(item_id):
    response = get_response(item_id)
    return response

def get_response(config_object, item_id):
    endpoint = config_object['Production_endpoints']['item'] + item_id

    http_headers = {
        "Authorization": 'Bearer AgAAAA**AQAAAA**aAAAAA**H5hKXw**nY+sHZ2PrBmdj6wVnY+sEZ2PrA2dj6AHl4GkAJGFpwudj6x9nY+seQ**hmYGAA**AAMAAA**I6cGW3QDc5h45yOaJ95jG9ZN7zn+WbV6xztgTcSFhB2YZQjvRB61DorP75uS1AviaZ7Doe7Dqc9CtRFsiWaTwazV06HZYXnE8jKYBGa5ROyU18nuyv0BYKPbHftqgmMEcUK2eSqzDXodjTo6ZbCl74mMgkVg/MoxDUV/51wb8sCz2p1vMq7Y6zbdpo12DBZW+0qyNRCsuLEKznLGBJd3zADs3zbmFdgG7HGLKMrUb0v9kAeKKMaKfBodrHrw/MxR0HR71T9jWiFqqdPcciQ61tZ9R1ob53A2Jf++o/i5Xa//5mIY7ClTDt7sjeNIi3LVNfOsHOMdJSepzu62Q+8xBLB4y4nrvDtfXcXLVr5nOxx/uo+0xJck2P5nyYHPbZVCZaGoOOa8CqT6nWn7hB59gDykQhv/0mQPnWa2pg8FK1KVcaDMFn9wBcSLEAi6RnFLkQaXHVcDIA3M2J87333EgcupEKYteJlLFlPN6lEHfI1Aj/3dA/UEvk0wDCRiAeJ3l4kcEqP50mueqevBodXVDonf9kztAJJAUCzgVzDOdyWW8fl6Q0HPDaomD2zhf5iFgxNKCZMTZbhIYHdCkT38Kalz4XHSoa1pbVu9YlbORy1jkwGq7EBhIzxqTudLP5OJDjsNizV1funyKw9OqXvAurAvuT76Olro9aHrdxzXcvfWQTEDcezeBZKISrnuU7hWbcmL8x/Envd6eCgWMY93UW6kHV/Mi5/gcJmlMVtjt0aWHCRNMWpnyK/mlR3OdqDw',
        "Content-Type": 'application/json',
        "X-EBAY-C-MARKETPLACE-ID": "EBAY_US",
        "X-EBAY-C-ENDUSERCTX": 'contextualLocation=country=<2_character_country_code>,zip=<zip_code>,affiliateCampaignId=<ePNCampaignId>,affiliateReferenceId=<referenceId>'
        }
    response = requests.get(endpoint, headers=http_headers)
    return response.text
