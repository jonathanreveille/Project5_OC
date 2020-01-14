# #! /usr/bin/env python3
# # coding : utf-8

# class Store: 
#     """ This class contains all information 
#     about stores """

#     def __init__(self, store):
#         self.name = store

#     def __repr__(self):
#         f"Store (name: {self.name})"


# class Category:
#     """ This class contains all the information 
#     about Categories """

#     def __init__(self, category):
#         self.name = category

#     def __repr__(self):
#         f"Category (name: {self.name})"


# class Brand:
#     """ This class contains all the information 
#     about the Brands"""

#     def __init__(self, brand):
#         self.name = brand

#     def __repr__(self):
#         f"Brand(name: {self.name})"


# class Product:
#     """ This class contains all information about product """

#     def __init__(self, code, url, product_name, stores, brands, nutrition_grade_fr, ingredients, categories, **kwargs):
        
#         self.code = code
#         self.name = product_name
#         self.url = url
#         self.brands = brands
#         self.nutrition_grade = nutrition_grade_fr
#         self.category = categories
#         self.stores = []

        # for store in stores.split(","):
        #     self.stores.append(Store(store.lower().strip()))
        

#     def __repr__(self):
#         return f"Product(name: {self.name})"





# def main():
#     pass

# if __name__ == "__main__":
#     pass




#     # @classmethod
#     # def is_valid(cls, product):
#     #     """ This method is to check if our product is valid
#     #     according to the parameters we want """

#     #     parameters = ("nutrition_grade_fr","product_name",\
#     #         "code", "brands","stores","url")

#     #     for parameter in parameters:

#     #         if parameter not in product or not product[parameter]:
#     #             return False
#     #     return True


#     # for parameter in parameters:
#     #     if parameter not in product or not product[parameter]:
#     #         not_valid_products.append(product)
#     #         print("-->DEBUGGING", product.get('product_name'), f"{parameter} not present or empty")
#     #         return False
#     #     else:
#     #         return True



#     # def is_valid(self, product):
#     #     """ This method is to check if all the data that 
#     #     we need are present and also, not empty """
#     #     # vérifier que les données sont là,
#     #     # vérifier si elles contiennent une donnée

#     #     is_valid = True

#     #     fields = ("product_name", "nutrition_grade_fr", "code", "brands", "stores", "url", "categories")

#     #     for field in fields:

#     #         if field not in product: #before : self.data_product
#     #             print("DEBBUGING --> there is a missing field or not info on product:", k, f"{field} in", self.data_product.get("product_name"))
#     #             return is_valid == False

#     #         elif not product:
#     #             return is_valid == False

#     #         return True
    

#         # self.final_list = [] # empty list to store all final products

#         # for product in self.data_product["products"]:

#         #     if not is_valid(*product):
#         #         continue
#         #         print("DEBUG", self.data_product.get('product_name'), "is present and has all info")

#         #     if is_valid(*product) == True:
            
#         #         self.cleaned_product.append(Product(**product))

#         # return self.cleaned_product


# dictionnaire = {'data_quality_errors_tags': [], 'additives_old_n': 4, 'emb_codes_orig': '', 'countries_tags': ['en:belgium', 'en:canada', 'en:france', 'en:guadeloupe', 'en:new-caledonia', 'en:reunion', 'en:switzerland'], 'image_ingredients_small_url': 'https://static.openfoodfacts.org/images/products/762/221/044/9283/ingredients_fr.288.200.jpg', 'ingredients_text_debug_tags': [], 'states': 'en:checked, en:complete, en:nutrition-facts-completed, en:ingredients-completed, en:expiration-date-completed, en:packaging-code-to-be-completed, en:characteristics-completed, en:categories-completed, en:brands-completed, en:packaging-completed, en:quantity-completed, en:product-name-completed, en:photos-validated, en:photos-uploaded', 'nucleotides_prev_tags': [], 'nutrition_score_beverage': 0, 'image_url': 'https://static.openfoodfacts.org/images/products/762/221/044/9283/front_fr.286.400.jpg', 'data_sources_tags': ['app-yuka', 'apps'], 'environment_impact_level_tags': [], 'allergens_from_ingredients': 'blé, lécithine de soja, lactose, protéines de lait'}

