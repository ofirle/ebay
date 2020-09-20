# from Categories.Category import Category
import xml.etree.ElementTree as ET
from DB.operation import DB

class Category:
    def __init__(self,
                 best_offer_enabled,
                 auto_pay_enabled,
                 category_id,
                 category_level,
                 category_name,
                 category_parent_id,
                 leaf_category):
        self.best_offer_enabled = best_offer_enabled
        self.auto_pay_enabled = auto_pay_enabled
        self.category_id = category_id
        self.category_level = category_level
        self.category_name = category_name
        self.category_parent_id = category_parent_id
        self.leaf_category = leaf_category

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def insert(self):
        # best_offer_enabled =
        # auto_pay_enabled =
        # leaf_category =
        # category_id = self.category_id
        # category_level = self.category_level
        # category_name = self.category_name
        # category_parent_id = self.category_parent_id
        list_values = {
            'best_offer_enabled': '1' if self.best_offer_enabled == 'true' else '0',
            'auto_pay_enabled': '1' if self.auto_pay_enabled == 'true' else '0',
            'leaf_category': '1' if self.leaf_category == 'true' else '0',
            'category_id': self.category_id,
            'category_level': self.category_level,
            'category_name': self.category_name,
            'category_parent_id': self.category_parent_id
        }
        # list_values = []
        # list_values.extend((best_offer_enabled, auto_pay_enabled, leaf_category, category_id, category_level, category_name, category_parent_id))
        DB.insert('Categories', list_values)


    @staticmethod
    def get_properties_names():
        list_properties_names = []
        list_properties_names.extend(
            ('best_offer_enabled',
             'auto_pay_enabled',
             'leaf_category',
             'category_id',
             'category_level',
             'category_name',
             'category_parent_id')
        )
        return list_properties_names


    def handle_xml_response(xml_requst: ET.Element):
        try:
            best_offer_enabled = xml_requst.find('{urn:ebay:apis:eBLBaseComponents}BestOfferEnabled').text
        except:
            best_offer_enabled = "false"
        try:
            auto_pay_enabled = xml_requst.find('{urn:ebay:apis:eBLBaseComponents}AutoPayEnabled').text
        except:
            auto_pay_enabled = "false"
        try:
            leaf_category = xml_requst.find('{urn:ebay:apis:eBLBaseComponents}LeafCategory').text
        except:
            leaf_category = "false"
        category_id = xml_requst.find('{urn:ebay:apis:eBLBaseComponents}CategoryID').text
        category_level = xml_requst.find('{urn:ebay:apis:eBLBaseComponents}CategoryLevel').text
        category_name = xml_requst.find('{urn:ebay:apis:eBLBaseComponents}CategoryName').text
        category_parent_id = xml_requst.find('{urn:ebay:apis:eBLBaseComponents}CategoryParentID').text
        category_object = Category(best_offer_enabled, auto_pay_enabled, category_id, category_level, category_name,
                                   category_parent_id, leaf_category)
        print(category_object)
        category_object.insert()
