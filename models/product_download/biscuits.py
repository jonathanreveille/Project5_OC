#! /usr/bin/env python3
# coding : utf-8

from models.models import Product

import requests


class ProductDownload:
    """ This class has the responsibility to download data from
    OpenFoodFact API """

    def __init__(self):
        self.url = "https://fr.openfoodfacts.org/cgi/search.pl"

        self.params = {
            "action": "process",
            "tagtype_0": "categories",
            "tag_contains_0": "contains",
            "tag_0": "biscuits",
            "sort_by": "unique_scans_n",
            "page_size": 100, #need to implement cleaning method to go above 90 for Pizza
            "json": 1
            }

    def check_connexion(self):
        """ This method is to download all data needed 
        from the URL, output = if <Response 200>params 
        and url are set well """
        
        connexion = True

        self.response = requests.get(self.url, params=self.params)

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
        only the values from the keys that we need. """

        self.product_list = []
    
        for product in self.data_product["products"]:
            #self.product_list.append(product["nutrition_grade_fr"]) #causes problems ...
            self.product_list.append(product["product_name"])
            self.product_list.append(product["code"])
            self.product_list.append(product["brands"])
            self.product_list.append(product["stores"]) #need to seperate stores .split() .strip()
            self.product_list.append(product["url"])
            #self.product_list.append(product["categories"]) causes problems

        print(self.product_list) #DEBUGGING : to check what is 'récolté' in self.product_list

        return self.product_list #elements we seek for exists

    
    def is_valid(self, product):
        """ This method is to check if all the data that 
        we need are present and also, not empty """
        # vérifier que les données sont là,
        # vérifier si elles contiennent une donnée

        is_valid = True

        fields = ("product_name", "code", "brands", "stores", "url")

        for field in fields:

            if field not in self.data_product or self.data_product[field]:
                return is_valid == False

            return is_valid == True

                #print("DEBBUG", self.data_product.get("product_name"), "--> missing data on field :" f"{field}")


    def get_cleaned_list(self):
        """This method is to check """

        self.cleaned_product = []

        for product in self.data_product["products"]:

            if not is_valid(product):
                continue
                print("DEBUG", self.data_product.get('product_name'), "is present and has all info")

            if is_valid(product) == True:
            
                self.cleaned_product.append(Product(**product))

                

        return self.cleaned_product


# class ProductCleaner:

#     def __init__(self, products):
#         self.products = products
#         self.fields_to_keep = ["product_name", "code", "brands", "stores", "url"]
#         self.product_cleaned = []

#     def clean_product(self, products):
#         """ this method is to clean data from our list of data
#         delete from list fields that are not present
#         delete from list fields that have None value """

#         for product in products:
            
#             if set(self.fields_to_keep) <= set(product):
#                 if all([value for key, value in product.items() if key in self.fields_to_keep]):
#                     self.product_cleaned.append(
#                         {"code": product["code"],
#                         "name": product["product_name"],
#                         "nutriscore": product["nutrition_grade_fr"],
#                         "brands": product["brands"],
#                         "stores": product["stores"],
#                         "url": product["url"]}
#                         )









def main():
    a = ProductDownload
    a.check_connexion()
    a.get_data_from_API()
    a.get_product_list()

if __name__ == "__main__":
    main()


            # print("DEBUG", \
            #     product["nutrition_grade_fr"],product["code"],\
            #     product["categories"], product["product_name"],\
            #     product["stores"], product["url"], product["ingredients"])
            #     # ==> return the list of downloaded product



# is_valid = True 
#         for product in self.products_list:
#             for parameter in parameters:
#                 try:
#                     if parameter not in product or not product[parameter]:
#                         return is_valid == False

#                     elif parameter in product or product[parameter]:
#                         self.cleaned_list.append(Product(**product))

#                 except TypeError as e:
#                     print(f"TypeError, missing a parameter for product...{parameter}", e)
#                     break
            
#                 return self.cleaned_list



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