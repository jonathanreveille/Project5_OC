
import requests

from bdd.models import Product

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
            "page_size": 200, #need to implement cleaning method to go above 90 for Pizza
            "json": 1
            }
        
    def check_connexion(self):
        """ This method is to download all data needed 
        from the URL, 
        output = if <Response 200> params 
        and url == everything is well set """
        
        connexion = True
        #self.response = statut.code()
        self.response = requests.get(self.url, params=self.params) # si pas de réseau = on arrivesur une exception. # Si le serveur ne répond 

        if connexion == False:
            print("<<Not connected to API>>")
        else:
            print("<<Connected to API>>")


    def fetch_data_from_API(self):
        """ This method is to transform what we received 
        from the API into .json format.
        We get in return a dictionnary field with data """

        self.data_product = self.response.json()
        #type(self.data_product)) # this a dict

        return self.data_product #becomes a list if we add : ...["products"]


    def get_product_data(self): 
        """  This method is to add to at our product [list]
        only the values from the keys that we need. """

        self.product_list = []
     
        for product in self.data_product["products"]:
            if self.is_valid_data(product):
                self.product_list.append(product) #contains only element with searched fields

        #compréhension de liste avec un dictionnaire
        #self.product_list = [Product.create(**product) for product in self.product_list] # c"est une liste d'instance de

        return self.product_list #on a une liste de dictionnaire avec toute les informations


    def is_valid_data(self, product):
        """ This method to validate the data that is present and complete
        --> we create a list of fields we want to search;
        --> check if the key exists;
        --> check if value exists for the key """

        fields = ["product_name", "nutrition_grade_fr", "categories", "brands", "stores", "url", "code"]

        for field in fields:
            if field not in product or not product[field]:
                print("Debugg1", f"{field}", " is missing info or keys for the product:", product.get("product_name"))
                return False

        return True


def main():
    a = ProductDownload()
    a.check_connexion()
    a.fetch_data_from_API()
    a.get_product_data()