# print(dictionnaire["allergens_from_ingredients"])

# for d in dictionnaire:
#     for key in d:
#         print(d[key])

#    # print(key[value])

# "data_quality_errors_tags" in dictionnaire


# def find_in_dict(field=str()):
#     """ FONCTION POUR AJOUTER A MA LISTE LA VALEUR 
#     DE LA CLE DU DICTIONNAIRE """

#     if field in dictionnaire[field] or dictionnaire: # SI LE CHAMPS EST PRESENT
#         print(field[key])

# find_in_dict("allergens_from_ingredients")

   # def create_object_by_category(self):
    #     """ this module is to create all the different 
    #     categories that we will need for our application"""

    #     self.check_connexion()
    #     self.fetch_data_from_API()
    #     self.get_product_data()
    #     self.fill_product()
    #     print("You have created your objects")





#compréhension de liste avec un dictionnaire
#self.product_list = [Product.create(**product) for product in self.product_list] # c"est une liste d'instance de


#  def fill_database_prod(self):
#         """ This method is to populate database with products"""
        
#         for product in self.product_list:
#             Product.create(**product)
#             product.product_name.add(**product)
#             product.save()

#         for product in self.product_list:
#             for brand in product["brands"]:
#                 Brand.get_or_create(brand_name = brand)
#                 product.add(brand)
#                 product.save()


            # for category in product:
            #     Product.create(**product, category = category,\
            #         nutrition_grade_fr = product["nutrition_grade_fr"].split(","),
            #         url = product["url"],
            #         brand = product["brands"],
            #         stores = product["stores"].split(","))

                   # db.create_tables([Product])



            #Product.create(**product, category= category,\
            # nutrition_grade_fr = product["nutrition_grade_fr"],\
            # url= product["url"],\
            # brand = product["brands"],\
            # stores = product["stores"])


            # product = Product.create(product_name=product["product_name"],\
            #                             url = product["url"], \
            #                             store = product["stores"],\
            #                             brand = product["brands"],
            #                             category = self.category)


            #print(product["product_name"])
            
            #print(product["url"])
            #print(product["stores"]) #nécessite un .split(",").strip().lower()
            #print(product["brands"])
            #print(product["product_name"])
            #print(product["categories"])



        # category = Category.get_or_create(category_name = self.category.lower())

        # dict_to_model(Product, self.product_list)

            #for product["product"] in product:# REFLEXION
            # Product.get_or_create(category = category, \
            #                 code = product["code"], \
            #                 url = product["url"], \
            #                 nutrition_grade_fr = product["nutrition_grade_fr"], \
            #                 brand = product["brands"], \
            #                 store = product["stores"])
        
                # for store in product["stores"].split(","):
                #     Store.get_or_create(store_name = store.strip().lower())
                #     product.store.add(store)
                #     product.save()
                    
                #     for brand in product["brands"]:
                #         Brand.get_or_create(brand_name=brand)
                #         product.brand.add(brand)
                #         product.save()





            # for store in product["stores"]:
            #     Store.get_or_create(store_name= store.strip().lower())
            #     product.stores.add(store)

            #     for brand in product["brands"]:
            #         Brand.get_or_create(brand_name = brand)
            #         product.brands.add(brand)


        # for product in self.product_list:
        #     product = Product.create(**product)



            # for store in product["stores"].split(","):
            #     store = Store.get_or_create(store_name = store.strip().lower())
            #     product.stores.add(store)
            #     product.stores.save()
            
            #     for brand in product["brand"]:
            #         brand = Brand.get_or_create(brand_name= brand)
            #         product.brands.add(brand)
            #         product.brands.save()

