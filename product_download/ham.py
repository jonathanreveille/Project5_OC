#! /usr/bin/env python3
# coding : utf-8

import requests

class ProductDownloadHam:
    """ This class has the responsibility to download data from
    OpenFoodFact API """

    def __init__(self):
        self._url = "https://fr.openfoodfacts.org/cgi/search.pl"

        self._params = {
            "action": "process",
            "tagtype_0": "categories",
            "tag_contains_0": "contains",
            "tag_0": "Produits à teneur réduite en sel",
            "sort_by": "unique_scans_n",
            "page_size": 100, #need to implement cleaning method to go above 90 for Pizza
            "json": 1
            }

    def check_connexion(self):
        """This method is to download all data needed 
        from the URL, output = if <Response 200>params and url are set well """

        self.response = requests.get(self._url, params=self._params)
        print(self.response)


    def get_product_list(self):
        """ This method is to transform what we received 
        from the API into a .json format into a mutable list"""

        self.data_product = self.response.json() #put the .json into self.data_product
        #DEBUG print(type(self.data_product)) #dict
        
        self.products_list = []

        self.products_list = self.data_product["products"]

        for product in self.products_list:
            print(product["nutrition_grade_fr"], product["product_name"], product["categories"], product["code"], product["stores"], product["url"])


    def clean_data_product(self):
        """ This method is to clean all the data that 
        we gathered from .json data.
        We will eliminate all products that has None 
        values in our parameters """
        #for product in self.product_downloaded[0]:
            #print(product)
        pass
        

def main():
    data = ProductDownloadHam()
    data.check_connexion()
    data.get_product_list()
    data.clean_data_product()

if __name__ == "__main__":
    main()