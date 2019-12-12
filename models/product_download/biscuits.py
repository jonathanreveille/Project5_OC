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
            "page_size": 50, #need to implement cleaning method to go above 90 for Pizza
            "json": 1
            }


    def check_connexion(self):
        """ This method is to download all data needed 
        from the URL, output = if <Response 200>params 
        and url are set well """
        
        connexion = True
        self.response = requests.get(self._url, params=self._params)

        if connexion == False:
            print("<<Not connected to API>>")
        else:
            print("<<Connected to API>>")
            return self.response


    def get_data_from_API(self):
        """ This method is to transform what we received 
        from the API into a .json format into a mutable list"""

        self.data_product = self.response.json() #put the .json into self.data_product (data_prod =dict)

        return self.data_product


    def get_product_list(self):
        """  This method is to  add to our product list
        only the keys that we need. """

        self.products_list = []

        self.products_dict = self.data_product["products"]

        for product in self.products_dict:
            self.products_list.append(product["nutrition_grade_fr"])
            self.products_list.append(product["product_name"])
            self.products_list.append(product["categories"])
            self.products_list.append(product["code"])
            self.products_list.append(product["stores"])
            self.products_list.append(product["url"])

        return self.products_list
            #^^^THIS WORKS

    def cleaning_product_list(self):
        """ Nous regardons si dans la liste de produit nous avons bien les champs cherchés;
        Si les champs sont pas présent: retourne False
        Si les champs sont présent : retourne True
        Vérifier  si les champs des produits ne sont pas vides """

        self.cleaned_product_list = [] # liste vide

        #boucle, pour chaque produit dans ma liste de produit
        for product in self.products_list:

            try: 
                self.cleaned_product_list.append(Product(**product))
                
            except TypeError as e:
                print("TypeError, missing a parameter...", e)
                break

            return self.cleaned_product_list


class Product:
    """ This class contains all information about product """

    def __init__(self, code, product_name, url, brands, nutrition_grade_fr, categories, stores, **kwargs):
        
        self.code = code
        self.name = product_name
        self.url = url
        self.brands = brands
        self.nutriscore = nutrition_grade_fr
        self.categories = []
        # Table association ProductStore?
        self.stores = []

        for store in stores.split(","):
            self.stores.append(Store(store.capitalize().strip()))
        
        for category in categories.split(","):
            self.categories.append(Category(category.capitalize().strip()))


    def __repr__(self):

        return f"Product(name: {self.name}, {self.brands})"



class Store: 
    """ This class contains all information 
    about stores """

    def __init__(self, store):
        self.name = store

    def __repr__(self):
        f"Store (name: {self.name})"



class Category:
    """ This class contains all the information 
    about Categories """

    def __init__(self, category):
        self.name = category

    def __repr__(self):
        f"Category (name: {self.name})"



class Brand:
    """ This class contains all the information 
    about the Brands"""

    def __init__(self, brand):
        self.name = brand

    def __repr__(self):
        f"Brand(name: {self.name})"




def main():
    data = ProductDownloadBiscuit()
    data.check_connexion()
    data.get_data_from_API()
    data.get_product_list()
    data.cleaning_product_list()

if __name__ == "__main__":
    main()





            # print("DEBUG", \
            #     product["nutrition_grade_fr"],product["code"],\
            #     product["categories"], product["product_name"],\
            #     product["stores"], product["url"], product["ingredients"])
            #     # ==> return the list of downloaded product






    #                 #champs qu'on recherche
    #     fields = ("product_name","nutrition_grade_fr","categories",\
    #             "code", "stores", "brands","code", "url")

    #     #Pour chaque champs dans les fields
    #     for field in fields:
    #         #Si le field n'est pas présent dans la liste ou pas de self.products_list[field] présent:
    #         if field not in self.products_list or not self.products_list[field]:
    #             print("-->DEBUG", self.products.get('product_name'), f"{field} not present or empty")
    #             return False
    #         return True