#! /usr/bin/env python3
# coding : utf-8

""" The aim of this module is to get all the products from the API,
and clean all the data"""

import requests
from settings.constants import CATEGORY, SIZE


class LoadingProduct:
    """ This class will allow us to 'get' from the API
    response with data in .json format """

    def __init__(self):
        
        self.url = "https://fr.openfoodfacts.org/cgi/search.pl"
        self.params = {
            "action" : "process",
            "tagtype_0" : "categories",
            "tag_contains_0" : "contains",
            "tag_0" : CATEGORY,
            "sort_by": "unique_scans_n",
            "page_size" : SIZE,
            "json" : 1
        } 
        #those are the parameters to customize what follows the URL


    def get_product(self):
        """ This method allows us to customize the URL 
        for our get requests at the OFF API """

        self.params["tag_0"] = CATEGORY
        self.params["page_size"] = SIZE

        # We apply the 'get' method to gather the data we want
        #according to the parameters
        response = requests.get(self.url, params=self.params)

        #We will now transform our response into a .json format
        self.data_dict = response.json()

        #empty list which will take all the data in
        list_of_products = []

        #for..in loop to append all data into our list_of_products=[]
        for product in self.data_dict["products"]:
            # we  add our products into our list_of_products
            list_of_products.append(product)
            
            #print(list_of_products) test

            return self.data_dict["products"]

            #show me what we gathered into the list
            

    def check_connexion_to_API(self):
        """ Method to check if url and parameters are set well """
        
        response = requests.get(self.url, params=self.params)
        print(response) # show me if the return is 200


def main():
    download_data = LoadingProduct()
    download_data.check_connexion_to_API()
    download_data.get_product()
    
    #products = []
    #products.download_data(CATEGORY, SIZE)
    


if __name__ == "__main__":
    main()


        #for product in products:
            #print(product["brands"])


##data = response.json()

#Nous sauvegarderons les données des produits récupérés
# dans la variable 'product' qui est une liste
##products = []

#On fait une boucle POUR les produits DANS data["clé"]: (.json)
#On ajoute ses données dans la liste 'products'


##for product in products:
    ##print(product["brands"])