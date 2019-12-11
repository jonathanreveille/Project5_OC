import requests
from settings.settings import CATEGORIES


class ProductDownload:
    """ This class has the responsibility to download data from
    OpenFoodFact API """

    def __init__(self):
        self._url = "https://fr.openfoodfacts.org/cgi/search.pl"
        for category in CATEGORIES:
            self._params = {
                "action": "process",
                "tagtype_0": "categories",
                "tag_contains_0": "contains",
                "tag_0": category, #name of products (large)
                "sort_by": "unique_scans_n",
                "page_size": 100,
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
        print(type(self.data_product))
        
        self.product_list = [] #empty list

        self.product_list = self.data_product["products"]
        print(type(self.product_list))

        for product in self.product_list:
            print(product["product_name"], product["code"], product["stores"], product["categories"], product["url"])

            #working here NOW 



            

        #for product in self.product_list:
            #WORKS : print(product["product_name"], product["code"], product["url"])
        
        #product_downloaded = [] #Empty list to stock data of products
        #product_downloaded.append(self.data_product["products"]) # add those data into a list

        #return product_downloaded #returns a list

        # return self.data_product # this is a dictionnary

        #for product in self.data_product["products"]:
            #product["products"] = product
            #self.product_downloaded.append(product)

    def clean_data_product(self):
        """ This method is to clean all the data that 
        we gathered from .json data.
        We will eliminate all products that has None 
        values in our parameters """
        #for product in self.product_downloaded[0]:
            #print(product)
        pass
        
        




def main():
    data = ProductDownload()
    data.check_connexion()
    data.get_product_list()
    data.clean_data_product()

if __name__ == "__main__":
    main()


       # if "nutrition_grade_fr" in self.product_list[0]:
            #print("True for nutrition")  --> TRUE
       # else:
            #print('Nutrition is not present')
##
        #if "product_name" in self.product_list[0]:
           # print("TRUE for product_name") --> TRUE
       # else:
           # print("FALSE for product_name")

        #if "code" in self.product_list[0]:
           # print("TRUE for code") --> TRUE
        #else:
            #print("FALSE for code")

        #if "stores" in self.product_list[0]:
            #print("TRUE for stores")  --> TRUE
        #else:
            #print("FALSE for stores") 

        # BUT I CAN'T USE IT TO SELECT DATA FROM THE .JSON file that has been transformed into a list