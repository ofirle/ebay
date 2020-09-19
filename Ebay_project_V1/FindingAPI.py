from lxml import etree
import requests


def findItemsByKeywords(config_object, keywords, affiliate=None, buyerPostalCode=None, paginationInput=None,
                        sortOrder=None, encoding="JSON", itemFilter=None, aspectFilter=None,
                        domainFilter=None, outputSelector=None, ):
    root = etree.Element("findItemsByKeywords",
                         xmlns="http://www.ebay.com/marketplace/search/v1/services")

    keywords_elem = etree.SubElement(root, "keywords")
    keywords_elem.text = keywords

    # affiliate is a dict
    if affiliate:
        affiliate_elem = etree.SubElement(root, "affiliate")
        for key in affiliate:
            key_elem = etree.SubElement(affiliate_elem, key)
            key_elem.text = affiliate[key]

    if buyerPostalCode:
        buyerPostalCode_elem = etree.SubElement(root, "buyerPostalCode")
        buyerPostalCode_elem.text = buyerPostalCode

    # paginationInput is a dict
    if paginationInput:
        paginationInput_elem = etree.SubElement(root, "paginationInput")
        for key in paginationInput:
            key_elem = etree.SubElement(paginationInput_elem, key)
            key_elem.text = paginationInput[key]

    # itemFilter is a list of dicts
    if itemFilter:
        for item in itemFilter:
            itemFilter_elem = etree.SubElement(root, "itemFilter")
            for key in item:
                key_elem = etree.SubElement(itemFilter_elem, key)
                key_elem.text = item[key]

    # sortOrder
    if sortOrder:
        sortOrder_elem = etree.SubElement(root, "sortOrder")
        sortOrder_elem.text = sortOrder

    # # aspectFilter is a list of dicts
    # for item in aspectFilter:
    #     aspectFilter_elem = etree.SubElement(root, "aspectFilter")
    #     for key in item:
    #         key_elem = etree.SubElement(aspectFilter_elem, key)
    #         key_elem.text = item[key]
    #
    # # domainFilter is a list of dicts
    # for item in domainFilter:
    #     domainFilter_elem = etree.SubElement(root, "domainFilter")
    #     for key in item:
    #         key_elem = etree.SubElement(domainFilter_elem, key)
    #         key_elem.text = item[key]

    # outputSelector is a list
    # for item in outputSelector:
    #     outputSelector_elem = etree.SubElement(root, "outputSelector")
    #     outputSelector_elem.text = item

    request = etree.tostring(root, pretty_print=True)
    response = get_response(findItemsByKeywords.__name__, request, encoding, config_object)
    print('response:', response)
    return response


def parse_findItemsByKeywords(response):
    res_output = response['findItemsByKeywordsResponse']
    # pprint.pprint(res_output)
    totalEntries = int(res_output[0]['paginationOutput'][0]['totalEntries'][0])
    totalPages = int(res_output[0]['paginationOutput'][0]['totalPages'][0])
    search_results = res_output[0]['searchResult'][0]['item']
    # pprint.pprint(search_results)

    print('\n*** {} listings were found in {} pages [Presenting {} items] ***'.format(totalEntries, totalPages,
                                                                                      len(search_results)))

    for idx, item in enumerate(search_results):
        item_title = item['title'][0]
        item_category = item['primaryCategory'][0]['categoryName'][0]
        item_category_ID = item['primaryCategory'][0]['categoryId'][0]
        item_price = item['sellingStatus'][0]['currentPrice'][0]['__value__']
        item_location = item['location'][0]
        item_shipping_type = item['shippingInfo'][0]['shippingType'][0]
        item_shipping_cost = item['shippingInfo'][0]['shippingServiceCost'][0]['__value__']

        print('\n{}) Title:{}'.format(idx + 1, item_title))
        print('- Category: {} [ID:{}]'.format(item_category, item_category_ID))
        print('- Price: {}$'.format(item_price))
        print('- Location: {}'.format(item_location))
        if item_shipping_type == 'Free':
            print('- Shipping cost: Free')
        else:
            print('- Shipping cost: {}$'.format(item_shipping_cost))


def get_response(operation_name, data, encoding, config_object, **headers):
    app_name = config_object['Production_Keys']['AppID']
    endpoint = 'http://svcs.ebay.com/services/search/FindingService/v1'
    endpoint = config_object['Production_endpoints']['finding']

    http_headers = {
        "X-EBAY-SOA-OPERATION-NAME": operation_name,
        "X-EBAY-SOA-SECURITY-APPNAME": app_name,
        "X-EBAY-SOA-RESPONSE-DATA-FORMAT": encoding}

    response = requests.post(endpoint, data=data, headers=http_headers)

    if encoding == "JSON":
        return response.json()
    else:
        return response.text