if __name__ == "__main__":
    main()


    # def get_clean(self):
    #     """ this method is to create a clean dictionnary
    #     with only the keys and values that we look for """
        
    #     clean_list = []

    #     for product in self.data_product["products"]:    

    #         if self.is_valid_data(product) == True:
    #             clean_list.append(self.data_product["products"])

    #         if not self.is_valid_data(product):
    #             print("Debugg3", self.data_product.get("product_name"), "value is present.")
    #             continue
            
    #     return clean_list




    #LAST ONE 
    # def is_valid_data(self):
    #     """ this method is to validate that all our dictionnaries
    #     in our list :
    #     --> contains the key we look for
    #     --> contains a value to the key """

    #     fields = ["product_name", "nutrition_grade_fr", "categories", "brands", "stores", "url", "code"]

    #     for field in fields:

    #         if field not in self.data_product or not self.data_product[field]:
    #             print("Debugg1", self.data_product.get("product_name"), "is missing info or key")
    #             return False



        #print("DEBUGG1",type(self.data_product)) #dict
        #print(self.data_product['products']) #list
        #['products'] #if we add [products] in braket, it becomes a list self.data_product
        #print("DEBBUG",type(self.data_product["products"])) # this is a list


        # for product in self.data_product["products"]:
        #     self.products.append("product_name:" + product["product_name"]) #[0] Position
        #     self.products.append("nutrition_grade:" + product["nutrition_grade_fr"]) #[1]
        #     self.products.append("categories:" +product["categories"]) #[2]
        #     self.products.append("brands:" +product["brands"]) #[3]
        #     self.products.append("stores:" +product["stores"])#[4]
        #     self.products.append("url:" +product["url"]) #[5]
        #     self.products.append("code:" +product["code"]) #[6]

        # self.product_dict = {}

        # self.res = {key: self.data_product[key] for key in self.data_product.keys()
        #                        & { 'url', 'nutrition_grade_fr', 'product_name'}} 
        # self.product_dict = self.res

        # print("filtered results are : ", str(self.res))
        # return self.product_dict
       
        # try:
        #     for key in self.data_product:
                
            #for product in self.data_product:
                #self.product_list.append(key["nutrition_grade_fr"]) #maybe not present for every product
                # self.product_list.append(product["product_name"])
                # self.product_list.append(product["code"])
                # self.product_list.append(product["brands"])
                # self.product_list.append(product["stores"]) #need to seperate stores .split() .strip()
                # self.product_list.append(product["url"])
                # self.product_list.append(product["categories"]) #causes problems

        # except KeyError as k:
        #     print("DEBUGG", k, "in", key.get("product_name"), "is not present or has none in value for its key")
        #     pass



    # def check_if_data_present(self):
    #     """ this method is to check :
    #     if the key is present in dictionnary,
    #     and, if the key's value is not empty"""

    #     # those are the parameters that we are seeking for :
    #     parameters = ("nutrition_grade_fr", "product_name", "code", "brands", "stores", "url", "categories")

    #     for parameter in parameters:

    #         if parameter not in self.data_product:
    #             return False

    #         elif parameter not in self.data_product[parameter]:
    #             return False

    #         elif parameter in self.data_product:
    #             return True
            
    #         elif parameter in self.data_product[parameter]:
    #             return True

                # Je vérifie que chaque produit contient bien toute les clés recherchées
                # je vérifie que que chaque clé recherchée contient une donnée (information)
                # Si ne contient pas de clé, ni d'info : on rejet le produit
                # je récupère la ligne qui est complète que je sauve dans une nouvelle variable
                # je laisse de côté la ligne qui n'est pas complète

    # def create_product(self):
    #     """ this method is to create our products from our
    #     the information we have received from the API """

    #     cleaned_product = []

    #     for k, v in self.clean_list:
    #         if self.product_list[k] != None:
    #             elif v is not None:


    #             if k not in self.product_list:
    #                 try:
    #                     create_product_list.append(Product(**product))

    #                 except TypeError as t:
    #                     print("TypeError occured", t)


    # # @classmethod
    # def product_is_valid(cls, product):
    #     """ This method is to check if our product is valid
    # #     according to the parameters we want """
    #     # montrer les paramètres qu'on recherche (parameters)
    #     # vérifier que les données sont là (existe-t-il?)
    #     # vérifier si elles contiennent une donnée (sont-elles remplies?)

    #     parameters = ("product_name", "nutrition_grade_fr", "code", "brands", "stores", "url", "categories")

    #     for parameter in parameters:
    #         if parameter not in product or not product[parameter]:
    #             print("DEBUGG", product.get("product_name"), f"{parameter} not present or missing info")
    #             return False
    #     return True


    # def create_product(self):
    #     """ this method is to create objects Product from the 
    #     list we gathered from the API """
    #     pass

    

    # def cleaning_data(self, final_product):
        
    #     self.product_list = []

    #     for product in final_product.values():
    #         for product in self.data_product:
    #             if product.get('nutrition_grades') and product.get('product_name') \
    #             and product.get('stores') and product.get('id'):

    #                 final_product = {
    #                         'barcode' : product['id'],
    #                         'name': product['product_name'],
    #                         'category': product['main_category'],
    #                         'sub_category' : product['categories'].upper().split(","),
    #                         'grade': product['nutrition_grades'],
    #                         'store': product['stores'],
    #                         'url': product['url']
    #                         }

    #                 self.product_list.append(final_product)

    #     return self.product_list


        # try:
        #     for product in final_product.values():
        #         for product in self.data_product["products"]:

        #             if product.get('nutrition_grades') and product.get('product_name')\
        #             and product.get('stores') and product.get('id')\
        #             and product.get("brands") and product.get("url")\
        #             and product.get("code") and product.get("categories"):
                    
        #                 final_product = {
        #                         'nutriscore': product['nutrition_grades'], \
        #                         'name': product['product_name'],\
        #                         'category': product['categories'],\
        #                         'brands' : product['brands'],\
        #                         'store': product['stores'],\
        #                         'url': product['url'],\
        #                         'code': product['code']
        #                         }

        #                 self.products.append(final_product)

        # except KeyError as e:
        #     print("DEBUGG 0 :KeyError occured:", e, '->for the product :', product.get("product_name"))
            
        #     pass
        # print(self.products)
        # return self.products


            # self.product_list.append(product["nutrition_grade_fr"]) #maybe not present for every product
            # self.product_list.append(product["product_name"])
            # self.product_list.append(product["code"])
            # self.product_list.append(product["brands"])
            # self.product_list.append(product["stores"]) #need to seperate stores .split() .strip()
            # self.product_list.append(product["url"])
            # self.product_list.append(product["categories"]) #causes problems



