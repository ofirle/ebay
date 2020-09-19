import json
import pprint
from configparser import ConfigParser
from FindingAPI import parse_findItemsByKeywords, findItemsByKeywords
from GetItemTransactions import getItemTransactions
from CategoryAPI import getCategoryTree

# Read config.ini file
config_object = ConfigParser()
config_object.read("Resources.ini")


def main():

    # ----------------------------------------------------------------------#
    # ---------------------------- Finding API -----------------------------#
    # ----------------------------------------------------------------------#


    """
    # ----  Load an exist response JSON ---- #
    with open('findItemsByKeywords_json.txt') as json_file:
        response = json.load(json_file)

    parse_findItemsByKeywords(response)

    # ----  Run a API request  ---- #
    response = findItemsByKeywords(config_object, keywords="iphone", encoding="JSON",
                                   paginationInput={"entriesPerPage": "5", "pageNumber": "1"})
    parse_findItemsByKeywords(response)

    # save the response to txt file
    with open('findItemsByKeywords_json.txt', 'w') as outfile:
        json.dump(response, outfile)

    """

    # ----------------------------------------------------------------------#
    # ---------------------------- Category API ----------------------------#
    # ----------------------------------------------------------------------#

    # pprint.pprint(findItemsByKeywords(config_object, category_id=1, encoding='JSON'))
    # pprint.pprint(findItemsByKeywords(config_object, keywords="iphone", encoding="JSON",
    #                                paginationInput={"entriesPerPage": "5", "pageNumber": "1"}))
    print(getItemTransactions(config_object, itemId="224041251095", encoding="XML",
                                   paginationInput={"entriesPerPage": "5", "pageNumber": "1"}))


if __name__ == '__main__':
    main()