#Originale
    # def fill_database_category(self):
    #     """ this method is to populate the category table """

    #     category = Category.get_or_create(category_name = self.category.lower())

    # def fill_database_product(self):

    #     for product in self.product_list:
    #         product = Product.create(category=category, **product)

    #         for store in product["stores"].split(","):
    #             store = Store.get_or_create(store_name = store.strip().lower())
    #             product.stores.add(store)
    #             product.stores.save()
            
    #             for brand in product["brand"]:
    #                 brand = Brand.get_or_create(brand_name= brand)
    #                 product.brands.add(brand)
    #                 product.brands.save()



        # for product in self.product_list:
        #     Product.insert_many(**product, fields=[Product.product_name, Product.code, Product.url, \
        #     Product.nutrition_grade_fr, Product.stores, Product.brands]).execute()

            # for store in product["stores"].split(","):
            #     store = Store.get_or_create(store_name = store.strip().lower())
            #     product.stores.add(store)
            #     product.stores.save()
            
            #     for brand in product["brand"]:
            #         brand = Brand.get_or_create(brand_name= brand)
            #         product.brands.add(brand)
            #         product.brands.save()


            # for brand in product["brands"]:
            #     brand = Brand.get_or_create(brand_name = brand.lower())
            #     brand.save()

        


        #category = Category.create(category_name = self.category.lower())

        # for product in self.product_list:
        #     product = Product.create(category=category, **product)

        #     for nutriscore in product["nutrition_grade_fr"]:
        #         nutriscore = Product.get_or_create(nutrition_grade_fr= nutriscore)
        #         product.nutrition_grade_fr.add(nutriscore)
        #         product.save()
            
        #         for store in product["stores"].split(","):
        #             store = Store.get_or_create(store_name = store.strip().lower())
        #             product.stores.add(store)
        #             product.save()

        #             for brand in product["brands"]:
        #                 brand = Brand.get_or_create(brand_name = brand.lower())
        #                 product.brands.add(brand)
        #                 product.save()

            #product = Product.create(category, **product) #(category_name = category, **product)
            #product = Product.create(category_name=category, **product) 
            #-> original : (category == category, **product) 

        # for product in self.product_list:

            # product = Product.create(category_name = category,
            #                         brand = brand, 
            #                         store = store,
            #                         url= url,
            #                         nutrition_grade_fr = nutriscore,
            #                          **product)

            #         product = Product.create(category_name=category,
            #                         code = product["code"],
            #                         product_name = product["product_name"],
            #                         url = product["url"],
            #                         nutrition_grade_fr= product["nutrition_grade_fr"],
            #                         brand= product["brands"],
            #                         store= product["stores"],
            #                         **product)

        # print("DEBBUG1 :", self.category.lower())
        # print("DEBBUG2 :", category)
        # print("DEBBUG3 :", str(category))



    # faire une boucle FOR...IN...changer l'attribut self.category par chacune des catégories dans notre attribut self.category.
    # categories = ['biscuits', 'pizza', 'soda']
    # for category in categories: # faire une boucle.





  

         #= [Category.create(**product) for product in self.product_list]
        
        # for category in self.product_list:
        #     category = Category.create(**category)
        
        # for store in self.product_list:
        #     store = Store.create(**store)

        # for product in self.product_list:
        #     product = Product.create(**product)

        # for store in self.product_list:
        #     store.split(",").lower()
        #     stores = Store.create(**store)

        # for product, stores in self.product_list:
        #     product = Product.create(product=product)

        #     #Store table
        #     for store in stores:
        #         store = Store.get(Store.store_name==store)
        #         ProductStore.create(product=product, store=store)

        # #         #Brand table
        #         for product, brands in self.product_list:
        #             product = Product.get(Product.product_name == product)
                    
        #             for brand in brands:
        #                 brand = Brand.create(brand_name=brand)
                                    
        #                 # for category table
        #                 for product, categories in self.product_list:
        #                     product = Product.get(Product.product_name == product)
        #                     for category in categories:

        #                         category = Category.create(category = category)

        # for product in self.product_list:
        #     product = Product.create(**product)

            # for store in self.product_list:
            #     store.split(",").lower()

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



