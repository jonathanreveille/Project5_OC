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
            "page_size": 500, #need to implement cleaning method to go above 90 for Pizza
            "json": 1
            }


    def check_connexion(self):
        """This method is to download all data needed 
        from the URL, output = if <Response 200>params and url are set well """

        self.response = requests.get(self._url, params=self._params)
        if False:
            print("<<Not connected to API>>")
        else:
            print("<<Connected to API>>")
            return self.response


    def get_product_list(self):
        """ This method is to transform what we received 
        from the API into a .json format into a mutable list"""

        self.data_product = self.response.json() #put the .json into self.data_product
        #DEBUG print(type(self.data_product)) #dict
        
        self.products_list = []

        self.products = self.data_product["products"]

        for product in self.products:
            try:
            #self.products_list.append(product)
                self.products_list.append(Product(**product))
            except TypeError as e:
                print("Type of error : ", e)

            return self.products_list



class Product:
    """ This class contains all information about product """

    def __init__(self, code, url, product_name, stores, brands, nutrition_grade_fr, ingredients, categories, **kwargs):
        
        self.code = code
        self.name = product_name
        self.url = url
        self.brands = brands
        self.nutrition_grade = nutrition_grade_fr
        self.category = []
        self.ingredients = ingredients
        # Table association ProductStore?
        self.stores = []

        for store in stores.split(","):
            self.stores.append(Store(store.capitalize().strip()))
        
        for category in categories.split(","):
            self.category.append(Category(category.capitalize().strip()))


    def __repr__(self):
        return f"Product(name: {self.name})"


    def is_valid(self, product, **kwargs):
        """ This method is to check if our list has all the data entries we need to create our objects """

        is_valid = True

        parameters = ("product_name","nutrition_grade_fr",\
                "categories", "code", "stores", "brands",\
                "code", "url")

        for parameter in parameters:
        
            if parameter not in product or not product[parameter]:# We check if we have the corresponding keys (parameters) in dict
                is_valid = False
                break

            if not product[parameter]:  # On vérifie que ça contient un truc
                is_valid = False
                break

        return is_valid


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
    data.get_product_list()
    #data.cleaning_product_list()

if __name__ == "__main__":
    main()





            # print("DEBUG", \
            #     product["nutrition_grade_fr"],product["code"],\
            #     product["categories"], product["product_name"],\
            #     product["stores"], product["url"], product["ingredients"])
            #     # ==> return the list of downloaded product

    # def cleaning_product_list(self):
    #     """ 
    #     Nous regardons si dans la liste de produit nous avons bien les champs cherchés;
    #     Si les champs sont pas présent: retourne False
    #     Si les champs sont présent : retourne True
    #     Vérifier  si les champs des produits ne sont pas vides
    #     """
    #     self.cleaned_product_list = [] # liste vide

    #     #boucle, pour chaque produit dans ma liste de produit
    #     for product in self.products_list:
    #         try: 
    #             # ajoute les produits dans ma liste "propre" de produit où les infos sont remplies(avec toute les données nécéssaires
    #             # on ajoute les produits triés et on les créer avec la class Product
    #             # si erreur (traduction : si manquant) alors exception levée
    #             self.cleaned_product_list.append(Product(**product)) 
    #         except TypeError as e:
    #             print("TypeError, missing a value maybe...", e)

    #         print(self.cleaned_product_list)
    #         return self.cleaned_product_list




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