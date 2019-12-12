#! /usr/bin/env python3
# coding : utf-8

import requests

class ProductDownloadBiscuit:
    """ This class has the responsibility to download data from
    OpenFoodFact API """

    def __init__(self):
        self._url = "https://fr.openfoodfacts.org/cgi/search.pl"

        self._params = {
            "action": "process",
            "tagtype_0": "categories",
            "tag_contains_0": "contains",
            "tag_0": "biscuits",
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

        self.products = self.data_product["products"]

        for product in self.products:
            print(product["nutrition_grade_fr"], product["product_name"], product["categories"], product["code"], product["stores"], product["url"])
            self.products_list.append(product)

            return self.products_list


    def clean_data_product(self, product):
        """ 
        On déclare les champs qu'on veut récupérer dans un tuple 'fields'
        POUR field IN fields:
        Si le FIELD n'est pas dans le produit ou pas présence de product[field]:
        return FALSE
        ou 
        return TRUE

        Nous regardons si dans la liste de produit nous avons bien les champs cherché;
        Si les champs sont présent : retourne True
        Si les champs sont pas présent: retourne False
        Vérifier  si les champs des produits ne sont pas vide
        """
        clean_products_list = []

        fields = ("product_name","nutrition_grade_fr","categories","code", "stores", "url")
        
        for fields in self.products_list:

            if fields not in self.products_list or not self.products_list[fields]:

                clean_products_list.append(Product(**product))


                
            else:
                continue

    def is_valid(self, product):
        fields = ("product_name", "nutrition_grade_fr", "stores", "url")
        for field in fields:
            if field not in product or not product[field]:
                print("-->DEBUG", product.get('product_name'), f"{field} not present or empty")
                return False
            return True

        cleaned_products = []

        for product in self.products_list:
            try:
                cleaned_products.append(Product(**product))

            except TypeError as e:

                print("TypeError", e)
                print(cleaned_products)


def main():
    data = ProductDownloadBiscuit()
    data.check_connexion()
    data.get_product_list()
    data.clean_data_product()

if __name__ == "__main__":
    main()